from flask import Flask, jsonify
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return "Hello, World!"
 
@app.route('/api/data')
def api_data():
    data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    return jsonify(data)
 
if __name__ == '__main__':
    app.run(debug=True)