from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)


@app.route('/search')
def search():
    query = request.args.get('query')
    if query is None:
        return jsonify({
            'message': 'Unprocessable Entity query parameter is required',
            'status': 422
        }), 422

    headers = {k:v for k, v in request.headers.items()}
    authorization = headers.get('Authorization')
    if authorization is None:
        return jsonify({
            'message': 'Unauthorized Error authorization header is required',
            'status': 401
        }), 401

    url = 'https://api.genius.com/search'
    response = requests.get(url,
                            params={'q': query},
                            headers={'Authorization': authorization})
    return json.loads(response.content), response.status_code

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)