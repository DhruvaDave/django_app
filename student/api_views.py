from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.contrib.auth.models import User

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, action
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle, BaseThrottle

# Third party
import random

# Loal Django Apps
from .models import Student
from .serializer import StudentSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class StudentAPIList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Generic Class View

class ContactsRateThrottle(UserRateThrottle):
    scope = 'contacts'

class StudentList(generics.ListCreateAPIView):

    throttle_classes = [UserRateThrottle]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudentDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    throttle_classes = [ContactsRateThrottle]
    throttle_scope = 'contacts'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentHighlight(generics.GenericAPIView):
    queryset = Student.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        student = self.get_object()
        return Response(student.name)



# randomly throttle 1 in every 10 requests
class RandomRateThrottle(BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 2) != 1

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    throttle_classes = [RandomRateThrottle]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, methods=['GET','POST'], renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        student = self.get_object()
        return Response(student.age)

    # def perform_create(self, serializer):
    #     print("------------>>>>>>>>>>>>")
        # serializer.save(user_id=self.request.user)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'studentapi': reverse('studentapi-list', request=request, format=format)
    })
