import { createContext, useContext, useEffect, useState } from "react";
import api from "../services/api";

type User = { username: string; role: string };

type AuthContextType = {
  user: User | null;
  loading: boolean;
  login: (username: string, password: string) => Promise<User>;
  logout: () => Promise<void>;
};

const AuthContext = createContext<AuthContextType>(null!);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);   // ← fixed
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/auth/me/")
      .then((res) => setUser(res.data))
      .catch(() => setUser(null))
      .finally(() => setLoading(false));
  }, []);

  const login = async (username: string, password: string): Promise<User> => {
    const res = await api.post("/auth/login/", { username, password });
    const u: User = { username: res.data.username, role: res.data.role };
    setUser(u);
    return u;
  };

  const logout = async () => {
    await api.post("/auth/logout/");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);