	
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:14:45 2018
 
@author: guilherme
"""
 
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:04:59 2018
 
@author: neurolab
"""
 
import numpy as np
from fuzzywuzzy import fuzz
from fancyimpute import BiScaler, KNN, NuclearNormMinimization, SoftImpute
import pandas as pd

 
#################### --- Treat string dialog text --- #####################
def treat_dialog_text(input_string):
 
    input_string = input_string.lower()
    special_characters1 = set('[~!@#$%^&*() ,+{}":;\']+$').intersection(input_string)
                 
    if not len(list(special_characters1)) == 0:
        for jj in list(special_characters1):
            # Get list of individual strings separated by special character j
            splited_input_string1 = input_string.split(jj)
            input_label = [None]*len(splited_input_string1)
                            
            for uu in range(len(splited_input_string1)):
                # remove extra blank spaces
                input_label[uu] = splited_input_string1[uu].strip() 
    else:
        input_label = [input_string]
         
        # make sure all elements in the list are non empty
    return(filter(None,input_label))
#    return(input_label)
#################### --- END--- ####################
     
     
 
#################### --- get_corresponding_labels --- ####################
def get_corresponding_labels(input_label,possible_labels):
           
    # Allocate memory
    match = [None]*len(possible_labels)
     
    # Iterate over all possible label targets available:
    for i in range(len(possible_labels)):
        # make the label target lower case
        target_label = possible_labels[i].lower()
        # Find special characteres that might be found in the target label string
        special_characters2 = set('[~!@#$%^&*() _+{}":;\']+$').intersection(target_label)
     
        if not len(list(special_characters2)) == 0:
            # Iterate over all special characteres found and get each component of the string individually
            for j in list(special_characters2):
                # Get list of individual strings separated by special character j
                splited_target_label2 = target_label.split(j)
                # Allocate memory
                temp_match = [None]*len(splited_target_label2)
     
                #Iterate over for all string components and evaluate them individually
                for u in range(len(splited_target_label2)):
                    # Evaluate input string label
                    temp_match[u] = fuzz.partial_ratio(input_label,splited_target_label2[u])
     
        else:
            # Evaluate input string label
            temp_match = fuzz.partial_ratio(input_label,target_label)
               
        # Find the maximum value of similarity among all strings separated by special characters
        match[i] = np.max(temp_match)
     
     
    # indices of the best matches:
    multiple_matches = np.where(match == np.max(match))
    # Get the array of indices itself
    multiple_matches = multiple_matches[0]
     
    # Check if there are multiple indices
    if np.size(multiple_matches) > 1:
        final_match = [None]*np.size(multiple_matches)# Allocate Memory
        final_match_index = [None]*np.size(multiple_matches)# Allocate Memory
 
         
        for ii in range(np.size(multiple_matches)):
            final_match[ii] = possible_labels[multiple_matches[ii]]
            final_match_index[ii] = multiple_matches[ii]
             
    else:
        final_match_index = np.argmax(match)
        final_match = [possible_labels[final_match_index]]
         
#    return (final_match,final_match_index)
    return (final_match)
 
#################### --- get_corresponding_labels END--- ####################
     
 
#################### --- Deal with Missing Data --- ####################
# Change The name of the local variable that are equal to the global variables
# There are still some bugs with KNN to deal with....    

def deal_missing_data(NewDataSet, options,selectedFeatures):
    
   while switch(options):
       if case('None'):
           DataSetDealt = NewDataSet
           
       if case('Remove All'):
           NewDataSet = NewDataSet.replace('-4',np.NaN)
           NewDataSet = NewDataSet.replace(' ',np.NaN)
           NewDataSet = NewDataSet.dropna(axis = 'rows',how = 'any')
           DataSetDealt = fixBrokenDataSet(NewDataSet,'Default')
           
       if case('Impute with KNN'):
           NewDataSet = NewDataSet.replace('-4',np.NaN)
           NewDataSet = NewDataSet.replace(' ',np.NaN)
           NewDataSet = fixBrokenDataSet(NewDataSet,'TurnNaN')
           NewDataSet = KNN(k=7).complete(NewDataSet)
           DataSetDealt = pd.DataFrame(NewDataSet,columns = selectedFeatures)
           
       if case('Impute with MICE'):
           NewDataSet = NewDataSet.replace('-4',np.NaN)
           NewDataSet = NewDataSet.replace(' ',np.NaN)
           NewDataSet = fixBrokenDataSet(NewDataSet,'TurnNaN')           
           DataSetDealt = NuclearNormMinimization().complete(NewDataSet)
           DataSetDealt = pd.DataFrame(NewDataSet,columns = selectedFeatures)
       break
       
   return DataSetDealt       
     
