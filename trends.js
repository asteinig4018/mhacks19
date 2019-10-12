const googleTrends = require('google-trends-api');
const fs = require('fs');

googleTrends.realTimeTrends({
    geo: 'US',
    category: 'all',
}, function(err, results) {
    if (err) {
       console.log(err);
    } else {
      fs.writeFileSync("google_trends_realtime.txt", results);
    }
});
