from . import views
from django.conf.urls import url

app_name = "snippets"
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^detail/(?P<snippet_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name="add")
]
