from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.utils import text
from blog.models import Page
from django.db import models


def website_directory_services_path(instance, filename):
    return str('services/service_{0}/{1}'.format(instance.slug, filename))


@python_2_unicode_compatible
class Service(models.Model):
	name = models.CharField(max_length = 50, help_text = "Use a short name, max length permitted = 50", unique = True)
	slug = models.SlugField(max_length = 50, editable = False, unique = True)
	resume_info = models.TextField(max_length = 250, help_text = "Describe briefly about service, max length is 250 characters")
	picture = models.ImageField(upload_to = website_directory_services_path)
	is_public = models.BooleanField(default = False)
	page = models.OneToOneField(Page, on_delete = models.CASCADE, blank = True, null = True)

	@permalink
	def get_absolute_url(self):
		return reverse('services:show_info', kwargs = {'slug': self.slug})

	def __str__(self):
		return self.name

	def set_slug(self):
		self.slug = text.slugify(self.name)

	def save(self, *args, **kwargs):
		self.set_slug()
		super(Service, self).save(*args, **kwargs)

	class Meta:
		db_table = 'website_services'
		verbose_name = 'service'
		verbose_name_plural = 'services'
		ordering = ['name']

