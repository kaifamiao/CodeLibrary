(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
/**
 * entry - main.js
 */
var mA = require('./moduleA/moduleA.js');
var mB = require('./moduleB/moduleB.js');
console.log(mA + " <-> " + mB);
},{"./moduleA/moduleA.js":2,"./moduleB/moduleB.js":4}],2:[function(require,module,exports){
/**
 * moduleA - moduleA.js
 */
var mAA = require('./moduleAA/moduleAA.js');
module.exports = "moduleA" + " <- " + mAA;
},{"./moduleAA/moduleAA.js":3}],3:[function(require,module,exports){
/**
 * moduleA\moduleAA - moduleAA.js
 */
module.exports = "moduleAA";
},{}],4:[function(require,module,exports){
var mBB = require('./moduleBB/moduleBB.js');
module.exports = "moduleB" + " <- " + mBB;
},{"./moduleBB/moduleBB.js":5}],5:[function(require,module,exports){
module.exports = "moduleBB";
},{}]},{},[1]);
