from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer


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