const googleTrends = require('google-trends-api');
const fs = require('fs');

googleTrends.realTimeTrends({
    geo: 'US',
    category: 'all',
}, function(err, results) {
    if (err) {
       console.log(err);
    } else {
      fs.writeFileSync("trends_realtime_us.json", results);
    }
});

googleTrends.realTimeTrends({
    geo: 'US',
    category: 's',
}, function(err, results) {
    if (err) {
       console.log(err);
    } else {
      fs.writeFileSync("trends_sports_us.json", results);
    }
});
