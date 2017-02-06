from __future__ import unicode_literals

from django.db import models
from blog.models import Page
from services.models import Service
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils import text


CHOICES_PROJECT_TYPE = (
	('DA', 'Digital Animation'),
	('VG', 'Video Games'),
	('VR', 'Virtual Reality'),
	('SB', 'Story Boards'),
	('WD', 'Web Development'),
	('O', 'Other'),
)

def portfolio_directory_path(instance, filename):
	return str('portfolio/project_{0}/{1}'.format(instance.slug, filename))



class Project(models.Model):
	name = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 50, editable = False)
	project_type = models.ManyToManyField(Service, related_name = 'services_projects_related', db_table = 'website_services_projects')
	cover = models.ImageField(upload_to = portfolio_directory_path, width_field= "width_field", height_field= "height_field")
	width_field = models.IntegerField(default = 0)
	height_field = models.IntegerField(default = 0)
	page = models.OneToOneField(Page, on_delete = models.CASCADE, blank = True, null = True)
	as_promo = models.BooleanField(default = False, verbose_name = 'Show as Promotional Project')

	class Meta:
		db_table = 'website_portfolio'
		verbose_name = 'project'
		verbose_name_plural = 'projects'
		ordering = ['-name']

	def __str__(self):
		return self.name

	def set_slug(self):
		if (hasattr(self, 'name')):
			self.slug = text.slugify(self.name)
		else:
			self.slug = 'without-slug'

	def get_slug(self):
		return self.slug

	def save(self, *args, **kwargs):
		self.set_slug()
		super(Project, self).save(*args, **kwargs)

	@permalink
	def get_absolute_url(self):
		return reverse('portfolio:show_info', kwargs = {'slug': self.slug})


class Promo(models.Model):
	project = models.OneToOneField(Project, on_delete = models.CASCADE)
	status = models.CharField(max_length = 50)
	subtitle = models.CharField(max_length = 50)

	class Meta:
		db_table = 'website_portfolio_promo'

