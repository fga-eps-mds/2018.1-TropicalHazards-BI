
# JSON Output Helper Utils

## Install

```bash
$ npm install json-output
```

## Usage

```javascript
var json = require('json-output');

/**
 * Send an JSON error response in an express app
 */
app.get('/some/route', function(req, res) {
	try {
		doSomethingCool();
	} catch (err) {
		res.json(json.error(err), 500);
		return;
	}
	res.send('OK');
});
```

## API


















