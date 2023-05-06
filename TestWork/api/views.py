from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Gate, LogVisit, UserOS
from .serializers import GateSerializer, UserOSSerializer


class GetUser(APIView):
    def get(self, request):
        users = UserOS.objects.all()
        serializer = UserOSSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserOSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(APIView):
    def get(self, request, pk):
        user = get_object_or_404(UserOS, pk=pk)
        serializer = UserOSSerializer(user)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        saved_user = UserOS.objects.get(login=kwargs['pk'])
        data = request.data
        serializer = UserOSSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            serializer.data})

    def delete(self, request, pk):
        user = get_object_or_404(UserOS, pk=pk)
        user.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GateAll(APIView):
    def get(self, request):
        gates = Gate.objects.all()
        serializer = GateSerializer(gates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GateApi(APIView):
    def get(self, request, pk):
        gate = get_object_or_404(Gate, pk=pk)
        serializer = GateSerializer(gate)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        saved_gate = Gate.objects.get(pk=kwargs['pk'])
        data = request.data
        serializer = GateSerializer(instance=saved_gate, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        gate = get_object_or_404(Gate, pk=pk)
        gate.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
