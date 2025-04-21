class StatsCalculatorChanged:
    def __init__(self, numbers):
        if numbers is None:
            raise ValueError("Input must not be None")
        self.numbers = numbers

    def get_average(self):
        if not self.numbers:
            raise ValueError("Cannot calculate average of an empty list")
        total = sum(self.numbers)
        return total / len(self.numbers)

    def get_median(self):
        if not self.numbers:
            raise ValueError("Cannot calculate median of an empty list")
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        return sorted_nums[mid]


if __name__ == "__main__":
    data1 = [10, 20, 30, 40]
    stats1 = StatsCalculatorChanged(data1)
    print(stats1.get_average())
    print(stats1.get_median())

    data2 = []
    stats2 = StatsCalculatorChanged(data2)
    try:
        print(stats2.get_average())
    except Exception as e:
        print(e)

    try:
        print(stats2.get_median())
    except Exception as e:
        print(e)
