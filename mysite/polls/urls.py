from django.conf.urls.defaults import *
import views
urlpatterns = patterns('',
    url(r'^$','polls.views.index' , name='index'),
    url(r'^latest/$', views.latest_books),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^time/$',views.current_time),
    url(r'^mytime/$',views.current_time_upgrade),
    url(r'^time_from_template/$',views.current_time_from_template),
    url(r'^hello/$',views.hello),
    url(r'^current_url/$',views.current_url_view_good),
    url(r'^meta_test/$',views.meta_test),
    url(r'^mytemplate/$',views.mate_template)
)