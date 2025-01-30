#include <iostream>
using namespace std;

long long keepLeftmostThreeOnes(long long num) {
    int count = 0;
    long long result = 0;
    if (num < 7) {
        return -1;
    }

    for (int i = 63; i >= 0; --i) {
        long long temp_num = num;
        if ((temp_num >> i) & 1) {
            result |= (1LL << i);  
            count++;
            if (count == 3) {  
                return result;
            }
        }
    }
    if (count == 1) {
        long long temp_num = num;
        result = 0;
        for (int i = 63; i >= 0; --i) {
            if ((temp_num >> i) & 1) {
                result |= (1LL << i - 1);
                result |= (1LL << i - 2);
                result |= (1LL << i - 3);
                return result;
            }
        }
    }
    if (count == 2) {
        int first_one = 0;
        for (int i = 63; i >= 0; --i) {
            long long temp_num = num;
            result = 0;
            if ((temp_num >> i) & 1) {
                count--;
                if (count == 0 && i > 1) {
                    result |= (1LL << first_one);
                    result |= (1LL << i - 1);
                    result |= (1LL << i - 2);
                    return result;
                } else 
                if (count == 0) {
                    result |= (1LL << first_one - 1);
                    result |= (1LL << first_one - 2);
                    result |= (1LL << first_one - 3);
                    return result;
                }
                first_one = i;
            }
        }
    }
    return -1;  
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        long long num;
        cin >> num;
        long long result = keepLeftmostThreeOnes(num);

        cout << result << '\n';
    }
    
    return 0;
}

 