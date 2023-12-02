def max_stocks(N, stocks_and_values, amount):
    def exhaust(index, remaining_money):
        # Base Case
        # No money left and reacht end of stocks_and_values
        if index == N or remaining_money == 0:                                                                  #O(1)
            return 0

        # Check what happens if we exclude current stock
        exclude_current = exhaust(index + 1, remaining_money)                                                   #Recursive so its O(N^2)

        # Check out what happens if we include current stock
        include_current = 0
        value_of_current = stocks_and_values[index][1]
        if value_of_current <= remaining_money:
            include_current = stocks_and_values[index][0] + exhaust(index + 1, remaining_money - value_of_current)

        # Return max between exclude and include. 
        return max(exclude_current, include_current)                                                             #O(1)

    # Start from index 0
    return exhaust(0, amount)


# TEST CASES
TEST_CASES = [{
    "N":4,
    "stock_and_values":[[1, 2], [4, 3], [5, 6], [6, 7]],
    "amount" : 12
},{
    "N":2,
    "stock_and_values":[[3, 2], [4, 3],],
    "amount" : 2
},{
    "N":3,
    "stock_and_values":[[1, 2], [4, 3], [5, 6]],
    "amount" : 5
},{
    "N":4,
    "stock_and_values":[[50, 20], [1, 5], [2, 5], [3, 5]],
    "amount" : 20
},{
    "N":5,
    "stock_and_values":[[1, 100], [10, 5], [10, 5], [10, 5],[10, 5]],
    "amount" : 100
},]

for idx,test in enumerate(TEST_CASES):
    print(f"==============TEST CASE {idx+1}==============")
    print(f'N: {test["N"]}')
    print(f'stocks_and_values: {test["stock_and_values"]}')
    print(f'amount: {test["amount"]}')
    result =  max_stocks(test["N"], test["stock_and_values"], test["amount"])
    print(f'\nResult for Test Case {idx+1}: {result}\n')