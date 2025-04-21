function calculateSum(arr) {
    let sum = 0;
    let validCount = 0;
    // Loop through each item in the array
    for (let i = 0; i < arr.length; i++) {
        // Only sum if the item is a number
        if (typeof arr[i] === 'number') {
            sum += arr[i];
            validCount++; // Count valid numbers
        }
    }
    // Return both total and average
    return {
        total: sum,
        average: validCount > 0 ? sum / validCount : 0
    };
}
