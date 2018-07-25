// Runs the given query and fetches the first result.
// Args:
// - query: the string to use for the query.
// - resultCallback: a function to call when the results are available.
//                   Should take a single argument: the JSON returned from
//                   giphy's API
function queryGiphy(query, resultCallback) {
  var giphy_url = "http://api.giphy.com/v1/gifs/search?"
                  + "api_key=" + giphy_api_key
                  + "&q=" + query
                  + "&limit=" + 1
  jQuery.get(giphy_url, resultCallback)
}

var currentGifUrl = null;

// Makes the element with ID 'resultPane' visible, and sets the element with ID
// 'result' to contain resultJson
function displayResult(resultJson) {
  var resultPaneDiv = document.querySelector('#resultPane')
  var resultDiv = document.querySelector('#result')

  // TODO: instead of just putting the resultJson in the div, parse it and pull
  // out the image url, and insert an image tag instead.
  console.log(resultJson)
  console.log(resultJson.data)
  console.log(resultJson.data[0])
  console.log(resultJson.data[0].images)
  console.log(resultJson.data[0].images.fixed_height_downsampled)
  console.log(resultJson.data[0].images.fixed_height_downsampled.url)
  currentGifUrl = resultJson.data[0].images.fixed_height_downsampled.url;

  var imgString = "<img src='" +
                  resultJson.data[0].images.fixed_height_downsampled.url +
                  "'/>"
  resultDiv.innerHTML = imgString

  // This line makes the container for the result div and the "add to favorites"
  // button visible.
  resultPaneDiv.style.display = "block"
}
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
// function that posts
// function addSearchToLists(listUrl, doneCallBack) {
//   jQuery.post("/checklist",
// }
function submitClick() {
  var inputBox = document.querySelector('#queryBox')
  var userInput = inputBox.value
  document.getElementById("itemName").innerHTML = capitalizeFirstLetter(userInput)
  document.getElementById("pottery").src ="https://www.potterybarn.com/search/results.html?words=" + (userInput) + "&cm_sp=HeaderLinks-_-OnsiteSearch-_-MainSite&cm_type=OnsiteSearch"
  document.getElementById("dormify").src ="https://www.dormify.com/search?q=" + (userInput)
  document.getElementById("dormco").src ="https://www.dormco.com/SearchResults.asp?Search=" + (userInput) + "&Submit="
  document.getElementById("walmart").src ="https://www.walmart.com/search/?query="+ (userInput) +"&cat_id=0"
  queryGiphy(userInput, displayResult)
}
  // class DatabaseEntry(ndb.Model):
  // 	value = ndb.StringProperty()
  // 	type = ndb.StringProperty()
window.addEventListener('load', () => {
  document.querySelector('#submit').addEventListener("click", submitClick)
  // document.querySelector("#needIt").addEventListener("click", () => {
  //   addSearchToLists()
});
var map, infoWindow;
function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 41.887327, lng: -87.652370},
          zoom: 12
        });
        infoWindow = new google.maps.InfoWindow;
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };

            infoWindow.setPosition(pos);
            infoWindow.setContent('Your Location.');
            infoWindow.open(map);
            map.setCenter(pos);

            var service = new google.maps.places.PlacesService(map);
            service.nearbySearch({
              location: pos,
              radius: 2000,
              type: ['retail stores near me']
            }, callback);

          }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        } else {
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
        }
      }

      function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
      }

      // https://developers.google.com/maps/documentation/javascript/examples/place-search
      function callback(results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
          for (var i = 0; i < results.length; i++) {
            createMarker(results[i]);
          }
        }
      }

      function createMarker(place) {
        var placeLoc = place.geometry.location;
        var marker = new google.maps.Marker({
          map: map,
          position: place.geometry.location
        });

        google.maps.event.addListener(marker, 'click', function() {
          infowindow.setContent(place.name);
          infowindow.open(map, this);
        });
      }
