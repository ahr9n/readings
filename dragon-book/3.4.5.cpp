#include "bits/stdc++.h"

#pragma GCC optimize("Ofast")
#pragma GCC optimize("-O2")

using namespace std;

vector<int> failure(string pattern) {
    vector<int> longestPrefix(pattern.size());
    
    for (int i = 1, k = 0; i < pattern.size(); ++i) {
        // as long as we cannot add one more char in k, get best next prefix in pattern
        while (k > 0 && pattern[k] != pattern[i])
            k = longestPrefix[k - 1];
        
        if (pattern[k] == pattern[i]) ++k;
        longestPrefix[i] = k;
    }
    return longestPrefix;
}

vector<int> KMP(string txt, string pattern) {
    vector<int> matches(txt.size());
    vector<int> longestPrefix = failure(pattern);

    for (int i = 0, k = 0; i < txt.size(); ++i) {
        // as long as we cannot add one more char in k, get best next prefix
        while (k > 0 && pattern[k] != txt[i])
            k = longestPrefix[k - 1];

        // if we match character in the pattern, move in pattern
        if (pattern[k] == txt[i])
            k++;

        matches[i] = k;
        // if we matched, let's find one more matching
        if (k == pattern.size()) {
            k = longestPrefix[k - 1];
        }
    }
    return matches;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);

    string pattern;
    cin >> pattern;

    vector<int> longestPrefix = failure(pattern);
    for (int i = 0; i < longestPrefix.size(); cout << longestPrefix[i++] << " \n"[i == longestPrefix.size()]);

    string txt;
    cin >> txt;

    vector<int> matches = KMP(txt, pattern);
    if (matches.empty()) cout << "No matches exist.\n";
    else {
        for (int i = 0; i < matches.size(); ++i)
            cout << matches[i] << " \n"[i + 1 == matches.size()];
    }

    return 0;
}
