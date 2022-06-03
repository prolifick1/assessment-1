# note: I had to use Pytest module for tests because otherwise import wont work 
# for me.

from src.optimal_change import optimal_change

def test_optimal_change():
    assert(optimal_change(62.13, 100) == 'The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.')
    assert(optimal_change(31.51, 50) == 'The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.')
    assert(optimal_change(.50, .50) == 'no change due')
    assert(optimal_change(34.41, 12) == 'Not enough money')
    assert(optimal_change('pocket lint', True) == 'input must make sense')
    assert(optimal_change(50, 9999999) == 'number too big')
    assert(optimal_change(50, -50.32) == 'numbers must be positive')
