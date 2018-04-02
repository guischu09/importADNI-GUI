	
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
 
#################### --- Treat string dialog text --- #####################
def treat_dialog_text(input_string):
 
    input_string = input_string.lower()
    special_characters1 = set('[~!@#$%^&*() ,_+{}":;\']+$').intersection(input_string)
                 
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
     
     
    #######################################
     
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
 
#################### --- END--- ####################
     
 
#################### --- Deal with Missing Data --- ####################
 
#--> Must do: Add imputation methods: KNN, MICE: fancy inpute package
def deal_missing_data(DataSet):
#       
    DataSet = DataSet.replace('-4',np.NaN)
    DataSet = DataSet.replace(' ',np.NaN)
    NewDataSet = DataSet.dropna(axis = 'rows',how = 'any')
             
    return NewDataSet
 
#################### --- END--- ####################
 
     
     
    
