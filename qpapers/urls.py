from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from qpapers.models import ques

urlpatterns = [url(r'^$', ListView.as_view(queryset=ques.objects.all() .order_by("-date")[:25], template_name="qpapers/qpapers.html")),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model= ques, template_name= "qpapers/details.html")),
]
