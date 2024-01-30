from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

routers = DefaultRouter()
routers.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
routers.register('profile', views.UserProfileViewSet)
routers.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(routers.urls))
]