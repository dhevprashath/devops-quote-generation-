# Setup Instructions

This project consists of a FastAPI backend and a React frontend. You can run the application using either Docker (recommended) or natively on your machine.

## Option 1: Running with Docker (Recommended)
Make sure Docker Desktop is installed and **running** on your system before proceeding.

1. Open your terminal in the root of the project.
2. Run the following command to build and start both the frontend and backend containers:
   ```bash
   docker-compose up --build
   ```
   *(To run it in the background, you can add `-d` at the end: `docker-compose up --build -d`)*
3. Once the containers are up and running, access the applications at:
   - **Frontend (React)**: [http://localhost:3000](http://localhost:3000)
   - **Backend API (FastAPI)**: [http://localhost:8000](http://localhost:8000)
   - **API Documentation (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Option 2: Running Locally (Without Docker)

### 1. Start the Backend
1. Open a new terminal and navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. (Optional but recommended) Create and activate a Python virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### 2. Start the Frontend
1. Open a **new** terminal (keep the backend terminal running) and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install the necessary Node.js packages:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
