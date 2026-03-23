export type NoteId = string

export type Note = {
  id: NoteId
  title: string
  body: string
  createdAt: number
  updatedAt: number
}

export function createNote(partial?: Partial<Pick<Note, 'title' | 'body'>>): Note {
  const now = Date.now()

  return {
    id: createId(),
    title: partial?.title?.trim() ?? '',
    body: partial?.body?.trim() ?? '',
    createdAt: now,
    updatedAt: now,
  }
}

export function formatDateTime(timestampMs: number): string {
  return new Date(timestampMs).toLocaleString()
}

function createId(): string {
  if (typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function') {
    return crypto.randomUUID()
  }

  return `${Date.now()}-${Math.random().toString(16).slice(2)}`
}
