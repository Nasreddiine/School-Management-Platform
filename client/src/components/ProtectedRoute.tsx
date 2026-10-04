import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

type Props = {
  role: "admin" | "professor" | "student";
  children: React.ReactNode;
};

export default function ProtectedRoute({ role, children }: Props) {
  const { user, loading } = useAuth();

  if (loading) return <p>Loading...</p>;
  if (!user) return <Navigate to="/login" replace />;
  if (user.role !== role) return <Navigate to={`/${user.role}`} replace />;

  return <>{children}</>;
}