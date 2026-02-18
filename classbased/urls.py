from django.urls import path
from classbased.views import ProfileView, HomeView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("", HomeView.as_view(), name="home"),
]
