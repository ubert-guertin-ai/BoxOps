import { NavLink } from "react-router-dom";

export default function NavBar() {
  return (
    <nav>
      <h2>My brand</h2>
      <div>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/about">About</NavLink>
        <NavLink to="/contact">Contact</NavLink>
      </div>
    </nav>
  )
}
