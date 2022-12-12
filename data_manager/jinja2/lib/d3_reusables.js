// function addChartToDOM(chartData) {
//     var width = 10
// }

function addChartToDOM(chartData) {
    var dataset = chartData.dataset;
    var options = chartData.options;
    var dom = "#" + chartData.label;

    if (options.chartType == "scatter") { scatterChartD02(dom, dataset, options); };
    if (options.chartType == "column") { barChartD02(dom, dataset, options); };
    if (options.chartType == "line") { lineChartD01(dom, dataset, options); };

}

function lineChartD01(dom, dataset, options) {
    var width = options.width || 600;
    var height = options.height || 400;
    var marker = options.marker || {flag: false, size: 5, fillColor: 'royalblue'};
    var displayAxes = options.displayAxes || true;
    var clipPath = options.clipPath || false;
    var padding = 30;
    var x = options.x;
    var y = options.y;

    if (options.dataConverstion.flag) {
        dataset = dataSetTransformation(dataset)
    }

    var svg = d3.select(document.getElementById(dom))
        .append('svg')
        .attr('height', height)
        .attr('width', width);

    xColumn = x[0]
    yColumn = y[0]
    // Scaling Data
    var resultXMinMax = findMinMaxJson(dataset, xColumn);
    if (options.xDate ) {
        var xScale = d3.scaleTime()
            .domain([resultXMinMax['min'], resultXMinMax['max']])
            .range([padding, width - padding*2]);
    }
    else {
        var xScale = d3.scaleLinear()
            .domain([resultXMinMax['min'], resultXMinMax['max']])
            .range([padding, width - padding*2]);
    }

    var resultYMinMax = findMinMaxJson(dataset, yColumn);
    var yScale = d3.scaleLinear()
        .domain([resultYMinMax['min'], resultYMinMax['max']])
        .range([height - padding, padding]);

    var aScale = d3.scaleSqrt()
        // .domain([resultYMinMax['min'], resultYMinMax['max']])
        .domain([0, resultYMinMax['max']])
        .range([0, 10]);

    // Preparing Axes
    var xAxis = d3.axisBottom()
        .scale(xScale)
        .ticks(5);
    var yAxis = d3.axisLeft()
        .scale(yScale)
        .ticks(5);

    // Define line generator
    var line = d3.line()
                .x(function(d) { return xScale(d[xColumn]); })
                .y(function(d) { return yScale(d[yColumn]); });
    svg.append("path")
        .datum(dataset)
        .attr("class", "line")
        .attr("d", line);

    svg.selectAll("circle")
        .data(dataset)
        .enter()
        .append("circle")
        .attr("cx", function(d) {return xScale(d[xColumn]);})
        .attr("cy", function(d) {return yScale(d[yColumn]);})
        .attr("r", function(d) {
            if (options.marker.size != 'variable') {return options.marker.size;} 
            else {return aScale(d[yColumn]);}})
        .attr("fill", options.marker.fillColor)
        .on("mouseover", function(d) {
            d3.select(this)
                .attr("fill", "orange");})
        .on("mouseout", function(d) {
            d3.select(this)
                .transition()
                .duration(250)
                .attr("fill", options.marker.fillColor)})
        .append("title")
        .text(function(d) {return JSON.stringify(dataset[0], undefined, 2).replace("{", "").replace("}", "");});

    if (options.dataLabel == true) {
        svg.selectAll("text")
            .data(dataset)
            .enter()
            .append("text")
            .text(function(d) {return ( "(" + d[xColumn] + ', ' + d[yColumn] + ")");})
            .attr("x", function(d) {return xScale(d[xColumn]);})
            .attr("y", function(d) {return yScale(d[yColumn]);})
            .attr("font-family", "sans-serif")
            .attr("font-size", "14px")
            .attr("fill", "red"); }

    if (displayAxes == true) {
        svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(0," + (height-padding) + ")")
            .call(xAxis);
        svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding + ",0)")
            .call(yAxis); }

    if (clipPath == true) {
        // clip Path code is not working
        svg.append("clipPath")
            .attr("id", "chart-area")
            .append("rect")
            .attr("x", padding)
            .attr("y", padding)
            .attr("width", width - padding*3)
            .attr("height", height - padding*2);

        svg.append("g")
            .attr("id", "circles")
            .attr("clip-path", "url(#chart-area)");
        
    }

}

