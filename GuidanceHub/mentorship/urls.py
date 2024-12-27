from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('send-request/', views.send_request, name='send_request'),
    path('requests/', views.view_requests, name='mentorship_requests'),
    path('manage-request/<int:request_id>/<str:action>/', views.manage_request, name='manage_request'),
    path('connections/', views.mentorship_connections, name='mentorship_connections'),
]
