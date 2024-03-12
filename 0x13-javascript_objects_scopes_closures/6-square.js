#!/usr/bin/node

const supSquare = require('./5-square');

class Square extends supSquare {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let d = 0; d < this.width; d++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
