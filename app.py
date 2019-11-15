from flask import Flask, request, jsonify
import requests
import json
from src.Validate import Validator
from werkzeug.exceptions import Unauthorized

app = Flask(__name__)


@app.route('/search')
def search():
    try:
        Validator(request).validate()
        query = request.args.get('query')
        headers = {k:v for k, v in self.__request.headers.items()}
        authorization = headers.get('Authorization')
        url = 'https://api.genius.com/search'
        response = requests.get(url,
                            params={'q': query},
                            headers={'Authorization': authorization})
        return json.loads(response.content), response.status_code
    except ValueError as ex:
        return jsonify({"message": ex.args[0][0]}), 422
    except Unauthorized as ex:
        return jsonify({"message": ex.description}), 401
    except Exception:
        return jsonify({"message": 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)