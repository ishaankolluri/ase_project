from django.conf.urls import url

from . import views

app_name = "simulator"
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^$', views.home, name='home'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signedup/', views.signedup, name='signedup'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^getstockdata_views/',views.getstockdata_views,name='getstockdata_views'),
    url(r'^market_execution/', views.market_execution, name="market_execution"),
]
