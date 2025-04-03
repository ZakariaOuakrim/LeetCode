import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            map.put(nums[i], i);
        }
        int diff;
        for(int i =0;i<nums.length;i++){
            diff=target-nums[i];
            if(map.containsValue(diff)){
                indices[0]=i;
                indices[1]=map.get(diff);
                return indices; 
            }
        }

        return null;
    }
    public static void main(String[] args) {
        
    }   
}
