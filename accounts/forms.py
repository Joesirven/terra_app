from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "date_of_birth", "role", "email", "phone", "image", "is_staff", "is_active",)


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields + ("first_name", "last_name", "date_of_birth", "role", "email", "phone", "image", "is_staff", "is_active",)
