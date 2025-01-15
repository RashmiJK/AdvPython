from flask import Flask, request, jsonify

app = Flask(__name__)

# path parameter that appears in the URL after the endpoint
@app.route("/get_user/<int:id>")
def get_user(id):
    user_data = {
        'id': id,
        'name': 'John Doe',
        'email': 'abc@pqr.com'
    }
    # query parameter that appears in the request after ? in the URL
    extra = request.args.get("extra")
    if extra:
        user_data['extra'] = extra
    return jsonify(user_data), 200

@app.route("/create_user/", methods=["POST"])
def create_user():
    if request.method == "POST":
        data = request.get_json()
        return jsonify(data), 200
    else:
        return 400

if __name__ == "__main__":
    app.run(debug=True)