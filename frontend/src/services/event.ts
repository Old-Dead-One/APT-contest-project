// event.js

const API_BASE_URL = "./backend/main_admin";

export const fetchEvents = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/events/`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching events:", error);
    throw error;
  }
};

export const fetchEventById = async (eventId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/events/${eventId}`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching event:", error);
    throw error;
  }
};

export const createEvent = async (event) => {
  try {
    const response = await fetch(`${API_BASE_URL}/events/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(event),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error creating event:", error);
    throw error;
  }
};

export const updateEvent = async (event) => {
  try {
    const response = await fetch(`${API_BASE_URL}/events/${event.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(event),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error updating event:", error);
    throw error;
  }
};

export const deleteEvent = async (eventId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/events/${eventId}`, {
      method: "DELETE",
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
  } catch (error) {
    console.error("Error deleting event:", error);
    throw error;
  }
};
