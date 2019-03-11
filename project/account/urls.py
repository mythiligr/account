from django.conf.urls import url
from account import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login', views.login_view, name='login'),
    url(r'^logout$', views.logout, name='user_logout'),
    url(r'^account/signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url('', TemplateView.as_view(template_name='account/home.html'), name='home'),
]