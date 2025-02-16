import NavBar from "./components/navbar/NavBar";
import Home from "./pages/home/Home";
import Settings from "./pages/settings/Settings";
import Single from "./pages/single/Single";
import Write from "./pages/write/Write";
import Login from "./pages/login/Login";
import Register from "./pages/register/Register";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Map from "./pages/Map/Map";

function App() {
  const user = false;
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/write" element={user ? <Write/> : <Register/>} />
        <Route path="/post/:postId" element={<Single/>} />
        <Route path="/settings" element={user ? <Settings/> : <Register/>} />
        <Route path="/register" element={user ? <Home/> : <Register/>} />
        <Route path="/login" element={user ? <Home/> : <Login />} />
        <Route path="/map" element={<Map />} />
      </Routes>
    </Router>
  );
}

export default App;
