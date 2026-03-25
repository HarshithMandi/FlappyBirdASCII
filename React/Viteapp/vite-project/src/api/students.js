const DEFAULT_API_BASE_URL = 'http://localhost:3001'

const API_BASE_URL =
  (import.meta?.env && import.meta.env.VITE_API_BASE_URL) || DEFAULT_API_BASE_URL

async function fetchJson(url, options) {
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...(options?.headers ?? {}),
    },
    ...options,
  })

  if (!response.ok) {
    const text = await response.text().catch(() => '')
    throw new Error(text || `Request failed: ${response.status}`)
  }

  return response.json()
}

export async function listStudents() {
  return fetchJson(`${API_BASE_URL}/students`)
}

export async function createStudent(student) {
  return fetchJson(`${API_BASE_URL}/students`, {
    method: 'POST',
    body: JSON.stringify(student),
  })
}
