from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hzp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'hzp.kgapp.views.test'),
    url(r'^main/', 'hzp.kgapp.views.mainProcess'),
    url(r'^import/', 'hzp.kgapp.views.importData2Product'),
)
