var defaults = {

    //Boolean - If we show the scale above the chart data
    scaleOverlay : false,

    //Boolean - If we want to override with a hard coded scale
    scaleOverride : false,

    //** Required if scaleOverride is true **
    //Number - The number of steps in a hard coded scale
    scaleSteps : 1,


    //Number - The value jump in the hard coded scale
    scaleStepWidth : 30,

    // Y 轴的起始值
    scaleStartValue : null,

    // Y/X轴的颜色
    scaleLineColor : "rgba(0,0,0,.1)",

    // X,Y轴的宽度
    scaleLineWidth : 2,

    // 刻度是否显示标签, 即Y轴上是否显示文字
    scaleShowLabels : true,

    // Y轴上的刻度,即文字
    scaleLabel : "<%=value%>",

    // 字体
    scaleFontFamily : "'Arial'",

    // 文字大小
    scaleFontSize : 12,

    // 文字样式
    scaleFontStyle : "normal",

    // 文字颜色
    scaleFontColor : "#666",

    // 是否显示网格
    scaleShowGridLines : true,

    // 网格颜色
    scaleGridLineColor : "rgba(0,0,0,.05)",

    // 网格宽度
    scaleGridLineWidth : 2,

    // 是否使用贝塞尔曲线? 即:线条是否弯曲
    bezierCurve : true,

    // 是否显示点数
    pointDot : true,

    // 圆点的大小
    pointDotRadius : 5,

    // 圆点的笔触宽度, 即:圆点外层白色大小
    pointDotStrokeWidth : 0,

    // 数据集行程
    datasetStroke : true,

    // 线条的宽度, 即:数据集
    datasetStrokeWidth : 2,

    // 是否填充数据集
    datasetFill : true,

    // 是否执行动画
    animation : true,

    // 动画的时间
    animationSteps : 30,

    // 动画的特效
    animationEasing : "easeOutQuart",

    // 动画完成时的执行函数
    onAnimationComplete : null

}



console.log("马承城"+charData.lineCharData[0].produceDataDate);

var dayData = {
    labels : ["5月9日","5月10日","5月11日","5月12日","5月13日","5月14日","5月15日"],
    datasets : [
        {
            lineItemName : "test1",
            fillColor : "rgba(220,220,220,0.5)",
            strokeColor : "rgba(220,220,220,1)",
            pointColor : "rgba(220,220,220,1)",
            pointStrokeColor : "#fff",
            data : [32, 16, 25, 12, 11, 5, 20]
        }
    ]
};


var monthData = {
    labels : ["5月9日","5月10日","5月11日","5月12日","5月13日","5月14日","5月15日"],
    datasets : [
        {
            lineItemName : "test1",
            fillColor : "rgba(220,220,220,0.5)",
            strokeColor : "rgba(220,220,220,1)",
            pointColor : "rgba(220,220,220,1)",
            pointStrokeColor : "#fff",
            data : [32, 16, 25, 12, 11, 5, 20]
        }
    ]
};


window.onload = function(){
    var ctx = document.getElementById("PVChart").getContext("2d");
    var width = $("#PVChartBox").width();
    document.getElementById("PVChart").width = width;
    var chartLine = new Chart(ctx).Line(dayData, defaults);

    initEvent(chartLine, clickCall);

    var ctx = document.getElementById("RewardChart").getContext("2d");
    var width = $("#RewardChartBox").width()
    document.getElementById("RewardChart").width = width;
    var chartLine = new Chart(ctx).Line(monthData, defaults);

    initEvent(chartLine, clickCall);
}

function clickCall(evt) {
    var point = chartLine.getPointSingleAtEvent(evt);

    if ( point !== null )
        alert( point.label + ": " + point.lineItemName + " ____ " + point.value);
}

function initEvent(chart, handler) {
    var method = handler;
    var eventType = "click";
    var node = chart.chart.canvas;

    if (node.addEventListener) {
        node.addEventListener(eventType, method);
    } else if (node.attachEvent) {
        node.attachEvent("on" + eventType, method);
    } else {
        node["on" + eventType] = method;
    }
}