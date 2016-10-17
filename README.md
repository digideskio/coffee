# coffee [![CircleCI](https://circleci.com/gh/webkom/coffee.svg?style=svg&circle-token=8f404a282940246354cff9f1ed724703769f2fba)](https://circleci.com/gh/webkom/coffee)

An API to the Moccamaster at the Abakus office.

## Setup dev environment
```bash
git clone git@github.com:webkom/coffee.git
cd coffee
virualenv venv -p python3
source venv/bin/activate
pip install -r requirements/base.txt
npm install
```

## Run the server
```bash
npm run build
python -m coffee.server
```

## Use the API
### GET [kaffe.abakus.no/api/status](http://kaffe.abakus.no/api/status)
Return data of last time coffee was turned on.
##### Example response
HTTP/1.1 200 OK   
Content-Type: application/json

```json
{
  "coffee": {
    "status": true,
    "last_start": "2012-12-12 12:12",
    "time_since": {
	  "hours": 0,
	  "minutes": 0
	}
  }
}
```

### GET [kaffe.abakus.no/api/stats](http://kaffe.abakus.no/api/stats)
Return stats of usage of the coffee machine. 
##### Example response
HTTP/1.1 200 OK   
Content-Type: application/json

```json
{
  "stats": {
    "2012-12-12": 3,
    "2012-12-13": 1,
    "2012-12-14": 7
  }
}
```
--------
MIT © webkom, Abakus Linjeforening
