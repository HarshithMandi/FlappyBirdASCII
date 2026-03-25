import { useMemo, useState } from 'react'
import { useNavigate } from 'react-router-dom'

export default function AddStudent({ onAddStudent }) {
  const navigate = useNavigate()
  const [name, setName] = useState('')
  const [rollNumber, setRollNumber] = useState('')
  const [department, setDepartment] = useState('')
  const [email, setEmail] = useState('')
  const [saving, setSaving] = useState(false)

  const departmentOptions = useMemo(
    () => ['HR', 'Engineering', 'Sales', 'Finance', 'Marketing'],
    []
  )

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!name.trim() || !rollNumber.trim() || !department.trim() || !email.trim()) {
      return
    }

    setSaving(true)
    try {
      await onAddStudent?.({
        name: name.trim(),
        rollNumber: rollNumber.trim(),
        department: department.trim(),
        email: email.trim(),
      })
      navigate('/students')
    } finally {
      setSaving(false)
    }

    setName('')
    setRollNumber('')
    setDepartment('')
    setEmail('')
  }

  return (
    <section className="card">
      <h2 className="cardTitle">Add Student</h2>
      <form className="form" onSubmit={handleSubmit}>
        <label className="field">
          <span className="label">Full name</span>
          <input
            className="input"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="e.g. Asha Kumar"
            autoComplete="name"
          />
        </label>

        <label className="field">
          <span className="label">Roll number</span>
          <input
            className="input"
            value={rollNumber}
            onChange={(e) => setRollNumber(e.target.value)}
            placeholder="e.g. 23CS102"
          />
        </label>

        <label className="field">
          <span className="label">Department</span>
          <select
            className="input"
            value={department}
            onChange={(e) => setDepartment(e.target.value)}
          >
            <option value="">Select a department</option>
            {departmentOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

        <label className="field">
          <span className="label">Email</span>
          <input
            className="input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="e.g. asha@example.com"
            autoComplete="email"
          />
        </label>

        <button className="button" type="submit" disabled={saving}>
          {saving ? 'Saving…' : 'Save Student'}
        </button>
      </form>
    </section>
  )
}