function dataSetTransformation(dataset) {
    dataset.forEach(function (arrayItem) {
        arrayItem.dateTime = new Date(arrayItem.year, (arrayItem.month-1));
        });

    return dataset;
}

function scatterChartD02(dom, dataset, options) {
    var width = options.width || 600;
    var height = options.height || 400;
    var marker = options.marker || {size: 5, fillColor: 'royalblue'};
    var displayAxes = options.displayAxes || true;
    var clipPath = options.clipPath || true;
    var padding = 30;
    var x = options.x;
    var y = options.y;

    var svg = d3.select(document.getElementById(dom))
        .append('svg')
        .attr('height', height)
        .attr('width', width);

    xColumn = x[0]
    yColumn = y[0]
    // Scaling Data
    var resultXMinMax = findMinMaxJson(dataset, xColumn);
    var xScale = d3.scaleLinear()
        .domain([resultXMinMax['min'], resultXMinMax['max']])
        .range([padding, width - padding*2]);

    var resultYMinMax = findMinMaxJson(dataset, yColumn);
    var yScale = d3.scaleLinear()
        .domain([resultYMinMax['min'], resultYMinMax['max']])
        .range([height - padding, padding]);

    var aScale = d3.scaleSqrt()
        // .domain([resultYMinMax['min'], resultYMinMax['max']])
        .domain([0, resultYMinMax['max']])
        .range([0, 10]);

    // Preparing Axes
    var xAxis = d3.axisBottom()
        .scale(xScale)
        .ticks(5);
    var yAxis = d3.axisLeft()
        .scale(yScale)
        .ticks(5);

    svg.selectAll("circle")
        .data(dataset)
        .enter()
        .append("circle")
        .attr("cx", function(d) {return xScale(d[xColumn]);})
        .attr("cy", function(d) {return yScale(d[yColumn]);})
        .attr("r", function(d) {
            if (options.marker.size != 'variable') {return options.marker.size;} 
            else {return aScale(d[yColumn]);}})
        .attr("fill", options.marker.fillColor)
        .on("mouseover", function(d) {
            d3.select(this)
                .attr("fill", "orange");})
        .on("mouseout", function(d) {
            d3.select(this)
                .transition()
                .duration(250)
                .attr("fill", options.marker.fillColor)})
        .append("title")
        .text(function(d) {return JSON.stringify(dataset[0], undefined, 2).replace("{", "").replace("}", "");});

    if (options.dataLabel == true) {
        svg.selectAll("text")
            .data(dataset)
            .enter()
            .append("text")
            .text(function(d) {return ( "(" + d[xColumn] + ', ' + d[yColumn] + ")");})
            .attr("x", function(d) {return xScale(d[xColumn]);})
            .attr("y", function(d) {return yScale(d[yColumn]);})
            .attr("font-family", "sans-serif")
            .attr("font-size", "14px")
            .attr("fill", "red"); }

    if (displayAxes == true) {
        svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(0," + (height-padding) + ")")
            .call(xAxis);
        svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + padding + ",0)")
            .call(yAxis); }

    if (clipPath == true) {
        // clip Path code is not working
        svg.append("clipPath")
            .attr("id", "chart-area")
            .append("rect")
            .attr("x", padding)
            .attr("y", padding)
            .attr("width", width - padding*3)
            .attr("height", height - padding*2);

        svg.append("g")
            .attr("id", "circles")
            .attr("clip-path", "url(#chart-area)");
        
    }

}


