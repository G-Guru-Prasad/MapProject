const pointData = [
  // { lon: 75.78543901946227, lat: 17.912671869722075, name: "Point 1" },
  // { lon: 78.16197854523557, lat: 23.583932873898675, name: "Point 2" },
  {
    name: "Point 0",
    location: {
      type: "Point",
      coordinates: [81.14796820214906, 18.51946379741335],
    },
  },
];

// Initializing the map
const map = new ol.Map({
  target: "map",
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM(),
    }),
  ],
  view: new ol.View({
    center: ol.proj.fromLonLat([77.9195654503556, 19.213164924083117]),
    zoom: 5,
  }),
});

// Handling Map Click Events
map.on("singleclick", function (evt) {
  const features = map.getFeaturesAtPixel(evt.pixel);
  const info = document.getElementById("feature-info");
  info.innerHTML = "";

  if (features) {
    if (features.length > 0) {
      features.forEach((feature) => {
        const name = feature.get("name") || "Polygon";
        showFeatureInfo(name, feature.getGeometry().getCoordinates());
      });
    }
  } else {
    showFeatureInfo("Map Clicked", evt.coordinate);
  }
});

function showFeatureInfo(title, coordinate) {
  const featureInfo = document.getElementById("feature-info");

  const pixel = map.getPixelFromCoordinate(coordinate);
  console.log("pixel", pixel);

  featureInfo.style.left = pixel[0] + "px";
  featureInfo.style.top = pixel[1] + 50 + "px";
  featureInfo.style.display = "block";
  featureInfo.innerHTML += `
        <div class="card">
            <h4 class='close-btn' onclick='closePopup();'>x</h4>
            <h3>${title}</h3>
        </div>
    `;
}

var closePopup = function () {
  document.getElementById("feature-info").style.display = "none";
};

// to fetch points and polygons data from database
function getSpatialData() {
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (
        !/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) &&
        !this.crossDomain
      ) {
        xhr.setRequestHeader("X-CSRFToken", csrf_token);
      }
    },
  });

  $.ajax({
    url: "getSpatialData",
    type: "GET",
    data: {},
    dataType: "json",
    contentType: "application/json",

    success: function (response) {
      var data = response["data"];
      addPoints(data["points_data"]);
      addPolygon(data["polygon_data"]);
    },

    error: function (xhr, status, error) {
      console.error("AJAX Error:", error);
    },
  });
}

function addPoints(pointsData) {
  console.log("pointsData", pointsData);
  const pointFeatures = pointsData.map((point) => {
    const feature = new ol.Feature({
      geometry: new ol.geom.Point(
        ol.proj.fromLonLat(point.location.coordinates)
      ),
      name: point.name,
    });

    feature.setStyle(
      new ol.style.Style({
        image: new ol.style.Icon({
          anchor: [0.5, 1],
          // src: 'https://openlayers.org/en/latest/examples/data/icon.png'
          src: "static/location_pin.png",
          scale: 0.07,
        }),
      })
    );

    return feature;
  });

  const pointLayer = new ol.layer.Vector({
    source: new ol.source.Vector({
      features: pointFeatures,
    }),
  });

  map.addLayer(pointLayer);
}

function addPolygon(polygonData) {
  const polygonFeatures = polygonData.map((polygon) => {
    const feature = new ol.Feature({
      geometry: new ol.geom.Polygon([
        polygon.area.coordinates.map((coord) => ol.proj.fromLonLat(coord)),
      ]),
      name: polygon.name,
    });

    feature.setStyle(
      new ol.style.Style({
        fill: new ol.style.Fill({ color: "#b2f0fe" }),
        stroke: new ol.style.Stroke({ color: "#6a6a00;", width: 2 }),
      })
    );

    return feature;
  });

  const polygonLayer = new ol.layer.Vector({
    source: new ol.source.Vector({
      features: polygonFeatures,
    }),
  });

  map.addLayer(polygonLayer);
}

addPoints(pointData);
