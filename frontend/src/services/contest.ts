// contests.js

const API_BASE_URL = "./backend/main_admin";

export const fetchContests = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/contests/`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching contests:", error);
    throw error;
  }
};

export const fetchContestById = async (contestId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/contests/${contestId}`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching contest:", error);
    throw error;
  }
};

export const createContest = async (contest) => {
  try {
    const response = await fetch(`${API_BASE_URL}/contests/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(contest),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error creating contest:", error);
    throw error;
  }
};

export const updateContest = async (contest) => {
  try {
    const response = await fetch(`${API_BASE_URL}/contests/${contest.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(contest),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error updating contest:", error);
    throw error;
  }
};

export const deleteContest = async (contestId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/contests/${contestId}`, {
      method: "DELETE",
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error deleting contest:", error);
    throw error;
  }
};
