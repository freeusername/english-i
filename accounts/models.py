from __future__ import unicode_literals
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.templatetags.static import static
from django.utils import six
from django.utils import timezone
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib import auth
from django.contrib.contenttypes.models import ContentType
from imagekit.models.fields import ImageSpecField
from core.utils.helpers import get_file_path
from pilkit.processors import ResizeToFit, ResizeToFill

from courses.models import Course, Intensity, Duration


COURSE_NOTPAID = 'course_notpaid'
COURSE_PAID = 'course_paid'
COURSE_STARTED = 'course_started'
COURSE_FINISHED = 'course_finished'

COURSE_STATUS_VALUE = (
    (COURSE_NOTPAID, _('not paid')),
    (COURSE_PAID, _('paid')),
    (COURSE_STARTED, _('started')),
    (COURSE_FINISHED, _('finished')),
)


@python_2_unicode_compatible
class User(AbstractUser):
    phone = models.CharField(_('phone'), max_length=255, blank=True, null=True)
    city = models.CharField(_('city'), max_length=255, blank=True, null=True)
    company = models.CharField(_('company'), max_length=255, blank=True, null=True)
    skype = models.CharField(_('skype name'), max_length=255, blank=True, null=True)
    avatar = models.ImageField(_('avatar'), upload_to=get_file_path, blank=True, null=True)

    admin_thumb = ImageSpecField([ResizeToFit(height=60, upscale=False)], source='avatar')
    avatar_view = ImageSpecField([ResizeToFill(width=157, height=157, upscale=False)], source='avatar')
    avatar_mini = ImageSpecField([ResizeToFill(width=25, height=25, upscale=False)], source='avatar')

    class Meta(AbstractUser.Meta):
        db_table = 'accounts_users'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def save(self, *args, **kwargs):
        if self.username != self.email:
            self.username = self.email
        super(User, self).save(*args, **kwargs)

    @classmethod
    def get_admin(cls):
        return cls.objects.order_by('id').filter(is_superuser=True).first()

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name()

    @property
    def upload_dir(self):
        return 'users/avatars/'

    def admin_thumbnail(self):
        if self.avatar:
            return '<img src="{}" />'.format(self.admin_thumb.url)
        else:
            return ''
    admin_thumbnail.short_description = _('avatar')
    admin_thumbnail.allow_tags = True

    def get_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        name = '%s' % (self.first_name)
        return name.strip()


class UserCourse(models.Model):
    user = models.ForeignKey(User, related_name="users_course", verbose_name=_("user"))
    course = models.ForeignKey(Course, related_name="courses_course", verbose_name=_("course"))
    intensity = models.ForeignKey(Intensity, related_name="courses_course", verbose_name=_("intensity"), blank=True, null=True)
    duration = models.ForeignKey(Duration, related_name="courses_course", verbose_name=_("duration"), blank=True, null=True)
    status = models.CharField(_('status'), max_length=255, choices=COURSE_STATUS_VALUE, default=COURSE_NOTPAID)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return _("%(user)s subscribed to course %(course)s") % \
               {'user': self.user.full_name,
                'course': self.course.title}

    class Meta:
        verbose_name = _('user course')
        verbose_name_plural = _('user courses')