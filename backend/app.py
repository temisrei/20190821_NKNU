from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

# 新增載入模組
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# 測試資料
# iris = [5.1, 3.5, 1.4, 0.2] # Iris Setosa
# iris = [7.0, 3.2, 4.7, 1.4] # Iris Versicolour
# iris = [6.4, 2.8, 5.6, 2.1] # Iris Virginica

# 把模型讀進來
classifier = joblib.load('classifier.joblib')

@app.route('/', methods=['GET'])
def main():
  return "<h1>Hello Flask!</h1>"

@app.route('/api', methods=['GET'])
def api():
  # ?iris=5.1,3.5,1.4,0.2 # Iris Setosa
  # ?iris=7.0,3.2,4.7,1.4 # Iris Versicolour
  # ?iris=6.4,2.8,5.6,2.1 # Iris Virginica
  irisData = request.args.get('iris')
  data = irisData.split(',')

  # 預測資料
  prediction = classifier.predict(np.array(data).reshape(1, -1))

  # 輸出類別
  types = { 0: "Iris Setosa", 1: "Iris Versicolour", 2: "Iris Virginica"}

  response = jsonify({
    "statusCode": 200,
    "status": "Prediction made",
    "result": "The type of iris plant is: " + types[prediction[0]]
  })
  return response

if __name__ == '__main__':
  app.run()