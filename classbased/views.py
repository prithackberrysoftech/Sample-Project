from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from classbased.forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin,View):
    login_url = "/admin/login/"   # or your custom login URL
    template_name = "classbased/profile.html"

    def get(self, request):
        profile_form = ProfileForm(instance=request.user.profile)
        password_form = PasswordChangeForm(user=request.user)

        return render(request, self.template_name, {
            "profile_form": profile_form,
            "password_form": password_form
        })

    def post(self, request):
        profile_form = ProfileForm(
            request.POST,
            instance=request.user.profile
        )
        password_form = PasswordChangeForm(
            user=request.user,
            data=request.POST
        )

        if "save_profile" in request.POST and profile_form.is_valid():
            profile_form.save()
            return redirect("profile")

        if "change_password" in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            return redirect("profile")

        return render(request, self.template_name, {
            "profile_form": profile_form,
            "password_form": password_form
        })
