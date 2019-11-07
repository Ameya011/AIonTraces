$(document).ready( function () {
  var items =  $(".timeline li");;
  
  function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
      rect.top >= -500 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) + 500 &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth) + 200
    );
  }

  function callbackFunc() {
 items = $(".timeline li");
   items.each(function(i) {
	var item = items[i];
      if (isElementInViewport(item)) {
	
        $(item).addClass("in-view");
	$(item).find("div").append($(item).data("tokenList"));
       } else {
        $(item).removeClass("in-view");
	$(item).find("div").remove("tokenlist");
}
  });
  }

function timeConverter(UNIX_timestamp){
  var a = new Date(UNIX_timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var min = a.getMinutes();
  var sec = a.getSeconds();
  var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
  return time;
}


$.getJSON( "data.json", function( data ) {
  $.each( data, function( key, val ) {
	var tokens = val.tokens;
var tokenList = $("<ul class=\"tokenlist\"/>");
     tokens.forEach(function (item) {
	tokenList.append($("<li class=\"token\">"+ item+"</li>"));
     });
//console.log("tokenlist length", tokenList.length);
	var chunkItem = $("<li><div><time>" + val.tracename + "</time><p class=\"chunk\">" + timeConverter(val.chunk) + " (" + val.chunk + ")</p><p class=\"tracepath\">" + val.tracepath + "</p></div></li>" );
	//chunkItem.find("div").append(tokenList);
console.log(tokenList);
chunkItem.data("tokenList", tokenList)
    $( ".timeline ul").append(chunkItem);
  });

callbackFunc();
});




$( window ).resize(callbackFunc);
$(window).scroll(callbackFunc);
});
