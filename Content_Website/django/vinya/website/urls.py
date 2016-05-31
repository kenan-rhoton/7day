from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name="HomePage"),
    url(r'^login/$', views.log_in, name="Login"),
    url(r'^logout/$', views.log_out, name="Logout")
]
