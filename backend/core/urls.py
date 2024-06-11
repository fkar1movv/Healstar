from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register('departments', views.DepartmentView)
router.register('hospitals', views.HospitalView)

urlpatterns = [
    path('', include(router.urls)),
]

