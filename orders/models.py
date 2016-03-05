from django.db import models
from django.utils.translation import ugettext_lazy as _

from courses.models import Course

class Order(models.Model):
    user = models.ForeignKey('accounts.User', related_name='order_user', verbose_name='user')
    course = models.ForeignKey(Course, related_name='order_course', verbose_name='course')

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return _("Order by %(user)s on the course %(course)s") % \
            {'user': self.user.full_name,
             'course': self.course.title}

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')