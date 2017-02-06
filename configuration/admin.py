from django.contrib import admin
from django.db import models
from .models import Website, SocialNetworks


class SocialNetworkInline(admin.StackedInline):
	model = SocialNetworks
	extra = 4

class WebsiteAdmin(admin.ModelAdmin):
	inlines = [SocialNetworkInline]
	list_display = ('sitename', 'slogan', 'description', 'is_active')
	search_fields = ('sitename',)
	list_editable = ('is_active',)
	list_filter = ['sitename', 'is_active']
	list_per_page = 5
	fieldsets = (
		('Basic Information', {
			'fields': ('sitename', 'slogan', 'description', 'is_active')
		}),
		('Header Video', {
			'classes': ('collapse',),
			'fields': ('header_video_poster', 'header_video'),
		}),
		# ('Social Networks', {
		# 	'classes': ('collapse',),
		# 	'fields': SocialNetworkInline,
		# }),
	)

	# def formfield_for_foreignkey(self, db_field, request, **kwargs):
	# 	if db_field.name == "car":
	# 		kwargs["queryset"] = SocialNetworks.objects.filter(website = request.sitename)
	# 	return super(WebsiteAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Website, WebsiteAdmin)
admin.site.register([
	#SocialNetworks,
])
