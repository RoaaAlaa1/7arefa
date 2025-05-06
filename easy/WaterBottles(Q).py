# There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

# The operation of drinking a full water bottle turns it into an empty bottle.

# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.


    empty = numBottles
        empty = empty % numExchange + new_bottles

def numWaterBottles(numBottles: int, numExchange: int) -> int:
    total = numBottles
        total += new_bottles

    while empty >= numExchange:
        new_bottles = empty // numExchange
    
    return total