from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    # signup
    url(r'^signup/$', views.signup, name='signup'),

    # dashboard homepage
    url(r'^info/$', views.info, name='info'),

]

