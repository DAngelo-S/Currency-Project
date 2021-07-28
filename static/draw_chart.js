// Load the Visualization API and the corechart package
google.charts.load('current', {'packages':['corechart']});

// Set a callback for when the API is loaded
google.charts.setOnLoadCallback(drawChart);

// This is the callback function which actually draws the chart
function drawChart(){

	dataTable = new google.visualization.DataTable(data);
	options.hAxis.ticks = dataTable.getDistinctValues(0);

	view = new google.visualization.DataView(dataTable);
	
	options['series'] = Series();
    options['selectionMode'] = 'multiple';
    options['tooltip'] = {
        'isHtml': true,
        trigger: 'both'
    }

	chart = new google.visualization.LineChart(document.getElementById(containerId));

	chart.draw(view, options);

	//google.visualization.drawChart({
	//	"containerId": containerId,
	//	"chartType": chartType,
	//	"options": options,
	//	"dataTable": data,
	//	"view": view
	//})
}

function Series() {
    var arr = view.getViewColumns();
    s = {}
    for (let i = 1; i < arr.length; i++) {
        var country = dataTable.getColumnId(arr[i]);
        if (america.includes(country))
            s[i-1] = { 'color': 'green'};
        else if (asia.includes(country) && europe.includes(country))
            s[i-1] = { 'color': 'purple'};
        else if (asia.includes(country) && africa.includes(country))
            s[i-1] = { 'color': 'orange'};
        else if (asia.includes(country))
            s[i-1] = { 'color': 'red'};
        else if (europe.includes(country))
            s[i-1] = { 'color': 'blue'};
        else if (oceania.includes(country))
            s[i-1] = { 'color': 'pink'};
        else if (africa.includes(country))
            s[i-1] = { 'color': 'yellow'};
        else if (country == '0') {
            s[i-1] = { 
                'color': 'grey',
                'enableInteractivity': false,
                'lineWidth': 0.1
            };
        } else
            s[i-1] = { 'color': 'black'};
    }

    return s;
}

function reload_chart(opt) {
    if (opt == 's')
        options['series'] = Series()

    if (!isNaN(opt)) {
        var arr = chart.getSelection()
        for(let i = 0; i < arr.length; i++)
            arr[i].row = arr[i].row + opt
        arr = arr.filter(function(value) {return value.row < selected && value.row >= 0})
    }
    
    chart.draw(view, options)
    
    if (!isNaN(opt))
        chart.setSelection(arr)
}