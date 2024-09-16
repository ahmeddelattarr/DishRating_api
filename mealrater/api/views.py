
from rest_framework import request, status, viewsets
from rest_framework.views import APIView

from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer,UserSerializer

from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token,created=Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key,},status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        response = {'message': 'You cant reach this part please register'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(detail=True, methods=['post'])
    @permission_classes([IsAuthenticated])
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user

            try:
                # update
                rating = Rating.objects.get(user=user, meal=meal)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Meal Rate Updated',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)

            except Rating.DoesNotExist:
                # create
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Meal Rate Created',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_201_CREATED)

        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)



