from django.urls import path
from . import views

urlpatterns = [
    path('now_date/', views.now_date_view),
    path('laptop/', views.laptop_list_view),
    path('laptop_detail/<int:id>/', views.laptop_detail_view),
    path('laptop/create/', views.laptop_create_view),

]
