class Solution {
public:
    string longestPalindrome(string s) {
        int length = s.length();
        if(length == 0)
            return "";
        int max_length = 0;
        string answer;
        vector<vector<bool>> dp(length, vector<bool>(length, false));
        for(int j = 0; j < length; ++j)
        {
            for(int i = 0; i <= j; ++i)
            {
                dp[i][j] = (s[i] == s[j]) && (j - i <= 2 || dp[i + 1][j - 1]);
                if(dp[i][j] && max_length < j - i + 1)
                {
                    max_length = j - i + 1;
                    answer = s.substr(i, max_length);
                }
            }
        }
        return answer;
    }
};

class Solution {
public:
    string longestPalindrome(string s) {
        int length = s.length();
        if(length == 0)
            return "";
        int max_length = 0;
        string answer;
        for(int i = 0; i < length; ++i)
        {
            // odd case
            int offset = 0;
            while(i - offset >= 0 && i + offset < length && s[i - offset] == s[i + offset])
                offset++;
            if(max_length < 2 * offset - 1)
            {
                max_length = max(max_length, 2 * offset - 1);
                answer = s.substr(i - offset + 1, max_length);
            }

            // even case
            offset = 0;
            int j = i + 1;
            while(i - offset >= 0 && j + offset < length && s[i - offset] == s[j + offset])
                offset++;
            if(max_length < 2 * offset)
            {
                max_length = max(max_length, 2 * offset);
                answer = s.substr(i - offset + 1, max_length);
            }
        }
        return answer;
    }
};
