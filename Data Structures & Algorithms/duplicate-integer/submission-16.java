class Solution {
    public boolean hasDuplicate(int[] nums) {
        // set of seen nums

        Set<Integer> seen = new HashSet<>();

        // iterate, check if in seen, then add
        for (int num : nums) {
            if (!seen.add(num))
                return true;
        }

        return false;
    }
}