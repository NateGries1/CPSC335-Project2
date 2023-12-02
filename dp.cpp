#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>


using namespace std;

int solve(vector<int>& value, vector<int>& stocks, int max_amount) {
    vector<vector<int>> dp(value.size()+1, vector<int>(max_amount+1, 0));
    
    for (int i = 1; i < value.size()+1; ++i) {
        for (int j = 1; j < max_amount+1; ++j) {
            if (value[i-1] <= j) {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-value[i-1]] + stocks[i-1]);
            } else {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    
    return dp.back().back();
}
int main() {
    int num_stocks;
    while (cin >> num_stocks) {
        vector<int> stocks(num_stocks);
        vector<int> values(num_stocks);
        pair<int, int> stock;
        for (int i = 0; i < num_stocks; ++i) {
            int price, value;
            cin >> price >> value;
            stocks[i] = price;
            values[i] = value;
        }

        int amount;
        cin >> amount;

        int result = solve(values, stocks, amount);
        cout << "Result is " << result << endl;
    }

    
}