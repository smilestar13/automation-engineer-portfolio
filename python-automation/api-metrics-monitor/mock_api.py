from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

@app.get("/v1/resources/metrics")
def metrics():
    raw_input = request.args.get("input", "{}")
    data = json.loads(raw_input)
    resource_id = data.get("resource_id", "unknown")

    return jsonify({
        "result": {
            "data": {
                "resource_id": resource_id,
                "metric_value": round(random.uniform(10, 500), 2)
            }
        }
    })

if __name__ == "__main__":
    app.run(port=5000)
