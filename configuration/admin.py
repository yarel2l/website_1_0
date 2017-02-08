from django.contrib import admin
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

	)


admin.site.register(Website, WebsiteAdmin)

