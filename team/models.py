from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from configuration.models import CHOICES_NETWORKS
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils import text


class Team(models.Model):
	name = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 50, editable = False)
	department = models.CharField(max_length = 100)

	class Meta:
		db_table = 'website_teams'
		verbose_name = 'team'
		verbose_name_plural = 'teams'

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
		super(Team, self).save(*args, **kwargs)

	@permalink
	def get_absolute_url(self):
		return reverse('team:members', kwargs = {'slug': self.slug})


class Profile(models.Model):
	bio = models.CharField(max_length = 250)
	networks = models.CharField(max_length = 50, choices = CHOICES_NETWORKS)
	role = models.CharField(max_length = 50)
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	team = models.ForeignKey(Team, on_delete = models.DO_NOTHING)

	class Meta:
		db_table = 'website_members_profile'
		verbose_name = 'profile'
		verbose_name_plural = 'profiles'


