from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext
from imagekit.models.fields import ImageSpecField
from core.utils.helpers import get_file_path, get_grammatical_case
from pilkit.processors import ResizeToFit, ResizeToFill
from uuslug import uuslug

from core.configs.models import AppConfig

COURSE_FRONT = 'course_front'
COURSE_PERSONAL = 'course_personal'

COURSES_TYPES = (
    (COURSE_FRONT, _('Course front')),
    (COURSE_PERSONAL, _('Course personal')),
)


class Skill(models.Model):
    position = models.PositiveSmallIntegerField(_('position'), default=0)
    show = models.BooleanField(_('show link?'), default=False)
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    lessons = models.PositiveSmallIntegerField(_('lessons'), default=0)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['position']
        verbose_name = _('skill')
        verbose_name_plural = _('skills')


class Course(models.Model):
    value_type = models.CharField(_('type'), max_length=255, choices=sorted(list(COURSES_TYPES), key=lambda ct: ct[1]),
                                  default=COURSE_FRONT)

    # Font course #
    position = models.PositiveIntegerField(_('position'), default=0)
    featured = models.BooleanField(_('featured'), default=False)
    skill = models.ForeignKey(Skill, related_name='course_skill', verbose_name='skill', blank=True, null=True)
    title = models.CharField(_('title'), max_length=255, blank=True, null=True)
    slug = models.SlugField(_('URL-path'), max_length=255, blank=True, unique=True,
                            help_text=_('If you do not specify this field, '
                                        'it will be generated <b>automatically</b>.'))
    short_description = models.TextField(_('short description'), blank=True, null=True)
    description = models.TextField(_('description'), blank=True, null=True)
    lessons = models.PositiveSmallIntegerField(_('number of lessons'), blank=True, null=True)
    duration = models.PositiveSmallIntegerField(_('course duration'), blank=True, null=True)
    pros_cons = models.TextField(_('pros and cons of the course'), blank=True, null=True)
    price = models.DecimalField(_('price'), default=0, max_digits=20, decimal_places=2, blank=True)
    preview = models.ImageField(_('preview'), upload_to=get_file_path, blank=True, null=True)
    image = models.ImageField(_('image'), upload_to=get_file_path, blank=True, null=True)

    # Personal Course #
    user = models.ForeignKey('accounts.User', related_name='personalcourse_user', verbose_name='user', blank=True,
                             null=True)
    skills = models.ManyToManyField(Skill, related_name='personalcourse_skills', verbose_name='skills', blank=True)
    no_skills = models.BooleanField(_('leave it for professionals'), default=False)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    admin_thumb = ImageSpecField([ResizeToFit(height=60, upscale=False)], source='image')
    preview_main = ImageSpecField([ResizeToFit(width=136, upscale=False)], source='preview')
    image_main = ImageSpecField([ResizeToFill(width=332, height=402, upscale=False)], source='image')

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return 'Custom course %s' % self.pk

    @property
    def get_course_title(self):
        return self.__unicode__

    def get_lessons(self):
        return get_grammatical_case(self.lessons,
                                    pgettext('1', 'lesson'),
                                    pgettext('2-4', 'lessons'),
                                    pgettext('5+', 'lessons'))

    def get_duration(self):
        return get_grammatical_case(self.duration,
                                    pgettext('1', 'month'),
                                    pgettext('2-4', 'months'),
                                    pgettext('5+', 'months'))

    @property
    def get_price_ru(self):
        return self.price * AppConfig.objects.get(key='currency_rate', enabled=True).value

    def get_skills_list(self):
        skills = self.skills.all()
        return skills

    def save(self, *args, **kwargs):
        if not self.title and self.value_type == 'course_personal':
            course = Course.objects.filter(user=self.user, value_type='course_personal')
            sum = len(course)+1
            self.title = _('Custom course %s') % sum
        if not self.slug:
            if self.title and self.value_type == 'course_front':
                self.slug = uuslug(self.title, instance=self)
            else:
                self.slug = uuslug('%s' % self.pk, instance=self)
        super(Course, self).save(*args, **kwargs)

    @property
    def upload_dir(self):
        return "courses/images"

    def admin_thumbnail(self):
        if self.image:
            return '<img src="{}" />'.format(self.admin_thumb.url)
        else:
            return ''

    admin_thumbnail.short_description = _('image')
    admin_thumbnail.allow_tags = True

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')


class Intensity(models.Model):
    position = models.PositiveSmallIntegerField(_('position'), default=0)
    recommended = models.BooleanField(_('recommended?'), default=False)
    title = models.CharField(_('title'), max_length=255, blank=True, null=True)
    description = models.TextField(_('description'), blank=True, null=True)
    lessons = models.DecimalField(_('lessons'), default=0, max_digits=10, decimal_places=0)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return self.title

    def get_duration(self):
        return Duration.objects.filter(intensity=self)

    def get_lessons(self):
        return get_grammatical_case(self.lessons, pgettext('1', 'lesson'), pgettext('2-4', 'lessons'), pgettext('5+', 'lessons'))

    def get_first_duration(self):
        duration = Duration.objects.filter(intensity=self).first()
        return duration

    # def save(self, *args, **kwargs):
    #     durations = Duration.objects.filter(intensity=self)
    #     for dur in durations:
    #         dur.save()
    #     super(Intensity, self).save(*args, **kwargs)

    class Meta:
        ordering = ['position']
        verbose_name = _('intensity')
        verbose_name_plural = _('intensities')


class Duration(models.Model):
    intensity = models.ForeignKey(Intensity, related_name='duration_intensity', verbose_name='intensity')
    duration = models.DecimalField(_('duration'), max_digits=10, decimal_places=0, default=60)
    price = models.DecimalField(_('price'), max_digits=20, decimal_places=2, blank=True, null=True)
    full_price = models.DecimalField(_('full price'), max_digits=20, decimal_places=2, blank=True, null=True,
                                     editable=False)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return _("Duration %(duration)s minutes to the intensity of %(intensity)s") % \
               {'duration': self.duration,
                'intensity': self.intensity.title}

    @property
    def get_price_ru(self):
        return self.price * AppConfig.objects.get(key='currency_rate', enabled=True).value

    @property
    def get_full_price_ru(self):
        return self.full_price * AppConfig.objects.get(key='currency_rate', enabled=True).value

    def save(self, *args, **kwargs):
        self.full_price = self.price * self.intensity.lessons
        super(Duration, self).save(*args, **kwargs)

    class Meta:
        ordering = ('duration',)
        verbose_name = _('duration')
        verbose_name_plural = _('durations')
