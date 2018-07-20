var Walmart_apiKey ="ney58wdjgyubyjwpmrsfysyg";
function queryWalmart(query, resultCallback) {
  // http://api.walmartlabs.com/v1/search?query=ipod&format=json&apiKey=ney58wdjgyubyjwpmrsfysyg


  var Walmart_url = "http://api.walmartlabs.com/v1/search?query="
                  + query+"&format=json&apiKey="+Walmart_apiKey
  jQuery.get(Walmart_url, resultCallback)
}

var universalurls = null;
// Makes the element with ID 'resultPane' visible, and sets the element with ID
// 'result' to contain resultJson
function displayResult(resultJson) {
  var resultPaneDiv = document.querySelector('#resultPane')
  var resultDiv = document.querySelector('#result')

  console.log(resultJson)
  console.log(resultJson.items[0].thumbnailImage)
  var linkWalmartpic = resultJson.items[0].thumbnailImage
  var imgString = "<img src='" + linkWalmartpic + "'/>"

resultDiv.innerHTML = imgString

  // resultDiv.innerHTML = resultJson

  resultPaneDiv.style.display = "block"
}

window.addEventListener('load', () => {
  document.querySelector('#submit').addEventListener("click", () => {
    var inputBox = document.querySelector('#queryBox')
    var userInput = inputBox.value
    queryWalmart(userInput, displayResult)
  })
})
