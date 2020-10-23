"""censo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path

from formulario import views


urlpatterns = [
	path("select2/", include("django_select2.urls")),
    path('admin/', admin.site.urls),
    path('', views.post_city, name='post_city'),
    path('andamento/', views.mapped_cities, name='mapped_cities'),
    path('faq/', views.faq, name='faq'),
    path('sobre/', views.about, name='about'),
    path('get-data/', views.download_csv_data, name='get_data'),

]
