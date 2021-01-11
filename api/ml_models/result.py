import keras
import pandas as pd
import tensorflow
from keras.models import load_model

def user_speech(text,model,csv):
        #text=input("Enter a sentence:")
        temp=pd.read_csv(csv)
        temp_list=text.split()
        for i in temp_list:
            if i in temp.columns:
                temp[i]=1
        temp_pred=model.predict(temp)
        if temp_pred>0.9:
            #print(temp_pred)
            return True
        else:
            return False
