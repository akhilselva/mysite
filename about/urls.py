from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from about.models import about

urlpatterns = [
	url(r'^$', ListView.as_view(queryset = about.objects.all() .order_by ("-date")[:10] , template_name="about/blog.html")),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model= about, template_name= "about/post.html")),
]
