async function fetchUserData(userId) {
  try {
      const response = await fetch(`/api/user/${userId}`);
      if (!response.ok) {
          throw new Error("Network response was not ok");
      }
      return await response.json();
  } catch (error) {
      console.error("Failed to fetch user data:", error);
      return null;
  }
}
