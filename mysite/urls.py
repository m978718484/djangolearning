from django.conf.urls.defaults import *
from contact import views as contactviews
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
    #url(r'^$','polls.views.index' , name='index'),
    url(r'^polls/',include('polls.urls')),
    url(r'^books/',include('books.urls')),
    url(r'^admin/',admin.site.urls),
    url(r'^contact_form/',contactviews.contact_form),
    url(r'^contact/',contactviews.contact),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
