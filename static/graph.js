
$.ajax({
    url: 'http://localhost:5000/data',
    type: 'GET',
    crossDomain: true,
    contentType: 'application/json',
    success: function(data){
        graph(data);
    }
});

function graph(data) {

    // Create the input graph
    var g = new dagreD3.graphlib.Graph()
      .setGraph({})
      .setDefaultEdgeLabel(function() { return {}; });
    
    var n = data['nodes'];
    for (var i in n) {
      g.setNode(n[i]['name'], {label: n[i]['label'], shape: n[i]['shape']});
    }

    g.nodes().forEach(function(v) {
      var node = g.node(v);
      // Round the corners of the nodes
      node.rx = node.ry = 5;
    });

    var e = data['edges'];
    for (var i in e) {
      g.setEdge(e[i]['from'], e[i]['to'], {label: e[i]['label']});
    }

    // Set up an SVG group so that we can translate the final graph.
    var svg = d3.select("svg"),
        inner = svg.append("g");

    // Set up zoom support
    var zoom = d3.zoom().on("zoom", function() {
        inner.attr("transform", d3.event.transform);
    });
    svg.call(zoom);

    // Create the renderer
    var render = new dagreD3.render();

    // Run the renderer. This is what draws the final graph.
    render(inner, g);

    // Center the graph
    var initialScale = 0.75;
    svg.call(zoom.transform, d3.zoomIdentity.translate((svg.attr("width") - g.graph().width * initialScale) / 2, 20).scale(initialScale));
    svg.attr('height', g.graph().height * initialScale + 40);

}