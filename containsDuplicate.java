import java.util.HashSet;

class containsDuplicate{
    public static void main(String[] args) {
        int[] nums={1,2,3,4};
        boolean b=hasDuplicate(nums);
        
        System.out.println(b);
    }

    public static boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hash = new HashSet<>();
            for(int i=0;i<nums.length;i++){
                //The elements already exists 
               if(!hash.add(nums[i])){
                    return true;
               }
            }
            return false;
        }
}