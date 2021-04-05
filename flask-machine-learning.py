from sklearn.externals import joblib
from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)


@app.route('/music-prediction/<int:age>/<int:gender>',methods=['GET'])
def get_prediction(age,gender):
    model=pickle.load(open('model.sav','rb'))
    prediction = model.predict([[age,gender]])
    return jsonify({'results':prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)