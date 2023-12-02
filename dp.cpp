#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>


using namespace std;

int solve(vector<int>& price, vector<int>& value, int max_amount) {
    vector<vector<int>> dp(price.size()+1, vector<int>(max_amount+1, 0));
    
    for (int i = 1; i < price.size()+1; ++i) {
        for (int j = 1; j < max_amount+1; ++j) {
            if (price[i-1] <= j) {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-price[i-1]] + value[i-1]);
            } else {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    
    return dp.back().back();
}
int main() {
    cout << "Reading Input..." << endl;
    int num_stocks;
    cin >> num_stocks;

    vector<int> prices(num_stocks);
    vector<int> values(num_stocks);
    pair<int, int> stock;
    for (int i = 0; i < num_stocks; ++i) {
        int price, value;
        cin >> price >> value;
        prices[i] = price;
        values[i] = value;
    }

    int amount;
    cin >> amount;
    cout << "Done" << endl;

    cout << "\nSolving...\n";
    int result = solve(prices, values, amount);
    cout << "Result is " << result << endl;
}