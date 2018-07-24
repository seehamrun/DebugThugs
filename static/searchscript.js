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
function submitClick() {
  var inputBox = document.querySelector('#queryBox')
  var userInput = inputBox.value
  document.getElementById("itemName").innerHTML = " " + (userInput) + " "
  document.getElementById("pottery").src ="https://www.potterybarn.com/search/results.html?words=" + (userInput) + "&cm_sp=HeaderLinks-_-OnsiteSearch-_-MainSite&cm_type=OnsiteSearch"
  document.getElementById("dormify").src ="https://www.dormify.com/search?q=" + (userInput)
  document.getElementById("dormco").src ="https://www.dormco.com/SearchResults.asp?Search=" + (userInput) + "&Submit="
  document.getElementById("walmart").src ="https://www.walmart.com/search/?query="+ (userInput) +"&cat_id=0"
  queryGiphy(userInput, displayResult)
}
window.addEventListener('load', () => {
  document.querySelector('#submit').addEventListener("click", submitClick)

});
