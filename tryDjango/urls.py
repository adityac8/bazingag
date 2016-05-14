from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.index', name='index'),
    url(r'^atndnce/$', 'profiles.views.atndnce', name='atndnce'),
    url(r'^about/$', 'profiles.views.about', name='about'),    
    url(r'^profile/$', 'profiles.views.profile', name='profile'),    
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    url(r'^courses/$', 'profiles.views.courses', name='courses'),
    url(r'^accounts/', include('allauth.urls')),


    
    url(r'^pyth/$', 'profiles.views.pyth', name='pyth'),
    url(r'^cpp/$', 'profiles.views.cpp', name='cpp'),
    url(r'^java/$', 'profiles.views.java', name='java'),
   
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)