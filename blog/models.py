from __future__ import unicode_literals
from django.utils import text
from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.db import models


@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length = 50, unique = True)
	slug = models.SlugField(max_length = 50, unique = True, editable = False)
	description = models.TextField(max_length = 120)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		db_table = 'blog_categories'
		verbose_name = 'category'
		verbose_name_plural = 'categories'
		ordering = ['-name']

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.set_slug()
		super(Category, self).save(*args, **kwargs)

	def set_slug(self):
		if (hasattr(self, 'name')):
			self.slug = text.slugify(self.name)
		else:
			self.slug = 'without-slug'

	def get_slug(self):
		return self.slug

	@permalink
	def get_absolute_url(self):
		return reverse('categories:details', kwargs = {'pk': self.pk})


@python_2_unicode_compatible
class Page(models.Model):
	title = models.CharField(max_length = 80, unique = True)
	slug = models.SlugField('slug', max_length = 160, null = True, blank = True, editable = False, unique = True)
	page_content = models.TextField('page_content', blank = True, null = True)
	date_created = models.DateTimeField(auto_now_add = True, editable = False)
	is_menu = models.BooleanField('navigation menu', default = True)
	category = models.ManyToManyField(Category, blank = True, db_table = 'blog_page_category_related')

	class Meta:
		db_table = 'blog_pages'
		ordering = ["-title"]
		verbose_name = "page"
		verbose_name_plural = "pages"

	def __str__(self):
		return self.title

	def set_slug(self):
		if (hasattr(self, 'title')):
			self.slug = text.slugify(self.title)
		else:
			self.slug = 'without-slug'

	def get_slug(self):
		return self.slug

	def save(self, *args, **kwargs):
		self.set_slug()
		if not self.id:
			self.date_created = now()
		super(Page, self).save(*args, **kwargs)

	@permalink
	def get_absolute_url(self):
		return reverse('pages:details', kwargs = {'pk': self.pk})

