from sklearn.externals import joblib
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/music-prediction/<int:age>/<int:gender>',methods=['GET'])
@cross_origin()
def get_prediction(age,gender):
    model=pickle.load(open('model.sav','rb'))
    prediction = model.predict([[age,gender]])
    return jsonify({'output':prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0')