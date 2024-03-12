#!/usr/bin/node
const dict = require('./101-data').dict;
const dKeys = Object.keys(dict);
const values = Object.values(dict);
let matched;
const result = {};
// loop over the values
for (let c = 0; c < values.length; c++) {
  result[JSON.stringify(values[c])] = [];
  matched = dKeys.filter(key => dict[key] === values[c]);
  matched.forEach(item => result[JSON.stringify(values[c])].push(item));
}
console.log(result)
