from django.urls import path
from apps.appointment.api.views import index, store, appointment_detail

urlpatterns = [
    path('appointments', index, name='appointment.index'),
    path('appointments/<int:id>', appointment_detail, name='appointment.details'),
    path('appointments/store', store, name='appointment.store'),
]