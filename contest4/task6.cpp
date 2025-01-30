#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>

using namespace std;
using ll = long long;

ll gcd(ll a, ll b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b != 0) {
        ll t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int main() {
    int n;
    cin >> n;
    vector<ll> X(n), Y(n);
    for (int i = 0; i < n; i++) {
        cin >> X[i] >> Y[i];
    }
    
    if (n < 3) {
        cout << 0 << endl;
        return 0;
    }
    
    int c = 1;
    for (int i = 0; i < n; i++) {
        unordered_map<string, int> map;
        int same = 0, localMax = 0;
        
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            
            ll dx = X[j] - X[i];
            ll dy = Y[j] - Y[i];
            
            if (dx == 0 && dy == 0) {
                same++;
                continue;
            }
            
            ll g = gcd(dx, dy);
            dx /= g;
            dy /= g;
            
            if (dx < 0) {
                dx = -dx;
                dy = -dy;
            } else if (dx == 0 && dy < 0) {
                dy = -dy;
            }
            
            string key = to_string(dx) + "_" + to_string(dy);
            map[key]++;
            localMax = max(localMax, map[key]);
        }
        c = max(c, localMax + 1 + same);
    }
    
    if (c == n) {
        cout << 0 << endl;
        return 0;
    }
    
    int Xn = n - c;
    int res = 0;
    int limit = min(c / 2, Xn);
    
    for (int T = 0; T <= limit; T++) {
        int val = T + ((Xn - T) / 3);
        res = max(res, val);
    }
    
    cout << res << endl;
    return 0;
}

 