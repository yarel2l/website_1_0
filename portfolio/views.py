from django.shortcuts import render_to_response, get_object_or_404
from .models import Project
from website_1_0.views import Homepage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PortfolioPage(Homepage):
	template_name = "portfolio/single_page.html"

	def get_context_data(self, slug= None, **kwargs):
		context = super(PortfolioPage, self).get_context_data(**kwargs)
		context['page'] = get_object_or_404(Project, slug = slug)
		context['related_projects'] = Project.objects.filter(project_type__services_projects_related__slug__exact = slug).exclude(slug = slug)
		return context


class ProjectsListPage(Homepage):
	template_name = 'portfolio/projects.html'

	def get(self, request,  slug = None, **kwargs):
		projects = Project.objects.filter(project_type__slug = slug)
		paginator = Paginator(projects, 5)  # Show 5 projects per page

		page = request.GET.get('page')
		try:
			projects = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			projects = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			projects = paginator.page(paginator.num_pages)
		context = super(ProjectsListPage, self).get_context_data(**kwargs)
		context['projects'] = projects
		return render_to_response(self.template_name, context)
