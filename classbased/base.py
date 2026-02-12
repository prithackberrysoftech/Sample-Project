# core/models/base.py

from django.db import models
from django.utils import timezone


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return super().update(is_deleted=True, is_active=False, updated_at=timezone.now())

    def hard_delete(self):
        return super().delete()

    def active(self):
        return self.filter(is_deleted=False, is_active=True)

    def deleted(self):
        return self.filter(is_deleted=True)


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(is_deleted=False)

    def all_with_deleted(self):
        return SoftDeleteQuerySet(self.model, using=self._db)

    def deleted_only(self):
        return self.all_with_deleted().deleted()


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SoftDeleteManager()
    all_objects = SoftDeleteManager()

    class Meta:
        abstract = True
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["is_deleted"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["created_at"]),
        ]

    def delete(self, using=None, keep_parents=False):
        """
        Soft delete parent + cascade to children
        """
        self.is_deleted = True
        self.is_active = False
        self.save()

        # Cascade soft delete
        for field in self._meta.related_objects:
            if field.on_delete == models.CASCADE:
                related_name = field.get_accessor_name()
                related_manager = getattr(self, related_name)
                related_manager.all().update(is_deleted=True, is_active=False)

    def restore(self):
        """
        Restore parent + cascade restore to children
        """
        self.is_deleted = False
        self.is_active = True
        self.save()

        for field in self._meta.related_objects:
            if field.on_delete == models.CASCADE:
                related_name = field.get_accessor_name()
                related_manager = getattr(self, related_name)
                related_manager.all().update(is_deleted=False, is_active=True)

    def hard_delete(self):
        super().delete()
