# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:39:52 2020

@author: UNIT
"""
import numpy as np
from datetime import datetime as dt

#function that calculates metrics from eskom data and outputs the metrics as a dictionary
#these metrics should include:
# Mean mean = np.mean(random_numbers)
# Median median=np.median()
# Maximum max=np.max()
# Minimum  min=np.min()
# Standard deviation   sigma = np.sqrt(variance)
# Variance    variance = np.var(random_numbers)


#FUNCTION 1
def Metrics_Calculator():
    
    

    Eskom_data=[2,4,6,7,1] #should be modified to a general level once eskom data is retrieved
    
    Mean=np.mean(Eskom_data)

    median= np.median(Eskom_data) #numpy np is used to access built in median() function
    

    Max=np.max(Eskom_data)
    
    
    Min=np.min(Eskom_data)

    
    variance=np.var(Eskom_data)
    sigma=np.sqrt(variance)
    
    
    dictionary={'min':Min,'median':median,'mean':Mean ,'variance':variance ,'Standard_Deviation':sigma ,'max':Max }
    print(dictionary ,'\n')# '\n' used for creating nextLine
    return dictionary

Metrics_Calculator()#declaration of function


#FUNCTION 2
def Five_Number_Sumry():
    
    
    data=[1,3,4,6,7]
    Min=np.min(data)
    Max=np.max(data)
    Mean=np.mean(data)
    Median=np.median(data)
    
    #google 1st quantile in python
    #google 3rd quantile in python
    #FQuantile=    
    #TQuantile=
    
    dictionary={'min':Min ,'max':Max,'mean': Mean,'median':Median,'1st_Quantile':0,'3rd_Quantile': 0}

    
    print(dictionary,'\n')
    return dictionary

Five_Number_Sumry()#declaration of function
    

#FUNCTION 3
def Date_Parser_Function(y,m,d):
    
    new_years = dt(y,m,d)
  

    
    ny_string = dt.strftime(new_years, '%A %d %B, %Y') #converts dateTime Obj to str to new format
    print(ny_string)
    
Date_Parser_Function(2020,2,13)#declaration of function date as a parameter
    
    
    
    
    
    


    