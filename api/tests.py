from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Order


class UserOrderTestCase(TestCase):

    def setUp(self):   # ✅ correct spelling
        self.user1 = User.objects.create_user(username="user1", password="user1")
        self.user2 = User.objects.create_user(username="user2", password="user2")

        Order.objects.create(user=self.user1)
        Order.objects.create(user=self.user1)
        Order.objects.create(user=self.user2)
        Order.objects.create(user=self.user2)

    def test_user_order_endpoint_retrieves_only_authenticated_user_orders(self):
        user = self.user2
        self.client.force_login(user)

        response = self.client.get(reverse('user_order_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        orders = response.json()
        self.assertTrue(all(order['user'] == user.id for order in orders))

    def test_user_order_list_unauthenticated(self):
        response = self.client.get(reverse('user_order_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
