class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int min = prices[0];
        for(int price: prices) {
            if(price >= min) {
                maxP = Math.max(maxP, price - min);
            } else {
                min = price;
            }
        }
        return maxP;
    }
}
