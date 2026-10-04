import { useEffect, useState } from "react";
import { useAuth } from "@/context/AuthContext";
import api from "@/services/api";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

export default function AdminDashboard() {
  const { user, logout } = useAuth();
  const [students, setStudents] = useState<any[]>([]);

  useEffect(() => {
    api.get("/admin/students/").then((res) => setStudents(res.data));
  }, []);

  return (
    <>
      <Navbar />

      <div className="min-h-screen bg-slate-100 p-8">
        <div className="max-w-5xl mx-auto">
          <div className="flex justify-between items-center mb-8">
            <h1 className="text-3xl font-bold text-slate-800">
              Admin Dashboard
            </h1>
            <button
              onClick={logout}
              className="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700"
            >
              Logout
            </button>
          </div>

          <p className="text-slate-600 mb-6">Welcome, {user?.username}</p>

          <h2 className="text-xl font-semibold text-slate-700 mb-4">
            Students
          </h2>

          <ul className="bg-white rounded-lg shadow divide-y">
            {students.map((s) => (
              <li key={s.id} className="p-4">
                {s.full_name} — {s.student_id}
              </li>
            ))}
          </ul>
        </div>
      </div>

      <Footer />
    </>
  );
}