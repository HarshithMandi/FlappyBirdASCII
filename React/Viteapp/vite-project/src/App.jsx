import './App.css'

import Home from './components/Home'
import AddStudent from './components/AddStudent'
import StudentList from './components/StudentList'
import FeedbackForm from './components/FeedbackForm'
import About from './components/About'
import Contact from './components/Contact'

import { useEffect, useMemo, useState } from 'react'
import { Routes, Route, Link } from 'react-router-dom'

import db from './data/db.json'
import { createStudent, listStudents } from './api/students'

const STUDENTS_STORAGE_KEY = 'sms.students'

function App() {
  const seedStudents = useMemo(() => {
    return Array.isArray(db?.students) ? db.students : []
  }, [])

  const [students, setStudents] = useState([])

  useEffect(() => {
    const load = async () => {
      try {
        const apiStudents = await listStudents()
        if (Array.isArray(apiStudents)) {
          setStudents(apiStudents)
          return
        }
      } catch {
        // ignore and fall back
      }

      try {
        const raw = localStorage.getItem(STUDENTS_STORAGE_KEY)
        if (raw) {
          const parsed = JSON.parse(raw)
          if (Array.isArray(parsed)) {
            setStudents(parsed)
            return
          }
        }
      } catch {
        // ignore and fall back
      }

      setStudents(seedStudents)
    }

    load()
  }, [seedStudents])

  useEffect(() => {
    try {
      localStorage.setItem(STUDENTS_STORAGE_KEY, JSON.stringify(students))
    } catch {
      // ignore
    }
  }, [students])

  const addStudent = async (student) => {
    try {
      const saved = await createStudent(student)
      setStudents((current) => [saved, ...current])
      return saved
    } catch {
      const fallback = { ...student, id: crypto.randomUUID() }
      setStudents((current) => [fallback, ...current])
      return fallback
    }
  }

  return (
    <div className="app">
      <header className="header">
        <h1 className="title">Online Student Management System</h1>
        <p className="subtitle">Add students, view the list, and send feedback.</p>

        <nav className="nav">
          <Link to="/">Home</Link>
          <Link to="/add-student">Add Student</Link>
          <Link to="/students">Student List</Link>
          <Link to="/feedback">Feedback</Link>
          <Link to="/about">About</Link>
          <Link to="/contact">Contact</Link>
        </nav>
      </header>

      <main className="main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/add-student" element={<AddStudent onAddStudent={addStudent} />} />
          <Route path="/students" element={<StudentList students={students} />} />
          <Route path="/feedback" element={<FeedbackForm />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
