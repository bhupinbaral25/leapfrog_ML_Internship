
from flask import Flask ,request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)
model = load('exam.joblib') 

@app.route("/Predict/>", methods=['POST'])
def Predict():
    json_data = request.json

    y = model.predict(np.array(json_data).reshape(-1, 1))
    y = str(y)
    results={ 
            "Results for your values": y,
            "given value":json_data
    }
    return jsonify(results)

if __name__=='__main__':
    app.run(debug=True)