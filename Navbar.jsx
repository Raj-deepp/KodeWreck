import React from "react";
import { navigation } from "../constants";
import "../Styles/Navbar.css";

const Navbar = () => {
  return (
    <div>
      <nav className="navbar">
        <div className="navbar-inner">
          {navigation.map((item) => (
            <a key={item.id} href={item.url} className="navbar-link">
              {item.title}
            </a>
          ))}
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
