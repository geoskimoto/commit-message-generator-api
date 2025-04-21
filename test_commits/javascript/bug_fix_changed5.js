class StatsCalculator {
    constructor(numbers) {
        if (!Array.isArray(numbers)) {
            throw new TypeError("Input must be an array");
        }
        this.numbers = numbers;
    }

    getAverage() {
        if (this.numbers.length === 0) {
            throw new Error("Cannot calculate average of an empty array");
        }
        const sum = this.numbers.reduce((a, b) => a + b, 0);
        return sum / this.numbers.length;
    }

    getMedian() {
        if (this.numbers.length === 0) {
            throw new Error("Cannot calculate median of an empty array");
        }
        const sorted = [...this.numbers].sort((a, b) => a - b);
        const mid = Math.floor(sorted.length / 2);
        if (sorted.length % 2 === 0) {
            return (sorted[mid - 1] + sorted[mid]) / 2;
        }
        return sorted[mid];
    }
}

const data1 = [10, 20, 30, 40];
const stats1 = new StatsCalculator(data1);
console.log(stats1.getAverage());
console.log(stats1.getMedian());

const data2 = [];
const stats2 = new StatsCalculator(data2);
try {
    console.log(stats2.getAverage());
} catch (e) {
    console.error(e.message);
}
try {
    console.log(stats2.getMedian());
} catch (e) {
    console.error(e.message);
}
