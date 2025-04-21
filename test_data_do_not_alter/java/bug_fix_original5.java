import java.util.Arrays;

public class StatsCalculatorOriginal {
    private double[] numbers;

    public StatsCalculatorOriginal(double[] numbers) {
        this.numbers = numbers;
    }

    public double getAverage() {
        double sum = 0;
        for (double num : numbers) {
            sum += num;
        }
        return sum / numbers.length;
    }

    public double getMedian() {
        double[] sorted = Arrays.copyOf(numbers, numbers.length);
        Arrays.sort(sorted);
        int mid = sorted.length / 2;
        if (sorted.length % 2 == 0) {
            return (sorted[mid - 1] + sorted[mid]) / 2;
        }
        return sorted[mid];
    }

    public static void main(String[] args) {
        double[] data1 = {10, 20, 30, 40};
        StatsCalculatorOriginal stats1 = new StatsCalculatorOriginal(data1);
        System.out.println(stats1.getAverage());
        System.out.println(stats1.getMedian());

        double[] data2 = {};
        StatsCalculatorOriginal stats2 = new StatsCalculatorOriginal(data2);
        System.out.println(stats2.getAverage()); // Will cause divide by zero
        System.out.println(stats2.getMedian());  // Will cause index error
    }
}
