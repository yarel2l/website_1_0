from django.contrib import admin
from .models import Promo, Project


class PromoInline(admin.StackedInline):
	model = Promo
	extra = 1


class ProjectAdmin(admin.ModelAdmin):
	inlines = [PromoInline]
	list_display = ('name', 'page', 'as_promo')
	list_editable = ('page', 'as_promo')
	list_filter = ['project_type', 'name', ]
	filter_horizontal = ['project_type', ]


admin.site.register(Project, ProjectAdmin)
