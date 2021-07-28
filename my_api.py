
from flask import Flask ,request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)
model = load('exam.joblib') 

@app.route("/Predict/<int:values>", methods=['GET'])
def main(values):
    y = model.predict(np.array(values).reshape(-1, 1))
    print(y)
    results={ 
            "Results for your values": y,
            "given value":values
    }
    return jsonify(results)

if __name__=='__main__':
    app.run(debug=True)