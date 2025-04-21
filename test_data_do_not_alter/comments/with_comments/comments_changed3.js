function isEven(n) {
    // Ensure input is a number
    if (typeof n !== 'number') {
        throw new Error("Input must be a number");
    }
    // Check if even
    return n % 2 === 0;
}