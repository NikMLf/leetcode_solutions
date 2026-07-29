class Solution {
    static constexpr int LIMIT = 1000001;

    int countWays(const vector<int>& cnt, const vector<vector<int>>& C) {
        int rem = 0;
        for (int x : cnt) rem += x;

        long long ways = 1;
        for (int c : cnt) {
            if (c == 0) continue;
            ways = min<long long>(LIMIT, ways * C[rem][c]);
            rem -= c;
            if (ways >= LIMIT) return LIMIT;
        }
        return (int)ways;
    }

public:
    string smallestPalindrome(string s, int k) {
        vector<int> freq(26, 0);
        for (char ch : s) freq[ch - 'a']++;

        vector<int> half(26, 0);
        string mid;

        int halfLen = 0;
        for (int i = 0; i < 26; ++i) {
            half[i] = freq[i] / 2;
            halfLen += half[i];
            if (freq[i] & 1) mid.push_back(char('a' + i));
        }

        // Precompute capped binomial coefficients up to halfLen.
        vector<vector<int>> C(halfLen + 1);
        C[0] = {1};
        for (int n = 1; n <= halfLen; ++n) {
            C[n].assign(n + 1, 1);
            for (int r = 1; r < n; ++r) {
                long long val = (long long)C[n - 1][r - 1] + C[n - 1][r];
                C[n][r] = (val >= LIMIT ? LIMIT : (int)val);
            }
        }

        if (countWays(half, C) < k) return "";

        string left;
        left.reserve(halfLen);

        for (int pos = 0; pos < halfLen; ++pos) {
            for (int ch = 0; ch < 26; ++ch) {
                if (half[ch] == 0) continue;

                half[ch]--;
                int ways = countWays(half, C);

                if (ways >= k) {
                    left.push_back(char('a' + ch));
                    break;
                }

                k -= ways;
                half[ch]++;
            }
        }

        string right = left;
        reverse(right.begin(), right.end());
        return left + mid + right;
    }
};