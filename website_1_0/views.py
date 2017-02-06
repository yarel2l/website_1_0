from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from configuration.models import Website
from services.models import Service
from portfolio.models import Project, Promo
from django.views.generic import View, TemplateView
import datetime


class Homepage(TemplateView):
	template_name = 'base.html'

	def get_context_data(self, **kwargs):
		context = super(Homepage, self).get_context_data(**kwargs)
		context['homepage'] = self.get_site_configuration
		context['services'] = self.services_section
		context['projects'] = self.portfolio_section
		context['promo'] = self.promos_section
		context['current_year'] = self.get_year
		return context

	def get_year(self):
		return str(datetime.datetime.now().year)

	def get_site_configuration(self):
		return get_object_or_404(Website, is_active = True)

	# Methods for load sections Service, Portfolio, Team and Contact in homepage#
	def services_section(self):
		public_services = Service.objects.all().filter(is_public = True)
		return public_services

	def portfolio_section(self):
		projects = Project.objects.all()
		return projects

	def promos_section(self):
		return Promo.objects.get(project__as_promo = True)

# class Homepage(View):
# 	template_name = 'base.html'
# 	# services = None
# 	# projects = None
#
# 	def __init__(self):
# 		self.website_info = self.get_site_configuration()
# 		self.services = self.service_section
# 		self.projects = self.portfolio_section
#
# 	def get(self, request, slug= None):
# 		content = {
# 			'homepage': self.website_info,
# 			'current_year': self.get_year(),
# 			'service_list': self.service_section,
# 			'projects_list': self.portfolio_section
# 		}
# 		return render(request, self.template_name, content)
#
# 	def get_year(self):
# 		return str(datetime.datetime.now().year)
#
# 	def get_site_configuration(self):
# 		return get_object_or_404(Website, is_active = True)
# 	# Methods for load sections Service, Portfolio, Team and Contact in homepage#
#
# 	def service_section(self):
# 		public_services = Service.objects.all().filter(is_public = True)
# 		return public_services
#
# 	def portfolio_section(self):
# 		projects = Project.objects.all()
# 		return projects
#
# 	def promos_section(self):
# 		return render_to_response('portfolio/promos.html', {'promo': Project.objects.get(as_promo = True)})
#
# 	def hire_us_section(self):
# 		return render_to_response('contact/hire_us.html', {}, content_type = 'text/html')




