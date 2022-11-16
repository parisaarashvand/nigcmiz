from django.contrib import admin
from django.urls import path,include
from . import view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nigcMizApp.urls')),
#    path('about/',view.about),
#    path('nigcMiz/',include('nigcMizApp.urls')),
#    path('reqlist/' ,include('nigcMizApp.urls')),


]

urlpatterns += staticfiles_urlpatterns()