#################### --- Deal with Missing Data END--- ###################
    

#################### --- Deal with Missing Data --- ####################

#def deal_missing_data(NewDataSet, options):
#    
#   while switch(options):
#       if case('None'):
#           DataSetDealt = NewDataSet
#           
#       if case('Remove All'):
#           NewDataSet = NewDataSet.replace('-4',np.NaN)
#           NewDataSet = NewDataSet.replace(' ',np.NaN)
#           NewDataSet = NewDataSet.dropna(axis = 'rows',how = 'any')
#           DataSetDealt = fixBrokenDataSet(NewDataSet,'Default')
#           
#       if case('Impute with KNN'):
#           NewDataSet = NewDataSet.replace('-4',np.NaN)
#           NewDataSet = NewDataSet.replace(' ',np.NaN)
#           NewDataSet = fixBrokenDataSet(NewDataSet,'Default')
#           DataSetDealt = KNN(k=7).complete(NewDataSet)
#           
#       if case('Impute with MICE'):
#           NewDataSet = NewDataSet.replace('-4',np.NaN)
#           NewDataSet = NewDataSet.replace(' ',np.NaN)
#           NewDataSet = fixBrokenDataSet(NewDataSet,'Default')           
#           DataSetDealt = NuclearNormMinimization().complete(NewDataSet)
#       break
#       
#   return DataSetDealt       
     
#################### --- Deal with Missing Data END--- ####################


#################### --- Switch Case implementation --- ####################



class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

#################### --- Switch Case implementation END --- ####################


#################### --- SfixBrokenDataSet --- ####################

# This function should be applied only for numeric pre filtered data
def fixBrokenDataSet(DataSet,*args):    
    for option in args:
        while switch(option):
            if case('TurnNaN'):
                # Find the rows that have crazy simbols and make them NaN
                [rows, cols] = DataSet.shape
                
                NumeriColumns = FindNumeriCols(DataSet)
        
                for uu in range(rows):    
                    single_row = DataSet.iloc[uu, NumeriColumns]
                    
                    try:
                        single_row.astype(np.float)        
                    except ValueError:
                        DataSet.iloc[uu,:] = np.NaN
                
                return (DataSet)
                
                
            if case('Default'):
            # Remove the rows that have crazy simbols
                [rows, cols] = DataSet.shape
                
                NumeriColumns = FindNumeriCols(DataSet)
        
                for uu in range(rows):    
                    single_row = DataSet.iloc[uu, NumeriColumns]
                    
                    try:
                        single_row.astype(np.float)        
                    except ValueError:
                        DataSet.iloc[uu,:] = np.NaN
                
                DataSet = DataSet.dropna(axis = 'rows',how = 'any') 
                return (DataSet)
            break  
        
#################### --- SfixBrokenDataSet END --- ####################


#################### --- FindNumeriCols --- ####################

def FindNumeriCols(DataSet):
    
    [rows, cols] = DataSet.shape
    
    N = 20 # This is an arbitrary choice
    cont = np.zeros(cols)
    
    for jj in range(cols):
        for uu in range(N):
            
            single_element = DataSet.iloc[uu,jj]
            
            try:
                float(single_element)
                cont[jj] = cont[jj] + 1
                        
            except ValueError:
                continue               
                
    NumeriColumns = cont > 4 # This is an arbitrary choice
    return (NumeriColumns)

#################### --- FindNumeriCols END --- ####################
