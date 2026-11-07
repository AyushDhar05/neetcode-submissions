class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] freq_s1 = new int[26];
        for(int i = 0; i < s1.length(); i++) {
            freq_s1[s1.charAt(i) - 'a'] ++;
        }

        int start = 0;
        int[] freq_s2 = new int[26];
        for(int i = 0; i < s2.length(); i++) {
            freq_s2[s2.charAt(i) - 'a'] ++;
            if(i - start + 1 > s1.length()) {
                freq_s2[s2.charAt(start) - 'a'] --;
                start ++;
            }
            if(Arrays.equals(freq_s1, freq_s2)) return true;
        }

        return false;
    }
}
