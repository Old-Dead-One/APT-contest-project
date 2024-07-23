const BASE_URL_API = "./main_admin.py";

interface Chapter {
  chapter_id: number;
  name: string;
  location: string;
}

async function fetchChapters(): Promise<Chapter[]> {
  const response = await fetch(`${BASE_URL_API}/chapters/`);
  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }
  return response.json();
}

async function fetchChapterById(chapter_id: number): Promise<Chapter[]> {
  const response = await fetch(`${BASE_URL_API}/chapters/${chapter_id}`);
  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }
  return response.json();
}

async function createChapter(chapter: Chapter): Promise<Chapter> {
  const response = await fetch(`${BASE_URL_API}/chapters/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(chapter)
  });
  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }
  return response.json();
}

async function updateChapter(chapter_id: number, chapter: Chapter): Promise<Chapter> {
  const response = await fetch(`${BASE_URL_API}/chapters/${chapter_id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(chapter)
  });
  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }
  return response.json();
}

async function deleteChapter(chapter_id: number): Promise<void> {
  const response = await fetch(`${BASE_URL_API}/chapters/${chapter_id}`, {
    method: "DELETE"
  });
  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }
}
