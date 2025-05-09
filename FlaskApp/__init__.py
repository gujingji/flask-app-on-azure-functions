from flask import Flask, request, jsonify
import qrcode
import base64
from io import BytesIO

# Always use relative import for custom module
from .package.module import MODULE_VALUE

app = Flask(__name__)

@app.route("/")
def index():
    return (
        "Try /hello/Chris for parameterized Flask route.\n"
        "Try /module for module import guidance"
    )

@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    return f"hello {name}"

@app.route("/module")
def module():
    return f"loaded from FlaskApp.package.module = {MODULE_VALUE}"



@app.route("/qrcode_post", methods=["POST"])
def qrcode_post():
    data = request.json
    employee_id = data.get("EmployeeID")

    if not employee_id:
        return jsonify({"error": "Missing EmployeeID"}), 400


    qr = qrcode.make(employee_id)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    return jsonify({"QRCodeBase64": img_base64})


@app.route("/qrcode_get/<employee_id>", methods=["GET"])
def qrcode_get(employee_id: str):
   
    if not employee_id:
        return jsonify({"error": "Missing EmployeeID"}), 

    qr = qrcode.make(employee_id)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    return img_base64

if __name__ == "__main__":
    app.run()