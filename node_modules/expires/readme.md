# node-expires

Simple Node.js expiration helper

## Install

```bash
$ npm install expires
```

## Usage

```javascript
var expires = require('expires');

// Returns some timestamp like 1341151672247
var timestamp = expires.after('2 seconds');

// Then it can be tested for expiration
expires.expired(timestamp);  // false
setTimeout(function() {
	expires.expired(timestamp);  // true
}, 2500);
```

### Supported Units

* "ms", "millisecond(s)"
* "sec(s)", "second(s)"
* "min(s)", "minute(s)"
* "hr(s)", "hour(s)"
* "day(s)"
* "wk(s)", "week(s)"
* "yr(s)", "year(s)"

### Fractions

Also completely valid are fractional values, such as the following:

```javascript
expires.after('0.5 hours');
expires.after('1/2 hours');

// A bit extreme, but still valid
expires.after('2.3/4.5 hours');
```

