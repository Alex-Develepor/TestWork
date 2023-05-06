from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from .models import Gate, LogVisit, UserOS
from .serializers import GateSerializer, UserOSSerializer, LogVisitSerializer

logging.basicConfig(level=logging.INFO, filename="logfile.log",
                    format="%(asctime)s %(levelname)s %(message)s")



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


class LogVisitApi(APIView):
    def get(self, request):
        logvisit = LogVisit.objects.all()
        serializer = LogVisitSerializer(logvisit, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LogVisitSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = UserOS.objects.get(login=str(serializer.validated_data['user']))
            except UserOS.DoesNotExist:
                logging.info(f'Пользователь {serializer.validated_data["user"]} не найден')
                return Response({f'Пользователь {serializer.validated_data["user"]} не найден'})
            try:
                Gate.objects.get(num_chekpoint=str(serializer.validated_data['num_checkpoint']))
            except Gate.DoesNotExist:
                logging.info(f'КПП {serializer.data["num_checkpoint"]} не найдено')
                return Response({f'КПП {serializer.data["num_checkpoint"]} не найдено'})
            serializer_user = UserOSSerializer(user)
            if serializer.validated_data['permit_id'] == serializer_user.data['permit']:
                if serializer_user.data['status'] is True:
                    user.status = False
                    serializer.validated_data['status'] = False
                    logging.info(f'Пользователь {serializer.validated_data["user"]} вышел')
                else:
                    user.status = True
                    serializer.validated_data['status'] = True
                    logging.info(f'Пользователь {serializer.validated_data["user"]} зашел')
                user.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logging.info('Некорректный пропуск')
                return Response({'Некорректный пропуск'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
