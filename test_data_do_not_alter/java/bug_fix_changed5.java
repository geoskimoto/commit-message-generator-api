import java.util.Arrays;

public class StatsCalculatorChanged {
    private double[] numbers;

    public StatsCalculatorChanged(double[] numbers) {
        if (numbers == null) {
            throw new IllegalArgumentException("Input must not be null");
        }
        this.numbers = numbers;
    }

    public double getAverage() {
        if (numbers.length == 0) {
            throw new IllegalArgumentException("Cannot calculate average of an empty array");
        }
        double sum = 0;
        for (double num : numbers) {
            sum += num;
        }
        return sum / numbers.length;
    }

    public double getMedian() {
        if (numbers.length == 0) {
            throw new IllegalArgumentException("Cannot calculate median of an empty array");
        }
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
        StatsCalculatorChanged stats1 = new StatsCalculatorChanged(data1);
        System.out.println(stats1.getAverage());
        System.out.println(stats1.getMedian());

        double[] data2 = {};
        StatsCalculatorChanged stats2 = new StatsCalculatorChanged(data2);
        try {
            System.out.println(stats2.getAverage());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        try {
            System.out.println(stats2.getMedian());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
