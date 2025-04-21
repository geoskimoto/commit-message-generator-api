const roleMap = {
  admin: 'Administrator',
  user: 'Regular User'
};

function getUserRole(user) {
  return roleMap[user.role] || 'Unknown';
}
