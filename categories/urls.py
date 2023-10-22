from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloView),
    path('now_date/', views.NowDateView),
    path('goodbye/', views.ByeView),
    path('laptop/', views.LaptopListView),
    path('laptop_detail/<int:id>/', views.LaptopDetailView),

]
