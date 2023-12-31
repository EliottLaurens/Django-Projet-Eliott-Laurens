"""
URL configuration for equipment_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from equipment_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('teachers/', views.teachers, name='teachers'),
    path('rooms/', views.rooms, name='rooms'),
    path('equipment/', views.equipment, name='equipment'),
    path('transfers/', views.transfers, name='transfers'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('transfer_equipment/<int:equipment_id>/', views.transfer_equipment, name='transfer_equipment'),
    path('add_room/', views.add_room, name='add_room'),
    path('equipment_in_room/<str:room_id>/', views.equipment_in_room, name='equipment_in_room'),
    path('equipment_transfers/<int:equipment_id>/', views.equipment_transfers, name='equipment_transfers'),
    path('teacher_responsibility/<int:teacher_id>/', views.teacher_responsibility, name='teacher_responsibility'),
]

