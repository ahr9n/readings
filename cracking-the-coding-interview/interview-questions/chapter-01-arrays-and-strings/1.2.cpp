#include "bits/stdc++.h"

using namespace std;

bool CheckPermutation(string a, string b) {
    if(a.size() != b.size()) return false;

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    return a == b;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);

    string a, b;
    cin >> a >> b;

    if(CheckPermutation(a, b))
        cout << "One of them is a permutation of the other.";
    else
        cout << "None of them is a permutation of the other.";

    return 0;
}
