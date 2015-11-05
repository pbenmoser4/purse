// var bodySelection = d3.select("body");
//
// var svgSelection = bodySelection.append("svg")
//   .attr("width", 50)
//   .attr("height", 50);
//
// var circleSelection = svgSelection.append("circle")
//   .attr("cx", 25)
//   .attr("cy", 25)
//   .attr("r", 25)
//   .style("fill", "purple");

var radii = [50,40,30,20,10];

var svgContainer = d3.select("body").append("svg")
  .attr("width", 100)
  .attr("height", 100);

var circles = svgContainer.selectAll("circle")
  .data(radii)
  .enter()
  .append("circle");

var circleAttributes = circles
  .attr("cx", 50)
  .attr("cy", 50)
  .attr("r", function(d){return d; })
  .style("fill", function(d){
    var retColor;
    switch(d){
    case 50:
      retColor = "white";
      break;
    case 40:
      retColor = "black";
      break;
    case 30:
      retColor = "blue";
      break;
    case 20:
      retColor = "red";
      break;
    case 10:
      retColor = "yellow";
      break;
    default:
      retColor = "red";
      break;
    }
    return retColor;
  })
