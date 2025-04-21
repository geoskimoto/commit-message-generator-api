function sumArray(arr) {
    if (!Array.isArray(arr)) return 0;
    return arr.reduce((a, b) => a + b, 0);
}