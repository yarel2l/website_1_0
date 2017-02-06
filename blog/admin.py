from django.contrib import admin
from .models import Page, Category


class PageAdmin(admin.ModelAdmin):
	list_display = ('name', 'picture', 'page', 'is_public')
	list_editable = ('picture', 'page', 'is_public')
	list_filter = ['name', 'is_public']
	list_per_page = 5
	fieldsets = (
		('Basic Information', {
			'fields': ('title', 'page_content', 'is_menu')
		}),
		('Select one Category', {
			'classes': ('collapse',),
			'fields': ('category',),
		}),

	)



admin.site.register(Page)
admin.site.register(Category)
