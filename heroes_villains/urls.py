from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.heroes_villains_list),
    path('<int:pk>/', views.hero_villain_detail),
]