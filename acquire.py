import numpy as np 
import pandas as pd 

def acquire_semicon():
    df =  pd.read_csv('secom.data', sep=' ', header=None)
    labels = pd.read_csv('secom_labels.data', sep=' ', header=None)

    df['timestamp'] = labels[1]
    df['defect'] = labels[0]
    df.defect = df.defect.apply(lambda x: 0 if x == -1 else 1)
    return df

