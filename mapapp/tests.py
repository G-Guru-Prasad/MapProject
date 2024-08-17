from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import PointData, PolygonData

class SpatialDataAPITestCase(APITestCase):

    def setUp(self):
        # Creating initial point and polygon data for testing using plain JSON
        self.point1 = PointData.objects.create(
            name="Point 1", 
            location={"type": "Point", "coordinates": [-0.09, 51.505]}
        )
        self.polygon1 = PolygonData.objects.create(
            name="Polygon 1",
            area={
                "type": "Polygon", 
                "coordinates": [[
                    [-0.09, 51.505], [-0.08, 51.505], [-0.08, 51.506], [-0.09, 51.506], [-0.09, 51.505]
                ]]
            }
        )

    def test_create_point(self):
        url = reverse('pointdata-list')
        data = {
            "name": "Point 2",
            "location": {"type": "Point", "coordinates": [-0.10, 51.504]}
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PointData.objects.count(), 2)
        self.assertEqual(PointData.objects.get(name="Point 2").location, {"type": "Point", "coordinates": [-0.10, 51.504]})

    def test_retrieve_points(self):
        url = reverse('pointdata-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Point 1")

    def test_update_point(self):
        url = reverse('pointdata-detail', kwargs={'pk': self.point1.pk})
        data = {
            "name": "Point 1 Updated",
            "location": {"type": "Point", "coordinates": [-0.11, 51.503]}
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.point1.refresh_from_db()
        self.assertEqual(self.point1.name, "Point 1 Updated")
        self.assertEqual(self.point1.location, {"type": "Point", "coordinates": [-0.11, 51.503]})

    def test_delete_point(self):
        url = reverse('pointdata-detail', kwargs={'pk': self.point1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PointData.objects.count(), 0)

    def test_create_polygon(self):
        url = reverse('polygondata-list')
        data = {
            "name": "Polygon 2",
            "area": {
                "type": "Polygon",
                "coordinates": [
                    [[-0.09, 51.505], [-0.08, 51.505], [-0.08, 51.506], [-0.09, 51.506], [-0.09, 51.505]]
                ]
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PolygonData.objects.count(), 2)

    def test_retrieve_polygons(self):
        url = reverse('polygondata-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Polygon 1")

    def test_update_polygon(self):
        url = reverse('polygondata-detail', kwargs={'pk': self.polygon1.pk})
        data = {
            "name": "Polygon 1 Updated",
            "area": {
                "type": "Polygon",
                "coordinates": [
                    [[-0.10, 51.504], [-0.09, 51.504], [-0.09, 51.505], [-0.10, 51.505], [-0.10, 51.504]]
                ]
            }
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.polygon1.refresh_from_db()
        self.assertEqual(self.polygon1.name, "Polygon 1 Updated")

    def test_delete_polygon(self):
        url = reverse('polygondata-detail', kwargs={'pk': self.polygon1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PolygonData.objects.count(), 0)
