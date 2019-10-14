from django.shortcuts import render
from . import forms
import numpy as np
import pandas as pd
import math
from django.http import HttpResponse
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
#from django.shortcuts import render_to_response
#from formtools.wizard.views import SessionWizardView
#from django.core.mail import send_mail
import pickle
#logr=logging.getLogger(__name__)

#X_train, X_test, Y_train, Y_test =0,0,0,0
# Create your views here.
def homepage(request):
    breast_cancer_data = pd.read_csv("data.csv")
    df=breast_cancer_data.drop('Unnamed: 32',axis=1)
    
    df.drop('id',axis=1,inplace=True)
    labelencoder_Y = LabelEncoder()
    df.iloc[:,0] = labelencoder_Y.fit_transform(df.iloc[:,0].values)
    drop_list = ['perimeter_mean','radius_mean','compactness_mean','concave points_mean','radius_se','perimeter_se','radius_worst','perimeter_worst','compactness_worst','concave points_worst','compactness_se','concave points_se','texture_worst','area_worst']
    df = df.drop(drop_list,axis = 1 )      
    X=df.drop('diagnosis',axis=1)
    X = (X -np.min(X))/(np.max(X)-np.min(X)).values
    Y=df['diagnosis']
    #x_scale=MinMaxScaler().fit_transform(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.30, random_state = 40)
    l=[X_train,X_test,Y_train,Y_test]
    with open("splitdata.dat",'wb') as f:
        pickle.dump(l,f)
    return render(request,'pages/homepage.html')

def homepage1(request):
    return render(request,'pages/homepage.html')

def user_input(request):
    form1=forms.Mean()
    form2=forms.SymanticError()
    form3=forms.Worst()
    return render(request,'pages/inputform.html',{'form1':form1,'form2':form2,'form3':form3})
    
def user_input_final(request):
    if request.method == 'POST':
        form=forms.Mean(request.POST)
        form1=forms.SymanticError(request.POST)
        form2=forms.Worst(request.POST)
        l=[]
        if form.is_valid():
            for i in form.cleaned_data:
                l.append(form.cleaned_data[i])
        if form1.is_valid():
            for i in form1.cleaned_data:
                l.append(form1.cleaned_data[i])
        if form2.is_valid():
            for i in form2.cleaned_data:
                l.append(form2.cleaned_data[i])
        with open("splitdata.dat",'rb') as f:
            l1=pickle.load(f)
        forest=rf(n_estimators=35,criterion='entropy',random_state=40)  
        #print(l1[0],l1[1])
        forest.fit(l1[0],l1[2])
        with open("max_min.dat",'rb') as f:
            l2=pickle.load(f)
        for i in range(16):
            min=l2[i][1]
            max=l2[i][0]
            if l[i]<min:
                l[i]=0.0
            elif l[i]>max:
                l[i]=1.0
            else:
                l[i]=round(((l[i]-min)/(max-min)),6)
        check=forest.predict([l])
        print(l,check)
        if check==[1]:
            return render(request,'pages\detected.html')
        else:
            return render(request,'pages\_nodetected.html')
            