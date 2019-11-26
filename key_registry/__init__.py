from flask import Flask
from flask import request
from flask import json
from flask_restful import abort
import redis

# Create Flask app
app = Flask(__name__)

# Connect to Redis
db = redis.Redis('redis')

# Set TTL to one year
ttl = 31104000


@app.route('/key', methods=['PUT'])
def put_key():
    if request.method == 'PUT' and request.is_json:
        content = request.get_json()
        key_id = content['key']
        db.delete(key_id)
        db.hmset(key_id, content)
        return "JSON stored at: " + str(key_id) + "\n" + str(content), 200
    else:
        abort(500)


@app.route('/key/key<value>', methods=['GET'])
def get_key(value):
    if request.method == 'GET':
        result = db.get(value)
        return json.dumps(result), 200
    else:
        abort(404)


if __name__ == "__main__":
    app.run()
