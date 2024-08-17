from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import PointData, PolygonData
from .serializers import PointDataSerializer, PolygonDataSerializer

# Create your views here.

def render_dashboard(request):
    context = dict()
    context['username'] = 'Guru'
    return render(request, 'dashboard.html', context)

def getSpatialData(request):
    
    # point_data = [
    #                 { "lon": 75.78543901946227, "lat": 17.912671869722075, "name": "Point 1" },
    #                 { "lon": 78.16197854523557, "lat": 23.583932873898675, "name": "Point 2" },
    #                 { "lon": 81.14796820214906, "lat": 18.51946379741335, "name": "Point 3" },
    #             ]

    # polygon_data = [
    #                 {
    #                     "coordinates": [
    #                     [76.3928477850369, 11.620174470250674],
    #                     [80.363832964832, 13.378081516373584],
    #                     [79.66173619768631, 10.266382244360443],
    #                     [77.39905134150314, 7.943969478884696],
    #                     [76.28616572528608, 11.826959063043574],
    #                     ],
    #                 },
    #                 {
    #                     "coordinates": [
    #                     [76.1738125190077, 12.966102719718734],
    #                     [80.26276164166131, 14.050584684798721],
    #                     [77.00148003256896, 16.792687373249777],
    #                     [76.22872658133883, 13.002388835880254],
    #                     ],
    #                 },
    #             ]
    
    try:
        points = list(PointData.objects.values('name', 'location'))
    except Exception as e:
        print('Unable to fetch points data from the database')
        points = []

    try:
        polygons = list(PolygonData.objects.values('name', 'area'))
    except Exception as e:
        print('Unable to fetch polygon data from the database')
        polygons = []
    
    data = {
        'status': 'success',
        'message': 'Data received successfully!',
        'data': {
            'points_data': points,
            'polygon_data': polygons,
        }
    }
    
    return JsonResponse(data)

# For CRUD operations
class PointDataViewSet(viewsets.ModelViewSet):
    queryset = PointData.objects.all()
    serializer_class = PointDataSerializer

class PolygonDataViewSet(viewsets.ModelViewSet):
    queryset = PolygonData.objects.all()
    serializer_class = PolygonDataSerializer