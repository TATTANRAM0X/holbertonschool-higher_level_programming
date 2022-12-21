#!/usr/bin/node
const Sq = require('./5-square.js');

module.exports = class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
