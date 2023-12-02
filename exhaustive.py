def max_stocks(N, stocks_and_values, amount):
    def exhaust(index, remaining_money):
        # Base Case
        # No money left and reacht end of stocks_and_values
        if index == N or remaining_money == 0:                                                                  #O(1)
            return 0

        # Get value if we exclude current stock
        exclude_current = exhaust(index + 1, remaining_money)                                                   #Recursive so its O(N^2)

        # Get value if we include current stock
        include_current = 0
        value_of_current = stocks_and_values[index][1]
        if value_of_current <= remaining_money:
            include_current = stocks_and_values[index][0] + exhaust(index + 1, remaining_money - value_of_current)

        # Return max between exclude and include. 
        return max(exclude_current, include_current)                                                             #O(1)

    # Start from index 0
    return exhaust(0, amount)


# TODO READ FROM AN INPUT FILE
N = 4
# [number of stock, total value]
Stocks_and_values = [[1, 2], [4, 3], [5, 6], [6, 7]]
Amount = 12
result = max_stocks(N, Stocks_and_values, Amount)
print(result)