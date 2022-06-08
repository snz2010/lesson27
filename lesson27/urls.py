"""
lesson27 URL Configuration
"""
from django.contrib import admin
from django.urls import path
from ads.views import IndexView, AdSimpleView, AdDetailView, CatSimpleView, CatDetailView, AddToCat, AddToAd


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('ad/', AdSimpleView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('cat/', CatSimpleView.as_view()),
    path('cat/<int:pk>/', CatDetailView.as_view()),
    path('addc/', AddToCat.as_view()),
    path('adda/', AddToAd.as_view()),
]

# 404
handler404 = "django_404_project.views.page_not_found_view"