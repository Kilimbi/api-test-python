## Simple Python3 API with Redis

Python3 script that runs a RESTful app and listens to HTTP (PUT / GET) requests on port 5000.

Redis is used for data persistence.

#### Usage

There are 2 endpoints:
- `/key`
- `/key/<KEY>`

Supported methods are:
- `PUT /key` Creates a redis key with the key/<KEY> value coming from the HTTP request body. Also returns a status code of `200` if successful and `500` in case of an error.

- `GET /key/<KEY>` Retrieves the key name and value in JSON format with a status code of `200` if successful and `404` with no data if the value is not found.

#### Examples

`curl -XPUT ​ http://HOST/key ​ -H 'content-type: application/json' -d '{"key": "key1", "value":"value1"}'`

The call above should add an item into Redis similar to `redis-cli set key1 value1`.

{"key": "key1", "value":"value1"}
 