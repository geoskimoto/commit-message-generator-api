class StatsCalculatorOriginal:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_average(self):
        total = sum(self.numbers)
        return total / len(self.numbers)

    def get_median(self):
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        return sorted_nums[mid]


if __name__ == "__main__":
    data1 = [10, 20, 30, 40]
    stats1 = StatsCalculatorOriginal(data1)
    print(stats1.get_average())
    print(stats1.get_median())

    data2 = []
    stats2 = StatsCalculatorOriginal(data2)
    print(stats2.get_average())
    print(stats2.get_median())
