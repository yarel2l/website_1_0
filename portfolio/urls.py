from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'(?P<slug>[a-z0-9-]+)/page/$', views.PortfolioPage.as_view(), name = 'show_info'),
	url(r'projects/by/(?P<slug>[a-z0-9-]+)/service/$', views.ProjectsListPage.as_view(), name = 'list'),
]
