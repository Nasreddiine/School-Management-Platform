import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api",
  withCredentials: true, // sends cookies with every request
});

// CSRF token for non-GET requests
api.defaults.xsrfCookieName = "csrftoken";
api.defaults.xsrfHeaderName = "X-CSRFToken";

// Auto-refresh on 401
api.interceptors.response.use(
  (res) => res,
  async (error) => {
    const original = error.config;
    const status = error.response?.status;

    const isAuthCheck =
      original.url.includes("/auth/me/") ||
      original.url.includes("/auth/refresh/") ||
      original.url.includes("/auth/login/");

    if (status === 401 && !original._retry && !isAuthCheck) {
      original._retry = true;
      try {
        await api.post("/auth/refresh/");
        return api(original);
      } catch {
        if (window.location.pathname !== "/login") {
          window.location.href = "/login";
        }
        return Promise.reject(error);
      }
    }

    return Promise.reject(error);
  }
);

export default api;