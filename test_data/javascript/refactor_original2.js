function getUserRole(user) {
  if (user.role === 'admin') {
      return 'Administrator';
  } else if (user.role === 'user') {
      return 'Regular User';
  } else {
      return 'Unknown';
  }
}
