from django.contrib import admin
from classbased.models import Book, Profile
from django.contrib.auth.models import User ,Group 
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = "Book Management System"
admin.site.site_title = "Book Admin"
admin.site.index_title = "Welcome to Admin Dashboard"


def make_free(modeladmin, request, queryset):
    queryset.update(price=0)


make_free.short_description = "Make selected books free"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "author", "price", "created_at", "slug")
    list_filter = (
        "price",
        "created_at",
    )
    search_fields = ("title", "author")
    ordering = ("order",)
    list_editable = ("price",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at",)
    actions = [make_free]
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (("order", "title", "author"),),
            },
        ),
        ("Price Info", {"fields": ("price", "slug")}),
    )


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.unregister(Group)
        