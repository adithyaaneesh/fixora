from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Service, Booking
from .serializers import ServiceSerializer, BookingSerializer


@api_view(['GET'])
def service_list(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def add_services(request):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['PUT'])
def update_service(request, pk):
    try:
        service = Service.objects.get(id=pk)
    except Service.DoesNotExist:
        return Response({'error': 'Service not found'}, status=404)

    serializer = ServiceSerializer(service, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_service(request, pk):
    try:
        service = Service.objects.get(id=pk)
    except Service.DoesNotExist:
        return Response({'error': 'Service not found'}, status=404)

    service.delete()
    return Response({'message': 'Service deleted successfully'}, status=204)



@api_view(['POST'])
def create_booking(request):
    data = request.data.copy()
    
    data['user'] = request.user.id  

    serializer = BookingSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Booking created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    serializer = BookingSerializer(bookings, many=True)

    return Response(serializer.data)