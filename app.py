from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    try:
        # Get the JSON data from the request body
        data = request.get_json()

        # Check if the request contains JSON data
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400

        # Echo the JSON data back to the caller
        return jsonify(data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
