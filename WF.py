
import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('HousePredictionFile', 'rb'))

def diabetes_prediction(xt):    
    prediction = loaded_model.predict(xt)    
    return f"Estimated Price Is  {prediction[0]}"
    
def main():
    st.title('House Price Prediction App')    
    lotsize = (st.text_input("lotsize"))
    bathrms = (st.text_input("bathrms"))
    stories = (st.text_input("stories"))
    driveway = (st.text_input("driveway"))
    recroom = (st.text_input("recroom"))
    fullbase = (st.text_input("fullbase"))
    gashw = (st.text_input("gashw"))
    airco = (st.text_input("airco"))
    garagepl = (st.text_input("garagepl"))
    prefarea = (st.text_input("prefarea"))
    #print(xt)
    #print("____________________________________________________________________")
    #print("Printing Details Of Collected Objects")
    #for i in xt[0]:
        #print(f"For {i} in Its Datatype= {type(i)}") 
    diagnosis = ''
    xxt=[[2000,3,2,1,0,1,0,0,1,0]]
    if st.button(f'Predict Result '):
        xt=[[int(lotsize),int(bathrms),int(stories),int(driveway),int(recroom),int(fullbase),int(gashw),int(airco),int(garagepl),int(prefarea)]]
    
        diagnosis = diabetes_prediction(xt)
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    