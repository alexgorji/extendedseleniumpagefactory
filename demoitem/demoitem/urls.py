"""
URL configuration for demoitem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo-items/', TemplateView.as_view(template_name='demo_list.html'), name='demo_items'),
    path('demo-create-item/', TemplateView.as_view(template_name='demo_create.html'), name='demo_create_item'),
    path('demo-load-element', TemplateView.as_view(template_name='demo_load_element.html'), name='demo_load_element'),
    path('demo-item-detail/', TemplateView.as_view(template_name='demo_detail.html'), name='demo_item_detail'),
]
