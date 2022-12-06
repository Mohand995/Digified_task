import pandas as pd
import numpy as np
import pickle
import json
import time
import os
import warnings
warnings.filterwarnings("ignore") 
import tensorflow as tf
os.environ['CUDA_VISIBLE_DEVICES']='-1'
from keras.models import load_model
###############################Load_Deep_Learning_Model################################
DL_Model = load_model("./models/DL_classifier.h5")

#########################Encode_Labels_to_Name########################################
Encode_Labels={0:"Fake Name",1:"Correct Name"}

##########################Load_RandomForrest_Model###################################
with open('./models/Random_forrest_pipeline_.pkl', 'rb') as f:
    RF_Model = pickle.load(f)
##########################Load_TFIDF_Vectorizer#####################################
with open('./models/Vectorizer.pkl', 'rb') as k:
    Vectorizer = pickle.load(k)
###########################Predict_by_RF#####################################
def Test_Model_Random_Forrest(text):
  prob_list=RF_Model.predict_proba(np.array([text]))[0]
  print(prob_list)
  prob=prob_list[np.argmax(prob_list)]
  print(type(prob))
  start_time=time.time()
  prediction=RF_Model.predict(np.array([text]))
  end_time=time.time()
  result="Model classify it as  {}".format(Encode_Labels[prediction[0]])
  inference_time="time is {} ms".format(end_time-start_time)
  final_result={"Name":text,"Prediction":result,"probability":prob,"Inference_time":inference_time }
  return json.dumps(final_result,ensure_ascii=False)
##########################Predict_by_DL##########################################
def Test_DL_model(text):
    point=np.array([text])
    start_time=time.time()
    x=Vectorizer.transform(point).toarray()
    prob=DL_Model.predict(x).astype(np.float64)[0][0]
    end_time=time.time()
  
    if prob>0.5:
      result="model classify it as Correct"
    else:
      result="model classify it as Fake"
    inference_time="time is {} ms".format(end_time-start_time)
    final_result={"Name":text,"Prediction":result,"probability":prob,"Inference_time":inference_time }
    return json.dumps(final_result,ensure_ascii=False)
    
#####################################################################
if __name__=="__main__":
    
    text="ياسر محمد محمود"
    #predictions = Test_Model_Random_Forrest(text)
    predictions = Test_DL_model(text)
    print(predictions)