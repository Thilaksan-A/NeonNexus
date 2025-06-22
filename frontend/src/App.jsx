import { useState, useEffect} from 'react'
import './App.css'
import axios from "axios"

function App() {
  const [users, setUsers] = useState([]);

  const fetchAPI = async() => {
    const response = await axios.get("https://neonnexus.onrender.com/api/user/get_users")
    console.log(response.data);
    setUsers(response.data)
  }

  useEffect(() => {
    fetchAPI()
  }, [])
  return (
    <>
      <h1>Crypto App</h1>
      <div className="card">
        <p>Below is list of users from db</p>
        <p>To test send a post request to 
          https://neonnexus.onrender.com/api/user/create_user with "name", "email" and "password"
        </p>
        <p>Name:______ Email______</p>
        { users.map((user, index) => (
          <div key={index}>{user.name} {user.email}</div>
        ))}
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
