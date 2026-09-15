#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    long long m = 1;
    long long current = 1;

    while (true) {
        if (current % n == 0) {
            cout << m << endl;
            break;
        }
        else {
            cout << current << endl;
            m += 1;
            current *= m;
        }
    }

    return 0;
}
