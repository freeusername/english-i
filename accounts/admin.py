from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm

from .models import User, UserCourse

class CourseInline(admin.TabularInline):
    model = UserCourse
    fk_name = "user"
    extra = 0

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('id', '__str__', 'email', 'is_superuser', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('id', 'username', 'email', 'password',)}),
        ('Personal info', {
            'fields': (
                'first_name', 'last_name', 'city', 'phone', 'date_joined', 'company', 'avatar',
            )
        }),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    readonly_fields = ('id', 'date_joined',)
    filter_horizontal = ('user_permissions',)
    list_display_links = ('__str__', 'email')
    inlines = [CourseInline]

admin.site.register(User, UserAdmin)