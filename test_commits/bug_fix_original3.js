async function fetchUserData(userId) {
  const response = await fetch(`/api/user/${userId}`);
  return response.json();
}
