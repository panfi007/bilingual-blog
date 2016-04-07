from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


def get_image_filename(instance, filename):
    title = instance.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(_('title'), max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    image = models.ImageField(_('image'), upload_to=get_image_filename, blank=True)
    body = models.TextField(_('body'))
    publish = models.DateTimeField(_('publish'), default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'), self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(_('name'), max_length=100)
    occupation = models.CharField(_('occupation'), max_length=150)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    photo = models.ImageField(_('photo'), upload_to='users/%Y/%m/%d', blank=True)
    description = models.TextField(_('description'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user)