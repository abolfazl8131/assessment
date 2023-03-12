from django.urls import path
from .apis import ProfileApi, RegisterApi, UserUpdateAPI , CreateSuperUserAPI


urlpatterns = [
    path('register/', RegisterApi.as_view(),name="register"),
    path('profile/', ProfileApi.as_view(),name="profile"),
    path('update/' , UserUpdateAPI.as_view()),
    path('create-superuser/' , CreateSuperUserAPI.as_view())
]
