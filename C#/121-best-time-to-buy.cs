using System;
public class Solution {
    public int MaxProfit(int[] prices) {
        int maxProfit = 0;
        int l = 0;
        int r = 1;

        while (r < prices.Length){
            maxProfit = Math.Max(maxProfit, prices[r] - prices[l]);
            if (prices[l] > prices[r]){
                l++;
            }else if(prices[l] < prices[r] || prices[l] == prices[r]){
                r++;
            }
        }
        return maxProfit;
    }
}