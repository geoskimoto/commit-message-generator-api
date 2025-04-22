class StatsCalculator {
    constructor(numbers) {
        this.numbers = numbers;
    }

    getAverage() {
        const sum = this.numbers.reduce((a, b) => a + b);
        return sum / this.numbers.length;
    }

    getMedian() {
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
console.log(stats2.getAverage()); 
console.log(stats2.getMedian());  
