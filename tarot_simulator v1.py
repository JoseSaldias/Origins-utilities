# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


spam_rate = 2 # Skills per second
exposure_time = 9 # seconds
tarots_available = 4

total_ticks = spam_rate * exposure_time * tarots_available
desired_cards = 6 # Amount of acceptable tarot card effects

success_chance = 0.4
card_chance = desired_cards * 1/14
final_chance = card_chance * success_chance

def interaction(final_chance):
    roll = random.uniform(0, 1)
    if roll >= final_chance:
        return 0
    else:
        return 1

def gvg(total_ticks, final_chance):
    c = 0
    for i in range(total_ticks):
        c += interaction(final_chance)
    return c


gvg_amount = 100
result = {}

for i in range(gvg_amount):
    result[i] = gvg(total_ticks, final_chance)

final = pd.DataFrame(result.values(), columns=(['Inflicted cards per gvg']))

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})

sns.set_style(r"whitegrid")
sns.countplot(final[r'Inflicted cards per gvg'])
plt.show()