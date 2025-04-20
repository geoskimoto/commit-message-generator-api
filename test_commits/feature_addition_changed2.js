function getUserFullName(user) {
  return `${user.firstName} ${user.lastName}`;
}

function getUserInitials(user) {
  return `${user.firstName[0]}.${user.lastName[0]}.`;
}
