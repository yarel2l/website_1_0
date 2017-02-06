from __future__ import unicode_literals
from django.utils import text
from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.db.models.signals import pre_save


def website_directory_videos_path(instance, filename):
    return str('configs/site_{0}/videos/{1}'.format(instance.slug, filename))

def website_directory_images_path(instance, filename):
    return str('configs/site_{0}/videos/{1}/poster/{2}'.format(instance.slug, instance.header_video.name, filename))

CHOICES_NETWORKS = (
	('YT', 'YouTube'),
	('FB', 'Facebook'),
	('TW', 'Twitter'),
	('IN', 'Linkedin'),
)

@python_2_unicode_compatible
class Website(models.Model):
	sitename = models.CharField(max_length = 50, default = 'Locomotion USA', unique=True)
	slug = models.SlugField(max_length = 50, editable = False)
	slogan = models.CharField(max_length = 120, default = 'Animation & Interactive')
	description = models.CharField(max_length = 120, default = 'Here some description used in footer section')
	header_video_poster = models.FileField(upload_to = website_directory_images_path)
	header_video = models.FileField(upload_to = website_directory_videos_path, blank = True, null = True)
	is_active = models.BooleanField(default = False)

	def __str__(self):
		return self.sitename

	def set_slug(self):
		self.slug = text.slugify(self.sitename)

	def save(self, *args, **kwargs):
		self.set_slug()
		if hasattr(self, 'is_active') and self.is_active == True:
			Website.objects.filter(is_active = True).update(is_active = False)
		super(Website, self).save(*args, **kwargs)

	@permalink
	def get_absolute_url(self):
		return reverse('website:details', kwargs = {'pk': self.slug})

	def get_networks(self):
		website = Website.objects.get(pk = self.id)
		social_networks = website.socialnetworks_set.all()
		return social_networks
	get_networks.short_description = 'Social Networks'

	class Meta:
		db_table = 'website_configuration'
		verbose_name = 'configuration'
		verbose_name_plural = 'global settings'
		ordering = ['-sitename']

@python_2_unicode_compatible
class SocialNetworks(models.Model):
	name = models.CharField(max_length = 50, choices = CHOICES_NETWORKS)
	url = models.URLField(max_length = 160, help_text = "Use Network URL. Ex: https://www.linkedin.com/locomotion-usa")
	website = models.ForeignKey(Website, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'website_networks'
		verbose_name = 'network'
		verbose_name_plural = 'networks'
		ordering = ['-name']


# Signals
# def signal_update_conf_activation(sender, instance, *args, **kwargs):
# 	if hasattr(sender, str(instance.is_active)) and instance.is_active == True:
# 		Website.objects.filter(is_active = True).update(is_active= False)
# 	return instance
#
#
# pre_save.connect(signal_update_conf_activation, sender= Website)