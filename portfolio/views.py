from django.shortcuts import render, get_object_or_404
from .models import Project
from website_1_0.views import Homepage


class PortfolioPage(Homepage):
	template_name = "portfolio/single_page.html"

	def get_context_data(self, slug= None, **kwargs):
		context = super(PortfolioPage, self).get_context_data(**kwargs)
		context['page'] = get_object_or_404(Project, slug = slug)
		context['related_projects'] = Project.objects.filter(project_type__services_projects_related__slug__exact = slug).exclude(slug = slug)
		return context
