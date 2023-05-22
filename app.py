import numpy as np
import streamlit as st
from backend import prediction


def predictHeartDisease(input_data):
    input_data=np.asarray(input_data).reshape(1,-1)

    returned_value=prediction(input_data)
    answer=int(returned_value)
    if answer==1:
            st.error("POSSIBLE CARDIAC DISEASE DETECTED.")
    else: 
            st.success("YOUR CONDITION SEEMS FINE. BUT FEEL FREE TO CONSULT A PHYSICIAN IF YOU ARE FELLING UNWELL.")

    f = open("user_records.txt", "a")
    f.write(str(input_data))
    f.write(": ")
    f.write(str(answer))
    f.write("\n")
    f.close()
    
    return

if __name__ == '__main__':
    # give a title to our app
    st.title('CARDIAC DISEASE PREDICTION APP')
    
    age=st.number_input("ENTER YOUR AGE",min_value=0, max_value=9999, value=0,step =1)

    sex = st.radio(
        "YOUR GENDER",
        ('MALE', 'FEMALE'))

    cp = st.radio(
        "ARE YOU HAVING CHEST PAIN?",
        ('SEVERE PAIN','CHEST PAIN WITH TIGHTNESS','MILD CHEST PAIN WITH DISCOMFORT','NO')
        )

    trestbps=st.number_input("ENTER YOUR CURRENT SYSTOLIC BLOOD PRESSURE",min_value=0, max_value=9999, value=0,step =1)

    chol=st.number_input("ENTER YOUR SERUM CHOLESTEROL LEVEL",min_value=0, max_value=9999, value=0,step =1)

    fbs=st.radio("ARE YOU DIABETIC?",
                 ('YES (if FastingBS > 120 mg/dl)', 'NO (if FastingBS < 120 mg/dl)')
                )

    restecg=st.radio("RESTING ELECTROCARDIOGRAM RESULT(SELECT NORMAL IF YOU DON'T KNOW THE EXACT CONDITION)",
                    ('NORMAL','ST-T ABNORMALITY','LEFT VENTRICULAR HYPERTROPHY')
                    )

    thalach=st.number_input("ENTER YOUR HIGHEST HEART RATE IN LAST 5 MIN",min_value=0, max_value=9999, value=0,step =1)

    exang=st.radio("DO YOU HAVE CHEST PAIN DURING PHYSICAL ACTIVITIES?",
                ('YES','NO')
                )

    oldpeak=st.number_input("NUMERIC VALUE MEASURED IN ST DEPRESSION (NORMAL VALUE IS < 0.5)",min_value=0.0, max_value=9999.0, value=0.0,step =0.1,format="%.1f")

    slope=st.radio("THE SLOPE OF THE PEAK EXERCISE ST SEGMENT (SELECT NORMAL IF YOU DON'T KNOW THE EXACT CONDITION)",
                   ('UPSLOPING (NORMAL CONDITION)','FLAT (SLIGHT ABNORMALITY)','DOWNSLOPING (SEVERE ABNORMALITY)')
                )

    if sex =="MALE":
        sex=1
    else:
        sex=0


    if cp=="SEVERE PAIN":
        cp=1
    elif cp=="CHEST PAIN WITH TIGHTNESS":
        cp=2
    elif cp=="MILD CHEST PAIN WITH DISCOMFORT":
        cp=3
    else:
        cp=4


    if fbs=="YES (if FastingBS > 120 mg/dl)":
        fbs=1
    else:
        fbs=0

    if restecg=="NORMAL":
        restecg=0
    elif restecg=="ST-T ABNORMALITY":
        restecg=1
    else:
        restecg=2


    if exang =="YES":
        exang=1
    else:
        exang=0


    if slope=="UPSLOPING":
        slope=1
    elif slope=="FLAT":
        slope=2
    else:
        slope=3
    
    
   

    if st.button("PREDICT HEART CONDITION"):
         predictHeartDisease([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope])
       
    