#include <bits/stdc++.h>

using namespace std;
long long lcm(long long a, long long b) {
    return (a / std::__gcd(a, b)) * b;
}

long long lcm_of_three(long long a, long long b, long long c) {
    return lcm(lcm(a, b), c);
}

int main() {
    long long n, x, y, z;
    cin >> n >> x >> y >> z;

    vector<long long> a(n);
    for (long long i = 0; i < n; ++i) {
        cin >> a[i];
    }
    if(n==1) {long long result = lcm_of_three(x, y, z); cout<<(result - (a[0] % result)) % result;return 0;}
    vector<pair<long long, int>> ops_x(2*n), ops_y(2*n), ops_z(2*n);

    for (int i = 0; i < n; ++i) {
        ops_x[i] = { (x - (a[i] % x)) % x, i };
        ops_y[i] = { (y - (a[i] % y)) % y, i };
        ops_z[i] = { (z - (a[i] % z)) % z, i };
        ops_x[i+n] = { (x - (a[i] % x)) % x+x, i };
        ops_y[i+n] = { (y - (a[i] % y)) % y+y, i };
        ops_z[i+n] = { (z - (a[i] % z)) % z+z, i };

    }
    sort(ops_x.begin(), ops_x.end());
    sort(ops_y.begin(), ops_y.end());
    sort(ops_z.begin(), ops_z.end());
    long long min_operations = LLONG_MAX;
    long long m=100;
    for (int i = 0; i < min(2*n,m); ++i) {
        long long op_x = ops_x[i].first;
        int idx_x = ops_x[i].second;

        for (int j = 0; j < min(2*n,m); ++j) {
            long long op_y = ops_y[j].first;
            int idx_y = ops_y[j].second;

            if (idx_x == idx_y and op_x!=op_y) continue;

            for (int k = 0; k < min(2*n,m); ++k) {
                long long op_z = ops_z[k].first;
                int idx_z = ops_z[k].second;
                long long total_operations;
                if (idx_x == idx_z and op_x!=op_z  || idx_y == idx_z and op_z!=op_y) continue;
                if(idx_x == idx_z and idx_x == idx_y) total_operations = op_x;
                else if(idx_x == idx_z and idx_x != idx_y) total_operations = op_x+op_y;
                else if(idx_x != idx_z and idx_x == idx_y) total_operations = op_x+op_z;
                else if(idx_y == idx_z and idx_x != idx_y) total_operations = op_y+ op_x;
                else total_operations = op_x + op_y + op_z;

                min_operations = min(min_operations, total_operations);
            }
        }
    }
    cout << min_operations << endl;
    return 0;
}

 