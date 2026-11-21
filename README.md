# TV Show & Season Tracker (MVP)

A lightweight Flask web application for tracking TV shows, watch status, upcoming releases, and personal ratings.

## MVP Features
- **View Shows (`/`):** Displays tracked shows as cards with status, optional next release notes, and optional ratings.
- **Add Shows (`/add`):** Add a show with a title, status (`Watching`, `On Break / Returning Soon`, `Want to Watch`, `Completed`), optional next release note, and optional rating (`1`–`5`).
- **Delete Shows (`/delete/<id>`):** Remove shows from the tracker.

## Known MVP Limitations & Roadmap
- **Data Persistence:** Uses a local SQLite database (`shows.db`) inside the container, meaning stored data is not persisted across container restarts or new Cloud Run deployments. Persistent cloud storage (e.g., Cloud SQL / PostgreSQL) is planned for a future sprint.
- **User Accounts:** Authentication (sign up, login, logout) and per-user show lists are slated for a future iteration.
- **AI Features:** Future updates plan to add user-facing AI features such as personalized show recommendations and season update tracking.

## AI-Assisted Development Workflow
AI tools were used throughout the Unit 12 MVP build to accelerate architecture setup, code generation, and documentation:
- **Code & Template Generation (GitHub Copilot):** Used structured prompts to scaffold the Flask application (`app.py`), SQLAlchemy `Show` database model, CRUD routes (`/`, `/add`, `/delete/<id>`), and Bootstrap 5 Jinja templates (`base.html`, `index.html`, `add.html`).
- **Containerization & Environment Setup (Gemini & GitHub Copilot):** Used AI assistance to generate the `Dockerfile`, `.dockerignore`, and pinned `requirements.txt`, as well as troubleshoot local Python environment prompts on Windows before verifying the build in Docker.
- **Documentation & Planning (Gemini):** Used AI to refine the MVP scope, document known stateless SQLite limitations, and structure project documentation across `README.md`, Jira, and Confluence.
