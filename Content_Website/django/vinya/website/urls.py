from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name="HomePage"),
    url(r'^login/$', views.log_in, name="Login"),
    url(r'^logout/$', views.log_out, name="Logout"),
    url(r'^add_post/$', views.add_post, name="AddPost"),
    url(r'^del_post/(?P<post_id>[0-9]+)/$', views.delete_post, name="DeletePost")
]
