#include "bits/stdc++.h"

#pragma GCC optimize("Ofast")
#pragma GCC optimize("-O2")

using namespace std;
using ll = long long;
using ld = long double;

const int N = 3E5 + 5, M = 1E6 + 10, MOD = 1E9 + 7, OO = 0x3f3f3f3f;

bool IsUnique(string s) {
    map<char, bool> chars;
    for (char &ch:s) {
        if (chars[ch]) return false;
        chars[ch] = true;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);

    string s;
    cin >> s;
    cout << (IsUnique(s) ? "Is unique." : "Is not unique.");

    return 0;
}
