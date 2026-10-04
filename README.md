# School Management Platform

A full-stack school management platform with role-based dashboards for **administrators**, **professors**, and **students**.

## Tech Stack

**Backend**
- Django
- Django REST Framework
- SimpleJWT (JWT via httpOnly cookies)
- django-cors-headers
- SQLite

**Frontend**
- React 19
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Axios

## Features

- Custom user model with role field (`admin` / `professor` / `student`)
- JWT authentication stored in **httpOnly cookies** (protected against XSS)
- Automatic token refresh on 401 responses
- Role-based access control enforced on both frontend and backend
- Separate dashboards per role:
  - **Admin** — view all students
  - **Professor** — view their own courses
  - **Student** — view their enrolled courses
- Protected routes on the frontend that redirect users based on their role
- Backend permission classes (`IsAdmin`, `IsProfessor`, `IsStudent`)

