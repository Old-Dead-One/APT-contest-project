// chapterService.js

const API_BASE_URL = "./backend/main_admin";

export const fetchChapters = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/chapters/`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching chapters:", error);
    throw error;
  }
};

export const fetchChapterById = async (chapterId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chapters/${chapterId}`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching chapter:", error);
    throw error;
  }
};

export const createChapter = async (chapter) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chapters/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(chapter),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error creating chapter:", error);
    throw error;
  }
};

export const updateChapter = async (chapter) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chapters/${chapter.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(chapter),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error updating chapter:", error);
    throw error;
  }
};

export const deleteChapter = async (chapterId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chapters/${chapterId}`, {
      method: "DELETE",
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
  } catch (error) {
    console.error("Error deleting chapter:", error);
    throw error;
  }
};
