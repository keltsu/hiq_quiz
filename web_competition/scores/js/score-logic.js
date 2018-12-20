
var stepX = hscore.split("''");
var stepY = stepX.toString();
stepY.split("__");

var parsittu = stepY.split("__");
parsittu.shift(); //remove first empty item

var step2 = parsittu.toString();
var items = step2.split(",");

//get all users & score, format numeric values and group as objects
var obj = [];
for (x=0; x<items.length; x++) {
  if (x % 2 == 0) {
    // console.log(debug[x] +' '+ debug[x+1]);
    obj.push({username: items[x], score: parseFloat(items[x+1])})
  }
}

obj.sort(function(a, b) {
  return a.score - b.score;
});

function renderResults(dom_id) {
  // document.getElementById(dom_id).innerHTML = "<h2>jeps</h2>";
// loop items into insertable html, remove first obsolete ' character
  var html_string = '';
  for (x=0; x< obj.length; x++) {
    html_string += '<div class="item">'+
                      '<div class="name">'+ obj[x].username.substring(1) + '</div>' +
                      '<div class="score">'+ obj[x].score + '</div>' +
                    '</div>'
  }
  document.getElementById(dom_id).innerHTML = html_string;
}
renderResults("dyna");
