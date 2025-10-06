import re,time
import numpy as np

def add_to_order(order, item_name, quantity, price_per_item):
    if quantity < 0 or price_per_item <0:
        return False
    if item_name not in order:
        order[item_name] = quantity,price_per_item
    else: order[item_name][0] += quantity

def remove_from_order(order,item_name):
    try:
        del order[item_name]
    except: return False
    else: return True
    
def calculate_bill(order,tax_rate):
    sum = 0
    for item in order.values():
        sum += (item[1] * item[0])
    sum += (sum * (tax_rate / 100))
    return sum

def get_most_expensive_item(order):
    most_expensive = (None, (0, 0))  # (item_name, (quantity, price_per_item))
    for item in order.items():
        if (item[1][1] * item[1][0]) > (most_expensive[1][1] * most_expensive[1][0]):
            most_expensive = item
    return most_expensive[0]

def 