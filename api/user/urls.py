from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns =[
   # path('register/', views.registration_view, name = 'register'),
   path('login/', views.signin, name = 'signin'),
   path('logout/<int:id>/', views.signout,name= 'signout' ),
   path('profile/<int:id>/', views.view_profile,name= 'view_profile' ),
   path('', include(router.urls)),


 ]
