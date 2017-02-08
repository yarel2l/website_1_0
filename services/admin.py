from django.contrib import admin
from blog.models import Page
from .models import Service


class PageInline(admin.StackedInline):
	model = Page
	extra = 1


class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name', 'picture', 'page', 'is_public')
	list_editable = ('picture', 'page', 'is_public')
	list_filter = ['name', 'is_public']
	list_per_page = 5
	fieldsets = (
		('Basic Information', {
			'fields': ('name', 'resume_info')
		}),
		('Picture & Visibility in homepage', {
			'classes': ('collapse',),
			'fields': ('picture', 'is_public')
		}),
		('Add one Page describing service', {
			'classes': ('collapse',),
			'fields': ('page',),
		}),
	)


admin.site.register(Service, ServiceAdmin)
