import { useMemo, useState } from 'react'
import './App.css'
import { useLocalStorageState } from './hooks/useLocalStorageState'
import type { Note, NoteId } from './types'
import { createNote, formatDateTime } from './types'

function App() {
  const [notes, setNotes] = useLocalStorageState<Note[]>('notes.v1', [])
  const [selectedId, setSelectedId] = useState<NoteId | null>(notes[0]?.id ?? null)

  const selectedNote = useMemo(
    () => notes.find((n) => n.id === selectedId) ?? null,
    [notes, selectedId],
  )

  function addNote() {
    const note = createNote({ title: 'Untitled', body: '' })
    setNotes((prev) => [note, ...prev])
    setSelectedId(note.id)
  }

  function deleteSelectedNote() {
    if (!selectedId) return
    const remaining = notes.filter((n) => n.id !== selectedId)
    setNotes(remaining)
    setSelectedId(remaining[0]?.id ?? null)
  }

  function updateSelectedNote(patch: Partial<Pick<Note, 'title' | 'body'>>) {
    if (!selectedId) return

    setNotes((prev) =>
      prev.map((n) => {
        if (n.id !== selectedId) return n

        const updated: Note = {
          ...n,
          title: patch.title ?? n.title,
          body: patch.body ?? n.body,
          updatedAt: Date.now(),
        }

        return updated
      }),
    )
  }

  return (
    <div className="app">
      <header className="row">
        <div>
          <h1 style={{ margin: 0 }}>Notes</h1>
          <div className="muted">React + TypeScript + localStorage</div>
        </div>
        <div className="buttonRow">
          <button type="button" onClick={addNote}>
            New note
          </button>
          <button type="button" onClick={deleteSelectedNote} disabled={!selectedId}>
            Delete
          </button>
        </div>
      </header>

      <main className="panes">
        <section className="panel stack" aria-label="Notes list">
          {notes.length === 0 ? (
            <div className="muted">No notes yet. Click “New note”.</div>
          ) : (
            <ul className="list">
              {notes.map((n) => {
                const isSelected = n.id === selectedId
                return (
                  <li key={n.id}>
                    <button
                      type="button"
                      className="listItem"
                      onClick={() => setSelectedId(n.id)}
                      aria-current={isSelected ? 'true' : undefined}
                    >
                      <div style={{ fontWeight: 600 }}>{n.title || 'Untitled'}</div>
                      <div className="muted">Updated: {formatDateTime(n.updatedAt)}</div>
                    </button>
                  </li>
                )
              })}
            </ul>
          )}
        </section>

        <section className="panel stack" aria-label="Editor">
          {selectedNote == null ? (
            <div className="muted">Select a note to edit.</div>
          ) : (
            <>
              <label className="stack">
                <div className="muted">Title</div>
                <input
                  className="input"
                  value={selectedNote.title}
                  onChange={(e) => updateSelectedNote({ title: e.target.value })}
                  placeholder="Untitled"
                />
              </label>
              <label className="stack">
                <div className="muted">Body</div>
                <textarea
                  className="textarea"
                  value={selectedNote.body}
                  onChange={(e) => updateSelectedNote({ body: e.target.value })}
                  placeholder="Write something…"
                />
              </label>
              <div className="muted">
                Created: {formatDateTime(selectedNote.createdAt)} · Updated:{' '}
                {formatDateTime(selectedNote.updatedAt)}
              </div>
            </>
          )}
        </section>
      </main>
    </div>
  )
}

export default App
