"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from slideshow.views import change_lang, logout_view


urlpatterns = [
    path('change_lang', change_lang, name='change_lang'),
    
]

urlpatterns += (
    path('admin/', admin.site.urls),
    path('', include("slideshow.urls")),
    path('logout/', logout_view, name='logout'),
    path('', include('social_django.urls', namespace='social')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 