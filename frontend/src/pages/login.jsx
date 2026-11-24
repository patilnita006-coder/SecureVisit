
import React, { useState } from "react";
import "./Login.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();

    setMessage(
      "Backend authentication will be connected soon."
    );
  };

  return (
    <div className="login-page">

      <div className="login-brand">
        <div className="brand-icon">S</div>
        <h2>SECURE<span>VISIT</span></h2>
        <p>VISITOR CAMERA SECURITY SYSTEM</p>
      </div>

      <div className="login-card">

        <div className="login-shield">♜</div>

        <h1>Welcome Back</h1>

        <p className="login-subtitle">
          Sign in to your security dashboard
        </p>

        <form onSubmit={handleLogin}>

          <label>Email Address</label>
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <label>Password</label>
          <input
            type="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <button type="submit">
            SIGN IN →
          </button>

        </form>

        {message && (
          <p className="login-message">{message}</p>
        )}

        <div className="login-footer">
          Protected by SecureVisit Security
        </div>

      </div>

      <p className="login-copyright">
        © 2026 SecureVisit. All Rights Reserved.
      </p>

    </div>
  );
}

export default Login;
