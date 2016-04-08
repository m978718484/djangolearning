from django.conf.urls.defaults import *
import views

urlpatterns=patterns('',
	url(r'^search_form/$',views.search_form),
	url(r'^contact_form/$',views.contact_form),
	#url(r'^search/$',views.search),
	url(r'^test/$',views.test),
)