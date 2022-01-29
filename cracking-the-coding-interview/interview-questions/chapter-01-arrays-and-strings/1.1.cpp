#include "bits/stdc++.h"

using namespace std;

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
