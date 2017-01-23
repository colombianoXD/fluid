var fs = require('fs');
var tri = [];

fs.readFileSync(process.argv[2]).toString().split('\n').
  forEach(function(line) {
    if (line !== '') {
      var parts = line.split(' ');
      var temp = [];
      parts.forEach(function(item) {
      temp.push(parseInt(item));
        });
      tri.push(temp);
    }
});

for (var i = tri.length - 1; i > 0; i--) {
  for (var j = tri[i].length - 1; j > 0; j--) {

    var value = Math.max(tri[i][j], tri[i][j - 1]) + tri[i - 1][j - 1];
    tri[i - 1][j - 1] = value;
  }
}

console.log(value);
