from utility import  *
import json
from flask import Flask,jsonify,request



app=Flask(__name__)

@app.route("/Guess_Name_RF",methods=['POST'])
def predict_rf():
    data=request.json
    try:
        sample=data['text']
    except KeyError:
        return  jsonify({'error':'NO text sent'})
    
    result=Test_Model_Random_Forrest(sample)
    return  result


@app.route("/Guess_Name_DL",methods=['POST'])
def predict_dl():
    data=request.json
    try:
        sample=data['text']
    except KeyError:
        return  jsonify({'error':'NO text sent'})
    result=Test_DL_model(sample)
    return  result

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
