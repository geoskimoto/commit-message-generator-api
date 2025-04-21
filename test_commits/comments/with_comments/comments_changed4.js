function findMax(arr) {
    // Return null for empty arrays
    if (!arr.length) return null;
    // Use spread operator to find max
    return Math.max(...arr);
}