#include "bits/stdc++.h"

using namespace std;

string URLify(string s) {
    string ret;
    for (int i = 0; i < s.size(); ++i) {
        if(s[i] == ' ') ret += "%20";
        else            ret += s[i];
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);

    string input;
    getline(cin, input, '\n');

    int n;
    for (int i = input.size() - 1; i >= 0; --i) {
        if(isdigit(input[i]) == false){
            n = stoi(input.substr(i + 1));
            input = input.substr(0, n);
            break;
        }
    }

    string output = URLify(input);
    cout << "String after is: " << output;

    return 0;
}
