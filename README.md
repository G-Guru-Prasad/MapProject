# **Spatial Data Platform**

This project is a spatial data platform that supports CRUD operations for managing spatial point and polygon data using plain JSON. The backend is built with Django and Django REST Framework, while the frontend is built with React.js/Vue.js and OpenLayers for map rendering.

## **Table of Contents**

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Setup and Installation](#setup-and-installation)
- [API Endpoints](#api-endpoints)
- [Frontend Integration](#frontend-integration)
- [Testing](#testing)
- [Assumptions](#assumptions)
- [Contributing](#contributing)
- [License](#license)

## **Features**

- **CRUD Operations for Points and Polygons**: Create, read, update, and delete spatial data for points and polygons.
- **Plain JSON Storage**: All spatial data is stored as JSON without relying on GIS-specific libraries.
- **Interactive Map**: Frontend interface using OpenLayers to display and interact with spatial data.

## **Technology Stack**

- **Backend**: Python, Django, Django REST Framework
- **Frontend**: HTML, CSS, Javascript, jQuery, OpenLayers
- **Database**: JSON-based storage for spatial data

## **Setup and Installation**

### **Backend Setup**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/G-Guru-Prasad/MapProject
   cd MapProject
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## **API Endpoints**

### **Point Data Endpoints**

- **Create a new point:**
  - `POST /api/points/`
  - Request Body:
    ```json
    {
      "name": "Point 1",
      "location": {
        "type": "Point",
        "coordinates": [-0.09, 51.505]
      }
    }
    ```

- **Retrieve all points:**
  - `GET /api/points/`

- **Update a point:**
  - `PUT /api/points/{id}/`
  - Request Body (same as `POST`)

- **Delete a point:**
  - `DELETE /api/points/{id}/`

### **Polygon Data Endpoints**

- **Create a new polygon:**
  - `POST /api/polygons/`
  - Request Body:
    ```json
    {
      "name": "Polygon 1",
      "area": {
        "type": "Polygon",
        "coordinates": [
          [[-0.09, 51.505], [-0.08, 51.505], [-0.08, 51.506], [-0.09, 51.506], [-0.09, 51.505]]
        ]
      }
    }
    ```

- **Retrieve all polygons:**
  - `GET /api/polygons/`

- **Update a polygon:**
  - `PUT /api/polygons/{id}/`
  - Request Body (same as `POST`)

- **Delete a polygon:**
  - `DELETE /api/polygons/{id}/`

## **Frontend Integration**

The frontend interacts with the backend through AJAX calls or `fetch` requests to the provided API endpoints. Spatial data is displayed on a map using OpenLayers.

### **Fetching Points & Polygons Example:**
```javascript
$.ajax({
    url: 'getSpatialData',
    method: 'GET',
    success: function(data) {
        data.forEach(function(point) {
            var marker = new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.fromLonLat(point.location.coordinates))
            });
            // Add marker to the map
        });
    }
});
```

## **Testing**

### **Backend Testing**

Run tests using Django’s test framework:
```bash
python manage.py test
```

Tests cover all CRUD operations for both points and polygons, verifying the correct handling of JSON data.

## **User Interface Notes**
- User will see a point with name 'Point 0' in the map when dashboard loads on the url http://127.0.0.1:8000
- When user clicks on 'Get Data' button the dashboard user will see all the points and polygons stored in the database on the map
- User can also create, update points and polygons and use 'Get Data' to see it reflected on the map

## **Assumptions**

- Spatial data is stored in plain JSON without GIS libraries.
- Frontend and backend communicate via ajax call.