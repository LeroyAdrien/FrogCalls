import librosa
import sys 
import os
import numpy as np
import pandas as pd
from scipy.io.wavfile import write


dataframe=pd.read_csv("../anuran_calls/Frogs_MFCCs.csv")
mfccs=dataframe.iloc[500,:-4].values
mfccs=np.array([mfccs])


print(mfccs.shape)
print(mfccs)




y=librosa.feature.inverse.mfcc_to_audio(mfccs,n_mels=mfccs.shape[0])
scaled = np.int16(y/np.max(np.abs(y)) * 32767)
write('test2.wav', 44100, scaled)
print(y.shape)
"""


y, sr = librosa.load("./test.wav")
    
#determine if instruemnt is harmonic or percussive by comparing means
y_harmonic, y_percussive = librosa.effects.hpss(y)
if np.mean(y_harmonic)>np.mean(y_percussive):
    harmonic=1
else:
    harmonic=0
    
#Mel-frequency cepstral coefficients (MFCCs)
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

print(mfcc)
print(type(mfcc))
print(mfcc.shape)

"""