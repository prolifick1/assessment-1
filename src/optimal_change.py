# Write your solution here!
import re

def optimal_change(item_price, cash_paid):
    if(isinstance(item_price, (int, float)) and isinstance(item_price, (int, float))):
        pass
    else:
        return 'input must make sense'
    if(item_price == cash_paid):
        return 'no change due'
    if(cash_paid > 99999):
        return 'number too big'
    if((item_price < 0) or (cash_paid < 0)):
        return 'numbers must be positive'
    if(cash_paid < item_price):
        return 'Not enough money'
    denominations = {
            10000: '$100 bills',
            5000: '$50 bills',
            2000: '$20 bills',
            1000: '$10 bills',
            500: '$5 bills',
            100: '$1 bills',
            25: 'quarters',
            10: 'dimes',
            1: 'pennies'
        }

    item_price_cents = int(100 * item_price)
    cash_paid_cents = int(100 * cash_paid)
    total_change_cents = cash_paid_cents - item_price_cents
    total_change = total_change_cents / 100
        
    print(f'total change: {total_change}')
    
    substring = ''
    for denom in denominations:
        count = 0
        while (total_change_cents / denom) >= 1:
           total_change_cents -= denom
           count+=1
        if count > 0:
            if(count == 1):
                substring += f'{count} {denominations[denom]}, '.replace('s', '')
            else:
                substring += f'{count} {denominations[denom]}, '
    
    
    res = f'The optimal change for an item that costs ${item_price} with an amount paid of ${cash_paid} is {substring}.' 
    last_denom = re.findall('\w+', res)[-1]
    last_num = re.findall('\d', res)[-1]
    print(f'last_num {last_num}')
    if(last_num == 1 and last_denom == 'pennies') :
        last_denom = 'penny'
    res = re.sub(r"\s\d\s\w+, \.", f' and {last_num} {last_denom}.', res)
    print(res) 
    return(res)