function scatterChartD01() {
	var data = [];
    var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

    function chart(selection){
        selection.each(function (data) {
            var x = d3.scale.linear().range([0, width]);
            var y = d3.scale.linear().range([height, 0]);
            // Define the axes
            var xAxis = d3.svg.axis().scale(x)
                .orient("bottom").ticks(5);
            var yAxis = d3.svg.axis().scale(y)
                .orient("left").ticks(5);

            var valueline = d3.svg.line()
                .x(function(d) { return x(d.date); })
                .y(function(d) { return y(d.close); });

            // Scale the range of the data
            x.domain(d3.extent(data, function(d) { return d.date; }));
            y.domain([0, d3.max(data, function(d) { return d.close; })]);

            d3.select(this)
                .append('svg')
                .attr('height', height)
                .attr('width', width)
                .selectAll("circle")
                .data(data)
                .enter()
                .append("circle")
                .attr("cx", function(d) { return x(d.date); })
                .attr("cy", function(d) { return y(d.close); })
                .attr("r", 5);
                // .append('path')
                // .attr("class", "line")
                // .attr("d", valueline(data))
                // .selectAll('dot')
                // .data(data)
                // .enter()
                // .append('circle')
                // .attr("r", 3.5)
                // .attr("cx", function(d) { return x(d.date); })
                // .attr("cy", function(d) { return y(d.close); })
                // .append("g")
                // .attr("class", "x axis")
                // .attr("transform", "translate(0," + height + ")")
                // .call(xAxis)
                // .append("g")
                // .attr("class", "y axis")
                // .call(yAxis);

        });
    }

    chart.height = function(value) {
        if (!arguments.length) return height;
        height = value;
        return chart;
    };

    return chart;

}


// Bar chart with options
function barChartD02(dom, dataset, options) {
    var width = options.width || 600;
    var height = options.height || 400;
    var barPadding = options.barPadding || 1;
    var fillColor = options.fillColor || 'steelblue';
    var textMargin = options.textMargin || 0.1;
    var maxDataValue = d3.max(dataset);

    if (options.chartType == 'column') {
        var barSpacing = width / dataset.length;
        var dataBarWidth = barSpacing - barPadding;
        var dataBarScale = height/maxDataValue * ( 1- textMargin);
        var dataBarMaximum = height; }

    if (options.chartType == 'bar') {
        var barSpacing =  height / dataset.length;
        var dataBarWidth = barSpacing - barPadding;
        var dataBarScale = width / maxDataValue * ( 1- textMargin);
        var dataBarMaximum = width; }

    var svg = d3.select(document.getElementById(dom))
        .append('svg')
        .attr('height', height)
        .attr('width', width);

    svg.selectAll("rect")
        .data(dataset)
        .enter()
        .append("rect")
        .attr("x", function(d, i) {return i * barSpacing;})
        .attr("y", function(d) {return (dataBarMaximum - d * dataBarScale);})
        .attr("width", dataBarWidth)
        .attr("height", function(d) {return (d * dataBarScale);})
        .attr("fill", fillColor);

    if (options.dataLabel == true) {
    svg.selectAll("text")
        .data(dataset)
        .enter()
        .append("text")
        .text(function(d) {return d;})
        .attr("x", function(d, i) {return i * barSpacing + (barSpacing-barPadding) / 2;})
        .attr("y", function(d) {return (dataBarMaximum - d * dataBarScale) - 14;})
        .attr("font-family", "sans-serif")
        .attr("font-size", "14px"); }

}


function barChart_D01(dom, data, options) {
    var margin = {top: 30, right: 20, bottom: 30, left: 50}
    var width = options.width || 800;
    var height = options.height || 200;
    var barPadding = options.barPadding || 1;
    var fillColor = options.fillColor || 'steelblue';

    var barSpacing = height / data.length;
    var barHeight = barSpacing - barPadding;
    var maxValue = d3.max(data);
    var widthScale = width / maxValue;

    var svg = d3.select(dom).append('svg')
            .attr('height', height)
            .attr('width', width)
            .selectAll('rect')
            .data(data)
            .enter()
            .append('rect')
            .attr('y', function (d, i) { return i * barSpacing })
            .attr('height', barHeight)
            .attr('x', 0)
            .attr('width', function (d) { return d*widthScale})
            .style('fill', fillColor);
    }

// basicD3 bar chart
function simpleBarChartD01(dom, dataset) {
    d3.select(document.getElementById(dom))
        .selectAll("div")
        .data(dataset)
        .enter()
        .append("div")
        .attr('class', 'bar')
        .style('height', function(d) {return d*5 + 'px'});
}

// basicD3 playground
function basicD3PlayGround(dom, dataset) {
    d3.select(document.getElementById(dom))
        .selectAll("p")
        .data(dataset)
        .enter()
        .append("p")
        .text(function(d) { return d;})
        .text(function(d) { return "I can print element " + d;})
        .style('color', function(d) {if (d>15) {return 'red';} else {return 'black';}});
}

