
#include <iostream>
#include <vector>

using namespace std;

const int mod = 998244353;
vector<long long> x;
vector<vector<long long> > powers;

long long mod_pow(long long base, long long exp) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

vector<long long> precompute_factorials(int n) {
    vector<long long> factorial(n + 1);
    factorial[0] = 1;
    for (int i = 1; i <= n; i++) {
        factorial[i] = (factorial[i - 1] * i) % mod;
    }
    return factorial;
}

vector<long long> precompute_inverse_factorials(const vector<long long> &factorial) {
    int n = factorial.size() - 1;
    vector<long long> inv_factorial(n + 1);
    inv_factorial[n] = mod_pow(factorial[n], mod - 2); // Fermat's Little Theorem
    for (int i = n - 1; i >= 0; i--) {
        inv_factorial[i] = (inv_factorial[i + 1] * (i + 1)) % mod;
    }
    return inv_factorial;
}

long long binomial_coefficient(long long n, long long k, const vector<long long> &factorial,
                               const vector<long long> &inv_factorial) {
    if (k > n) return 0;
    return (factorial[n] * inv_factorial[k] % mod) * inv_factorial[n - k] % mod;
}

long long calc_x(const vector<long long> &a, int r) {
    long long sum = 0;
    for (int i = 1; i < a.size(); i++) {
        sum = (sum + powers[i][r]) % mod;
    }
    return sum;
}

void calc_power(vector<long long> &a, int n, int k) {
    for (int i = 0; i <= n; i++) {
        powers.push_back(vector<long long>(k + 1, 1));
    }
    for (int i = 1; i <= n; i++) {
        ;
        powers[i][0] = 1;
        for (int j = 1; j <= k; j++) {
            long long res = mod_pow(a[i], j);
            powers[i][j] = res;
        }
    }
}

void calc_x_vector(vector<long long> &a, int k) {
    for (int r = 0; r <= k; r++) {
        x.push_back(calc_x(a, r));
    }
}


long long calc_b(const vector<long long> &a, int p, const vector<long long> &factorial,
                 const vector<long long> &inv_factorial) {
    long long res = 0;
    for (int m = 0; m <= p; m++) {
        res = (res + (binomial_coefficient(p, m, factorial, inv_factorial) *
                      x[m] % mod *
                      x[p - m] % mod)) % mod;
    }
    return res;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        a[i] = a[i] % mod;
    }

    calc_power(a, n, k);
    calc_x_vector(a, k);

    vector<long long> factorial = precompute_factorials(n);
    vector<long long> inv_factorial = precompute_inverse_factorials(factorial);

    for (int p = 1; p <= k; p++) {
        long long result = (calc_b(a, p, factorial, inv_factorial) -
                            mod_pow(2, p) * x[p] % mod + mod) % mod;
        cout << result * mod_pow(2, mod - 2) % mod << endl;
    }
}

 