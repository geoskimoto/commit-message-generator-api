function isEven(n) {
    if (typeof n !== 'number') {
        throw new Error("Input must be a number");
    }
    return n % 2 === 0;
}