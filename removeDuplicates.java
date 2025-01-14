
    public static int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int pointeur = 0;
        for (int i = 0; i < nums.length; i++) { 
            int index = -1;
            if (nums[i] != nums[pointeur]) {
                if (index != -1) {
                    nums[index] = nums[i];
                }
                index = i;
            }
        }
        return 0; 
    }
