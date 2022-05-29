import random

from braces.views import AnonymousRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView, View

from .forms import (
    LoginForm,
    PassChangeForm,
    RegisterForm,
    UserDocumentForm,
    UserUpdateForm,
    VerifyCodeForm,
)
from .models import OtpCode, UserDocument
from .uitils import send_otp

# Create your views here.
user = get_user_model()


class UserLoginView(View):
    form_class = LoginForm
    register_form = RegisterForm
    template_name = "accounts/auth.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(request.path)
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(
            request, self.template_name, {"form": form, "register_form": RegisterForm}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, user_name=cd["user_name"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, "با موفقیت وارد شدید", "info")
                return redirect("accounts:dashboard")
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است", "warning")
        return render(request, self.template_name, {"form": form})


# class UserLoginView(AnonymousRequiredMixin, FormView):
#     form_class = LoginForm
#     success_url = reverse_lazy("accounts:dashboard")
#     template_name = "accounts/auth.html"
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         cd = form.changed_data
#         user = authenticate(
#             self.request, user_name=cd["user_name"], password=cd["password"]
#         )
#         if user is not None:
#             login(self.request, user)
#             messages.success(self.request, "", "success")
#         else:
#             messages.error(self.request, "", "danger")
#         return super(UserLoginView, self).form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context_data = super(UserLoginView, self).get_context_data(**kwargs)
#         context_data["register_form"] = RegisterForm
#         return context_data
#
#     def form_invalid(self, form):
#         print(form.errors)
#         messages.error(self.request, form.errors, "danger")
#         return super(UserLoginView, self).form_invalid(form)


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "", "success")
        return redirect("accounts:login")


class UserRegisterView(AnonymousRequiredMixin, View):
    form_class = RegisterForm

    def post(self, request):
        form = self.form_class(request.POST)
        print(form.errors)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp(form.cleaned_data["phone_number"], random_code)
            OtpCode.objects.create(
                phone_number=form.cleaned_data["phone_number"], code=random_code
            )

            request.session["user_registration_info"] = {
                "phone_number": form.cleaned_data["phone_number"],
                "user_name": form.cleaned_data["user_name"],
                "email": form.cleaned_data["email"],
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "password": form.cleaned_data["password"],
            }
            messages.success(request, "کد برای شما ارسال شد", "success")
            return redirect("accounts:verify")


class UserRegisterVerifyCodeView(AnonymousRequiredMixin, View):
    form_class = VerifyCodeForm
    template_name = "accounts/verify.html"

    # def dispatch(self, request, *args, **kwargs):
    #     if request.META.get("HTTP_REFERER") == "":
    #         return super(UserRegisterVerifyCodeView, self).dispatch(
    #             request, *args, **kwargs
    #         )
    #     raise Http404

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        user_session = request.session["user_registration_info"]
        code_instance = OtpCode.objects.get(phone_number=user_session["phone_number"])
        form = self.form_class(request.POST)
        print(form.errors)
        print(form.cleaned_data)
        if form.is_valid():
            print(form.errors)
            cd = form.cleaned_data
            print(cd)
            print(code_instance.code)
            if cd["code"] == code_instance.code:
                user.objects.create_user(
                    first_name=user_session["first_name"],
                    last_name=user_session["last_name"],
                    user_name=user_session["user_name"],
                    email=user_session["email"],
                    phone_number=user_session["phone_number"],
                    password=user_session["password"],
                )
                code_instance.delete()
                messages.success(request, "you registered.", "success")
                return redirect("accounts:dashboard")
            else:
                messages.error(request, "this code is wrong", "danger")
                return redirect("accounts:verify")
        return redirect("accounts:verify")


class UserDashboard(LoginRequiredMixin, View):
    def get(self, request):
        user_obj = get_object_or_404(user, id=request.user.id)
        return render(request, "accounts/dashboard.html", {"user": user_obj})


class UserUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    def test_func(self, user):
        return self.get_object() == self.request.user

    model = user
    success_url = reverse_lazy("accounts:dashboard")
    template_name = "accounts/update.html"
    form_class = UserUpdateForm


class UserPassChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("accounts:dashboard")
    success_message = "رمز عبور با موفقیت تغییر یاقت"
    form_class = PassChangeForm

    def form_invalid(self, form):
        print(form.errors)
        return super(UserPassChangeView, self).form_invalid(form)


class UserDocCreatView(LoginRequiredMixin, View):
    form_class = UserDocumentForm
    template_name = "accounts/doc.html"

    def get(self, request):
        form = self.form_class(instance=request.user.document)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES, instance=request.user.document)
        if form.is_valid():
            form.save()
            messages.success(request, 'مدارک با موفقیت بارگذاری شد', 'success')
        return redirect('accounts:dashboard')
