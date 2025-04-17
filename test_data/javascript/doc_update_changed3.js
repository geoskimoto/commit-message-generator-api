/**
 * Encrypts a string using a basic Caesar cipher-like algorithm.
 * @param {string} text - The text to encrypt.
 * @param {number} key - The key (shift) for the encryption.
 * @returns {string} The encrypted string.
 */
function encrypt(text, key) {
  return text.split('').map(char => String.fromCharCode(char.charCodeAt(0) + key)).join('');
}
