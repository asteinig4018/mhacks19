const googleTrends = require('google-trends-api');
const fs = require('fs');
const spawn = require("child_process").spawn;

googleTrends.realTimeTrends({
    geo: 'US',
    category: 'all',
}, function(err, results) {
    if (err) {
       console.log(err);
    } else {
      fs.writeFileSync("trends_realtime.json", results);
      var pythonProcess = spawn('python',["trends_simplifier.py","trends_realtime"]);
    }
});

googleTrends.realTimeTrends({
    geo: 'US',
    category: 's',
}, function(err, results) {
    if (err) {
       console.log(err);
    } else {
      fs.writeFileSync("trends_sports.json", results);
      var pythonProcess = spawn('python',["trends_simplifier.py","trends_sports"]);
    }
});
