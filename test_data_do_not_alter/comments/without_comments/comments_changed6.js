function calculateSum(arr) {
    let sum = 0;
    let validCount = 0;
    for (let i = 0; i < arr.length; i++) {
        if (typeof arr[i] === 'number') {
            sum += arr[i];
            validCount++;
        }
    }
    return {
        total: sum,
        average: validCount > 0 ? sum / validCount : 0
    };
}
