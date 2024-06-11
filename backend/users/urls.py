from django.urls import path

from users import views


urlpatterns = [
    path('generate/id/', views.GenerateIDView.as_view(), name='generate-id'),

    path('patients/create/<str:patient_id>/', views.CreatePatientView.as_view(), name='create-patient'),
    path('patients/detail/<int:pk>/', views.RetrievePatientView.as_view(), name='patient-detail'),
    path('patients/list/', views.ListPatientView.as_view(), name='patients-list'),

    path('doctors/create/<str:doctor_id>/', views.CreateDoctorView.as_view(), name='create-doctor'),
    path('doctors/detail/<int:pk>/', views.RetrieveDoctorView.as_view(), name='doctor-detail'),
    path('doctors/list/', views.ListDoctorView.as_view(), name='doctors-list')
]
