class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> state = new HashSet<>();
        int start = 0;

        int res = 0;
        for(int i = 0; i < s.length(); i++) {
            while (state.contains(s.charAt(i))) {
                state.remove(s.charAt(start));
                start++;

            }
            // state.put(s.charAt(i), i);
            state.add(s.charAt(i));
            res = Math.max(res, i - start + 1);
        }
        return res;
    }
}
