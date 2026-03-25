import { useState } from 'react'

export default function FeedbackForm() {
  const [name, setName] = useState('')
  const [message, setMessage] = useState('')
  const [submitted, setSubmitted] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault()

    if (!name.trim() || !message.trim()) {
      return
    }

    setSubmitted(true)
    setName('')
    setMessage('')
  }

  return (
    <section className="card">
      <h2 className="cardTitle">Feedback Form</h2>
      <p className="muted">Tell us what you think about the system.</p>

      {submitted ? <p className="success">Thanks! Your feedback was submitted.</p> : null}

      <form className="form" onSubmit={handleSubmit}>
        <label className="field">
          <span className="label">Your name</span>
          <input
            className="input"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="e.g. Rahul"
          />
        </label>

        <label className="field">
          <span className="label">Message</span>
          <textarea
            className="input textarea"
            rows={5}
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Write your feedback..."
          />
        </label>

        <button className="button" type="submit">
          Submit Feedback
        </button>
      </form>
    </section>
  )
}
