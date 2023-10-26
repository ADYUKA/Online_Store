from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('now_date/', views.now_date_view),
    path('goodbye/', views.bye_view),
    path('laptop/', views.laptop_list_view),
    path('laptop_detail/<int:id>/', views.laptop_detail_view),

]