// Using Mike Bostock's Towards Reusable Charts Pattern
function barChart_Advanced() {

    // All options that should be accessible to caller
	var data = [];
    var width = 900;
    var height = 200;
    var xAxisLabel = 'x';
    var yAxisLabel = 'y';
    var barPadding = 1;
    var fillColor = 'steelblue';

    function chart(selection){
        selection.each(function (data) {
            var barSpacing = height / data.length;
            var barHeight = barSpacing - barPadding;
            var maxValue = d3.max(data);
            var widthScale = width / maxValue;
            // var yScale = d3.scaleLinear.([height, 0]);

            d3.select(this).append('svg')
                .attr('height', height)
                .attr('width', width)
                .selectAll('rect')
                .data(data)
                .enter()
                .append('rect')
                .attr('y', function (d, i) { return i * barSpacing })
                .attr('height', barHeight)
                .attr('x', 0)
                .attr('width', function (d) { return d*widthScale})
                .style('fill', fillColor);
            
            updateWidth = function() {
            widthScale = width / maxValue;
            bars.transition().duration(1000).attr('width', function(d) { return d*widthScale});
            svg.transition().duration(1000).attr('width', width);
            };

            updateData = function() {
            svg.transition().duration(1000).attr('data', data);
            };

        });
    }

    chart.data = function(value) {
        if (!arguments.length) return data;
        data = value;
        if (typeof updateData === 'function') updateData();
        return chart;
    };

    chart.width = function(value) {
        if (!arguments.length) return margin;
        width = value;
        if (typeof updateWidth === 'function') updateWidth();
        return chart;
    };

    chart.height = function(value) {
        if (!arguments.length) return height;
        height = value;
        return chart;
    };

    chart.barPadding = function(value) {
        if (!arguments.length) return barPadding;
        barPadding = value;
        return chart;
    };

    chart.fillColor = function(value) {
        if (!arguments.length) return fillColor;
        fillColor = value;
        return chart;
    };

    return chart;
}


function barChartWithTransitions() {

    // All options that should be accessible to caller
	var data = [];
    var width = 900;
    var height = 200;
    var xAxisLabel = 'x';
    var yAxisLabel = 'y';
    var barPadding = 1;
    var fillColor = 'steelblue';
	var updateData;
	var updateWidth;

    function chart(selection){
        selection.each(function (data) {
            var barSpacing = height / data.length;
            var barHeight = barSpacing - barPadding;
            var maxValue = d3.max(data);
            var widthScale = width / maxValue;

            d3.select(this).append('svg')
                .attr('height', height)
                .attr('width', width)
                .selectAll('rect')
                .attr('data', data)
                .enter()
                .append('rect')
                .attr('y', function (d, i) { return i * barSpacing })
                .attr('height', barHeight)
                .attr('x', 0)
                .attr('width', function (d) { return d*widthScale})
                .style('fill', fillColor);
            
            updateWidth = function() {
            widthScale = width / maxValue;
            bars.transition().duration(1000).attr('width', function(d) { return d*widthScale});
            svg.transition().duration(1000).attr('width', width);
            };

            updateData = function() {
            bars.transition().duration(1000).attr('data', data);
            };

        });
    }

    chart.data = function(value) {
        if (!arguments.length) return data;
        data = value;
        if (typeof updateData === 'function') updateData();
        return chart;
    };

    chart.width = function(value) {
        if (!arguments.length) return margin;
        width = value;
        if (typeof updateWidth === 'function') updateWidth();
        return chart;
    };

    chart.height = function(value) {
        if (!arguments.length) return height;
        height = value;
        return chart;
    };

    chart.barPadding = function(value) {
        if (!arguments.length) return barPadding;
        barPadding = value;
        return chart;
    };

    chart.fillColor = function(value) {
        if (!arguments.length) return fillColor;
        fillColor = value;
        return chart;
    };

    return chart;
}


function findMinMaxJson(arr, prop) {
    let min = arr[0][prop], max = arr[0][prop];

    for (let i = 1, len=arr.length; i < len; i++) {
        let v = arr[i][prop];
        min = (v < min) ? v : min;
        max = (v > max) ? v : max;
      }

    result = {min: min, max: max}

    return result;
}