from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewSet, RatingViewSet, UserViewSet,LoginView

router=routers.DefaultRouter()
router.register('meals',MealViewSet)
router.register('ratings',RatingViewSet)
router.register('register',UserViewSet)

urlpatterns=[
	path('',include(router.urls)),
	path('login/', LoginView.as_view(), name='login'),



]