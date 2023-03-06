import pandas as pd 
import numpy as np
import os 

def get_crosstabs(df, features, targets):
    '''
    Get crosstabs between multiple features and targets
    '''
    ctabs = {}
    for target in targets:
        ctabs[target] = {}
        for feature in features:
            ctabs[target][feature] = pd.crosstab(df[feature], df[target])
    return ctabs 



def extract_responses_value_counts(column):
    '''
    Extract responses from a column with multiple answers per row and return a dictionary of counts
    '''
    all_responses = []
    for response in column:
        if isinstance(response, str):
            split_responses = response.split(';')
            all_responses.extend([r.strip() for r in split_responses])
    unique_responses = list(set(all_responses))
    unique_responses = [r for r in unique_responses if r != '']
    counts = {response: all_responses.count(response) for response in unique_responses}
    return counts

def extract_responses(column):
    all_responses = []
    for response in column:
        if isinstance(response, str):
            split_responses = response.split(';')
            all_responses.extend([r.strip() for r in split_responses])
    unique_responses = list(set(all_responses))
    unique_responses = [r for r in unique_responses if r != '']
    return unique_responses
