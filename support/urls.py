from django.urls import path
from .views import submit_ticket

urlpatterns = [
    path('submit/', submit_ticket, name='submit_ticket'),
]
