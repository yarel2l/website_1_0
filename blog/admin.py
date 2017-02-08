from django.contrib import admin
from .models import Page, Category

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'date_created', 'is_menu', )
	list_editable = ('title', 'is_menu', )
	list_filter = ['title', 'date_created']
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


admin.site.register(Page, PageAdmin)
admin.site.register(Category)

