import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Header from "../src/components/global/Header"
import Home from "../src/pages/Home"
import './App.css'

const App: React.FC = () => {
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  )
}

export default App