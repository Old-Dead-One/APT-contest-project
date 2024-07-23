// player.js

const API_BASE_URL = "./backend/main_admin";

export const fetchPlayers = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/players/`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching players:", error);
    throw error;
  }
};

export const fetchPlayerByChapter = async (playerId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/players/chapter${playerId}`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching player:", error);
    throw error;
  }
};

export const createPlayer = async (player) => {
  try {
    const response = await fetch(`${API_BASE_URL}/players/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(player),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error creating player:", error);
    throw error;
  }
};

export const updatePlayer = async (player) => {
  try {
    const response = await fetch(`${API_BASE_URL}/players/${player.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(player),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error updating player:", error);
    throw error;
  }
};

export const deletePlayer = async (playerId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/players/${playerId}`, {
      method: "DELETE",
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
  } catch (error) {
    console.error("Error deleting player:", error);
    throw error;
  }
};
