function renderChart(data, labels) {
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Your State',
                    data: data[0],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                },
                {
                    label: 'Mean State',
                    data: data[1],
                    borderColor: 'rgba(192, 192, 192, 1)',
                    backgroundColor: 'rgba(192, 192, 192, 0.2)',
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        callback: function (value, index, values) {
                            return value;
                        }
                    }
                }]
            },
        }
    });
}

function getChartData() {
    //$("#loadingMessage").html('<img src="./giphy.gif" alt="" srcset="">');
    $.ajax({
        url: "http://localhost:3000/chartdata",
        success: function (result) {
            $("#loadingMessage").html("");
            var data = [];
            data.push(result.thisWeek);
            data.push(result.lastWeek);
            var labels = result.labels;
            renderChart(data, labels);
        },
        error: function (err) {
            $("#loadingMessage").html("Error");
        }
    });
}

$("#renderBtn").click(
    function () {
        getChartData();
    }
);