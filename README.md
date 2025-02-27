# Transport Management System

This is a containerized application for managing transport orders. The project consists of a Django backend and a Nuxt frontend, both running in Docker containers via Docker Compose.

## Technologies Used

- **Django 3.2** – Robust and scalable backend framework.
- **Nuxt 3** – Modern Vue.js framework for a reactive, SEO-friendly frontend.
- **PostgreSQL** – Database used for persistent data storage.
- **Docker & Docker Compose** – Containerization for consistency across environments. Multistage builds are used to keep production images lean
## Getting Started

To build and run the project from the root directory, use:

```bash
cd swida
docker-compose up -d --build
```
**Now is your transport management app available on http://locahost:3000/orders**

## Configuration
The Nuxt app uses runtime configuration for the API base URL. In nuxt.config.ts, the configuration is set as follows:
```
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_ENV_API_URL || 'http://localhost:8000/api'
    }
  }
})
```
In Docker Compose, the environment variable is set to point to the backend:
```yaml
services:
  nuxt-app:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NUXT_ENV_API_URL=http://web:8000/api
    depends_on:
      - web
```

## Architectural Decisions: DI & Service Layer
Instead of relying solely on Django’s generic class-based views, this project uses a dependency injection (DI) and service layer approach for handling business logic. Here’s why this approach is preferred to me:
- Separation of Concerns:
The view layer handles only HTTP request/response logic while the service layer encapsulates business logic. This separation makes the code easier to understand and maintain.

- Testability:
By injecting services into views, you can easily mock or replace them during testing, allowing for unit testing of business logic without full-stack dependencies.

- Flexibility & Reusability:
The service layer can be reused across different parts of the application or even across projects, avoiding code duplication.

- Maintainability:
As the project grows, keeping business logic separate from view logic makes it simpler to modify, extend, or refactor the application.

I know that using generic views might be even faster and leverage the full potential of the Django framework, but I aimed to implement this solution as if I were writing code for a production-ready application. With possibility to grow :-)
