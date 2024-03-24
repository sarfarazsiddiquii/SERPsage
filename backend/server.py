from flask import Flask, jsonify

# app instance
app = Flask(__name__)

# /api/home
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Like this video if this helped!",
    })


if __name__ == "__main__":
    app.run(debug=True)