from django.shortcuts import render
from rest_framework import filters
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Profile, User
from .serializers import ProfileSerializer, UsersSerializer


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile(request):
    user = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)


def fnet_home(request):
    return render(request, "users/fnet_home.html")


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_profile(request):
    my_profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllAgents(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UsersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

    def get_queryset(self):
        agent = self.request.user
        return User.objects.exclude(id=agent.id).order_by('-date_joined')
