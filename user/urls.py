from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include, reverse_lazy
from user.apps import UserConfig

from .forms import CustomAuthenticationForm
from user.views import RegisterView, VerifyView, UsersListView, UserDetailView, UserProfileView, UserProfileEditView, \
    UserBlockView, UserEndBlockView, DeleteProfileView, UserPasswordChange

app_name = UserConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("verify/", VerifyView.as_view(), name="verify"),
    path("login/", LoginView.as_view(template_name="user/login.html", form_class=CustomAuthenticationForm), name="login"),
    path("logout/", LogoutView.as_view(next_page="mailings:campaign_list"), name="logout"),
    path("user/", UsersListView.as_view(), name="user_list"),
    path("user/detail/<str:username>/", UserDetailView.as_view(), name="user_detail"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("profile/edit/", UserProfileEditView.as_view(), name="edit_profile"),
    path("profile/block/<str:username>/", UserBlockView.as_view(), name="user_block"),
    path("profile/endblock/<str:username>/", UserEndBlockView.as_view(), name="user_end_block"),
    path("profile/delete/<str:username>/", DeleteProfileView.as_view(), name="delete_profile"),
    path("password-change/", UserPasswordChange.as_view(), name="password_change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(template_name="user/password_change_done.html"), name="password_change_done"),
    path("password-reset/", PasswordResetView.as_view(template_name="user/password_reset_form.html", email_template_name="user/password_reset_email.html", success_url=reverse_lazy("user:password_reset_done")), name="password_reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"), name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html", success_url=reverse_lazy("user:password_reset_complete")), name="password_reset_confirm"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"), name="password_reset_complete")
]
