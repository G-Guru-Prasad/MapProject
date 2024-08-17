from rest_framework import serializers
from .models import PointData, PolygonData

class PointDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointData
        fields = '__all__'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class PolygonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolygonData
        fields = '__all__'
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
