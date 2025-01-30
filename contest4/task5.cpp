#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    long long s;
    cin >> n >> s;
    vector<long long> a(n + 1), p(n + 1), leftLimit(n + 1), G(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }
    for (int i = 1; i <= n; ++i) {
        p[i] = p[i - 1] + a[i];
    }
    int L = 1;
    for (int i = 1; i <= n; ++i) {
        while (p[i] - p[L - 1] > s) {
            L++;
        }
        leftLimit[i] = L;
    }
    G[0] = 0;
    for (int i = 1; i <= n; ++i) {
        G[i] = G[leftLimit[i] - 1] + i;
    }
    long long res = 0;
    for (int i = 1; i <= n; ++i) {
        res += G[i];
    }
    cout << res << endl;
    return 0;
}

 