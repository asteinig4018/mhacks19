If N objects are placed into k boxes, then there is at least one box containing at least ceil(N/k) objects 

30 = ceil(N/87)


===============================================

const twitterData; // TO DO
const weatherData; // TO DO
const stockData; // TO DO
const approvalRatingData; // TO DO
let chartData; // TO-DO

xmlhttp.get("somefile.json", result => {
	twitterData = result;
	sliderCalculation();
})


function sliderCalculation() {

if (!twitterData || !weatherData || !stockData || !approvalRatingData || !chartData) return;

let arrs = [];
let arrm = [];
let arrp = [];
let arrsTotal = 0;
let arrmTotal = 0;
let ncount = 0;
let ccount = 0;
let lcount = 0;
let time = allData[0].h;
twitterData.forEach(tweet => {
	arrs = arrs.concat(tweet.s);
	arrm = arrm.concat(tweet.m);
	arrp = arrp.concat(tweet.p);
}

arrsAvg = arrs.reduce((acc,a) => acc + a, 0) / arrs.length
arrmAvg = arrm.reduce((acc,a) => acc + a, 0) / arrm.length

lcount = arrp.filter(p => p === 'l').length;
ccount = arrp.filter(p => p === 'c').length;
ncount = arrp.filter(p => p === 'n').length;



const stateArray = Object.keys(weatherData);
let statesAverage = stateArray.reduce((acc,state) => {
	for (let i=0; i<50; i++) {
		let temptemp = weatherData[state].temperature;
		let temphigh = weatherData[state].average_monthly_high;
		let templow = weatherData[state].average_monthly_low;
		
		return acc + ((temptemp-temphigh)*(templow-temptemp))/(Math.pow(((temphigh+templow)/2),2))
	}
}, 0) / 50.0;




let stockmultiply;
let stockpricecurrent = stockData.current_price;
let stockpricechange = stockData.percent_change;
if (stockpricechange <= 0.73 && stockpricechange >= -0.73)
	stockmultiply = 0;
else
	stockmultiply = stockpricechange*0.5*0.73;





let approveAvg = approvalRatingData.approve_avg;
let currentApproval = approvalRatingData.approve;

function equation(sentiment, stockmultiply, pollcurrent, pollaverage, avgtemp, lvalue, cvalue, ltweets, ctweet, time, const1 = 70, const2 = 60, const3 = 50, const4 = 45, const5 = 25, slideInput = True) {
	return const1*(sentiment) + const2*(stockmultiply)+const3*((pollcurrent-pollaverage)/(pollaverage))+const4*avgtemp + const5/2*lvalue*ltweets+ const5/2*cvalue+ctweet+const5

	//let chartData; // TO-DO
	
}}