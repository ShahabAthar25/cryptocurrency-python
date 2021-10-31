import React from "react";

import "./Header.css";

function Header() {
  return (
    <div className="header">
      <div className="headerLeft">
        <h1>CryptoMyScene</h1>
      </div>
      <div className="headerCenter">
        <ul>
          <li>
            <a href="#">Buy CryptoMyScene</a>
          </li>
          <li>
            <a href="#">Sell CryptoMyScene</a>
          </li>
        </ul>
      </div>
      <div className="headerRight">
        <h2>
          <a href="#">Login</a>
        </h2>
        <h2>
          <a href="#">SignUp</a>
        </h2>
      </div>
    </div>
  );
}

export default Header;
