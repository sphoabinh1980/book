const path = require('path'), fs = require('fs');
const ROOT = path.join(__dirname, '..');
const CH = [1, 2, 3, 4, 5].filter((i) => fs.existsSync(path.join(ROOT, 'content', `ch${i}.js`))).map((i) => require(path.join(ROOT, 'content', `ch${i}.js`)));
console.log(JSON.stringify(require(path.join(ROOT, 'content', 'front.js')).targets({ CH })));
