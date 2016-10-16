from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from books.models import buy



urlpatterns = [
	url(r'^$', ListView.as_view(queryset = buy.objects.all() .order_by ("-date")[:10] , template_name="books/books.html")),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model= buy, template_name= "books/buy.html")),
]
