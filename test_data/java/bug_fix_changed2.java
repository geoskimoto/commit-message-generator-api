public class MathUtils {
    public static double average(int[] nums) {
        if (nums.length == 0) return 0;
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        return (double) sum / nums.length;
    }
}
