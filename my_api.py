
from flask import Flask , request
from joblib import load
import numpy as np

app = Flask(__name__)
model = load('exam.joblib') 

@app.route("/Predict/", methods=['GET'])
def main():
    y = model.predict(np.array(2).reshape(-1, 1))
    return y

if __name__=='__main__':
    app.run(debug=True)