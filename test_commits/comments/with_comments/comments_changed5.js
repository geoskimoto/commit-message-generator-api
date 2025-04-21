function reverseString(str) {
    // Validate input
    if (typeof str !== 'string') return '';
    // Split string into characters, reverse and join
    return str.split('').reverse().join('');
}