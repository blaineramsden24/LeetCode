public class Solution{
    public int LengthOfLongestSubstring(string s){
        int l = 0;
        int r = 1;
        string longestSubstring = '';

        while (r < s.Length){
            currentSubstring = s[l:r];
            if (!currentSubstring.Contains(s[r])){
                if(r - l > longestSubstring.Length){
                    longestSubstring = currentSubstring;
                }
            }else{
                l = r;
                r ++;
            }
        }
        return longestSubstring.Length;
    }
}