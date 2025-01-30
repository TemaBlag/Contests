#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    int min_a = *min_element(a.begin() + 1, a.end());
    int max_a = *max_element(a.begin() + 1, a.end());
    int result = INT_MAX;


    for (int a1 = min_a; a1 <= max_a; ++a1) {
        for (int a2 = a1; a2 <= max_a; ++a2) {
            vector<int> corrections;
            int cost = abs(a1 - a[1]) + abs(a2 - a[2]);
            for (int i = 3; i <= n; ++i) {
                if (a[i] < a1) {
                    corrections.push_back(a1 - a[i]);
                } else if (a[i] > a2) {
                    corrections.push_back(a[i] - a2);
                } else {
                    corrections.push_back(0);
                }
            }

            sort(corrections.begin(), corrections.end());
            for (int i = 0; i < m; ++i) {
                cost += corrections[i];
            }
            result = min(result, cost);
        }
    }
    cout << result << endl;
    return 0;
}

 