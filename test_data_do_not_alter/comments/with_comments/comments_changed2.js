function sumArray(arr) {
    // Check if input is an array
    if (!Array.isArray(arr)) return 0;
    // Use reduce to sum elements
    return arr.reduce((a, b) => a + b, 0);
}