from flask import Flask, request, jsonify
import io, json, time

app = Flask(__name__)


@app.route('/')
def hello():
	with io.open('clientdata/json.txt', 'r', encoding='utf-8') as f:
		return f.read()

@app.route('/api/client/submit', methods=['POST']) 
def foo():
    if not request.json:
        abort(400)
    with io.open('clientdata/json.txt', 'a', encoding='utf-8') as f:
        f.write("%s\n" % json.dumps(request.get_json(), ensure_ascii=False))
    return jsonify(request.get_json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)