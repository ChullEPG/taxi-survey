import pandas as pd 
import numpy as np
import os 
import matplotlib.pyplot as plt

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


def plot_cost_perception_comparison(owner_cost_perceptions, owner_driver_costs_perceptions, colors, cost_type, question):
    # Get unique values
    unique_vals = sorted(set(owner_cost_perceptions.index.tolist() + owner_driver_costs_perceptions.index.tolist()))
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom1 = None
    bottom2 = None
    count = 0
    for val in unique_vals:
        owner_val = owner_cost_perceptions[val] if val in owner_cost_perceptions else 0
        owner_driver_val = owner_driver_costs_perceptions[val] if val in owner_driver_costs_perceptions else 0
        ax.bar('Owner', owner_val, bottom=bottom1, label=val, color = colors[count])
        ax.bar('Driver/Owner', owner_driver_val, bottom=bottom2, color = colors[count])
        if bottom1 is None:
            bottom1 = 0
            bottom2 = 0
        bottom1 += owner_val 
        bottom2 += owner_driver_val
        count +=1

    ax.legend(title=f'{question}', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    ax.set_xlabel(f'{question}')
    ax.set_ylabel('Count')
    ax.set_title(f'Owner vs. Owner/Driver {cost_type} Cost Perceptions')
    plt.tight_layout()
    plt.savefig(f'figures/owner_vs_owner_driver_{cost_type}_cost_perceptions.png')
    plt.show()


def plot_pref_ev_comparison_among_groups(driver, owner, owner_driver, colors):
    #unique_vals = sorted(set([response.lower() for response in driver.index.tolist()]))
    unique_vals = sorted(set(driver.index.tolist()))
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom_driver = 0
    bottom_owner = 0
    bottom_driver_owner = 0
    count = 0
    
    for val in ['strongly agree', 'agree', 'neutral', 'disagree', 'strongly disagree', "don't know"]:
        driver_val = driver[val] if val in driver else 0
        owner_val = owner[val] if val in owner else 0
        owner_driver_val = owner_driver[val] if val in owner_driver else 0
        
        ax.bar('Driver', driver_val, bottom=bottom_driver,label = val, color=colors[count])
        ax.bar('Owner', owner_val, bottom=bottom_owner,  color=colors[count])
        ax.bar('Driver/Owner', owner_driver_val, bottom=bottom_driver_owner, color=colors[count])
        
        
        bottom_driver += driver_val
        bottom_owner += owner_val 
        bottom_driver_owner += owner_driver_val
        count += 1

    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    ax.set_ylabel('Normalised Count (%)')
    plt.title("Prefer electric taxi for driving or for business")
    plt.tight_layout()
    plt.savefig(f'figures/prefer_EV_among_groups.png')
    plt.show()