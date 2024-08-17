from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mapapp import views as views
from rest_framework.routers import DefaultRouter
from .views import PointDataViewSet, PolygonDataViewSet

router = DefaultRouter()
router.register(r'points', PointDataViewSet)
router.register(r'polygons', PolygonDataViewSet)

urlpatterns = [
    # path('', include(router.urls)),  # Include router URLs
    path('', views.render_dashboard, name='dashboard'),
    path('api/', include(router.urls)),
    path('getSpatialData', views.getSpatialData, name='getSpatialData'),
    
]