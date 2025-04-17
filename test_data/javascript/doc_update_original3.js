function encrypt(text, key) {
  return text.split('').map(char => String.fromCharCode(char.charCodeAt(0) + key)).join('');
}
