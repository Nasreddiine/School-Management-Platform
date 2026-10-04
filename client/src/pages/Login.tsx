import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Footer from "@/components/Footer";
import Navbar from "@/components/Navbar";
import { useAuth } from "@/context/AuthContext";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    try {
      const user = await login(username, password);
      navigate(`/${user.role}`);
    } catch (err: any) {
      setError(err.response?.data?.detail || "Login failed");
    }
  };

  return (
    <>
      <Navbar />

      <div className="min-h-screen bg-slate-400 flex items-center justify-center">
        <div className="w-full max-w-md bg-white border border-slate-500 rounded-lg p-8 shadow-md">

          <h1 className="text-3xl font-bold text-center text-slate-800 mb-8">
            Login Portal
          </h1>

          <form className="space-y-5" onSubmit={handleSubmit}>
            <div>
              <label className="block text-slate-700 font-medium mb-2">
                Username
              </label>

              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter your username"
                className="w-full border border-slate-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-slate-500"
              />
            </div>

            <div>
              <label className="block text-slate-700 font-medium mb-2">
                Password
              </label>

              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter your password"
                className="w-full border border-slate-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-slate-500"
              />
            </div>

            {error && (
              <p className="text-red-600 text-sm text-center">{error}</p>
            )}

            <button
              type="submit"
              className="w-full bg-slate-700 text-white py-2 rounded-md hover:bg-slate-800 transition"
            >
              Log In
            </button>
          </form>

        </div>
      </div>

      <Footer />
    </>
  );
}

export default Login;