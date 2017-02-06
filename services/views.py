from django.shortcuts import get_object_or_404
from .models import Service
from website_1_0.views import Homepage


class ServicePage(Homepage):
	template_name = "services/single_page.html"

	def get_context_data(self, slug= None, **kwargs):
		context = super(ServicePage, self).get_context_data(**kwargs)
		context['page'] = get_object_or_404(Service, slug = slug)
		context['services'] = Service.objects.all().exclude(slug = slug)
		return context


