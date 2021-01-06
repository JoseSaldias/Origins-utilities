# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:43:01 2020

@author: Heffer
"""
# Dependencies
import random
import pandas as pd

def hd_refine():
    """
    hd_refine simulates a refine session for a single gear until it breaks or
    reaches +9. outputs are state: 1 if success or 0 if gear broke and total
    money spent on enriched stones.    
    """
    # State Variables
    cost = 0
    counter = 0
    e_elu = 500000
    hd_elu = 1500000
    state = 1 # success
    current_refine = 0
    refine_table = {0:[100, 0], 1:[100, 0], 2:[100, 0], 3:[100, 0], 4:[100, 0],
                5:[90, e_elu], 6:[90, e_elu], 7:[70, hd_elu], 8:[40, hd_elu],
                9:[40, hd_elu]}

    # Upgrade until +9 or break
    while current_refine < 9:
        
        # Refine roll
        chance = random.randint(0, 100)
    
        if refine_table[current_refine][0] >= chance:
            current_refine += 1
            cost += refine_table[current_refine][1]
            counter += 1
            
        else:        
            
            # Use of Hd ore
            if current_refine in [7,8]:
                current_refine -= 1
                counter += 1
            
            # Weapon is broken
            else:
                counter += 1
                state = 0 # failure
                break
    
    return state, cost/1000000

def enriched_refine():
    """
    hd_refine simulates a refine session for a single gear until it breaks or
    reaches +9. outputs are state: 1 if success or 0 if gear broke and total
    money spent on enriched stones.    
    """
    # State Variables
    cost = 0
    counter = 0
    e_elu = 500000
    state = 1 # success
    current_refine = 0
    refine_table = {0:[100, 0], 1:[100, 0], 2:[100, 0], 3:[100, 0], 4:[100, 0],
                5:[90, e_elu], 6:[90, e_elu], 7:[70, e_elu], 8:[40, e_elu],
                9:[40, e_elu]}

    # Upgrade until +9 or break
    while current_refine < 9:
        
        # Refine roll
        chance = random.randint(0, 100)
    
        if refine_table[current_refine][0] >= chance:
            current_refine += 1
            cost += refine_table[current_refine][1]
            counter += 1
            
        else:        
            # Weapon is broken
            counter += 1
            state = 0 # failure
            break
    
    return state, cost/1000000

# Store results
result_storage = []
cost_storage = []
n = 100
for i in range(n):
    result, cost = enriched_refine()
    result_storage.append(result)
    cost_storage.append(cost)

df = pd.DataFrame({'Gear state':result_storage, 'Zeny spent[M]':cost_storage})

