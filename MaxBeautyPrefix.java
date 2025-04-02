import java.util.Arrays;

class MaxBeautyPrefix{
    public static long getMaxBeauty(int[] arr){
        int n = arr.length;
        Arrays.sort(arr);  // First sort the original array
        
        // Create the arranged array (alternating small and large elements)
        int[] arranged = new int[n];
        int left = 0, right = n - 1;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                arranged[i] = arr[left++];  // Take from left (smaller elements)
            } else {
                arranged[i] = arr[right--]; // Take from right (larger elements)
            }
        }
        
        // Create the prefix sum (psum) array
        long[] psum = new long[n + 1];
        for (int i = 0; i < n; i++) {
            psum[i + 1] = psum[i] + arranged[i];
        }
        
        // Calculate max beauty based on psum
        if (n % 2 == 1) {
            // For odd length: sum of elements at even indices (0-based)
            long sum = 0;
            for (int i = 0; i < n; i += 2) {
                sum += arranged[i];
            }
            return sum;
        } else {
            // For even length: negative sum of first half
            return -psum[n / 2];
        }
    }

    public static void main(String[] args) {
        int[] arr={3,4,5,1,1};
        long d = getMaxBeauty(arr);
        System.out.println(d);
    }
}