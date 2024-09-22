from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.appointment.api.serializers import AppointmentSerializer
from apps.appointment.models import Appointment

@api_view(['GET'])
def index(request):
    serializer = AppointmentSerializer(Appointment.objects.all(), many=True)
    return Response({'data': serializer.data})

@api_view(['POST'])
def store(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def appointment_detail(request, id):
    try:
        appointment = Appointment.objects.get(id=id)
    except Appointment.DoesNotExist:
        return Response({'error': 'Not found any data'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({'data': AppointmentSerializer(appointment).data})

    if request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        appointment.delete()
        return Response({'message': 'Appointment delete'},status=status.HTTP_204_NO_CONTENT)