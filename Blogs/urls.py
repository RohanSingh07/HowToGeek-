from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from Blogs.views import HomeView,BlogView,AboutView,ContactView,AddBlog,EditBlog

app_name ="Blogs"

urlpatterns = [

    path('',HomeView,name='HomeView'),
    path('Blog/<slug>',BlogView,name='BlogView'),
    path('About/',AboutView,name='AboutView'),
    path('Contact/',ContactView,name='ContactView'),
    path('AddBlog/',AddBlog,name='AddBlog'),
    path('EditBlog/<slug>',EditBlog,name='EditBlog'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)