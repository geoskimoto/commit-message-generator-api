public class MathUtils {
    public static double average(int[] nums) {
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        return sum / nums.length;
    }
}
