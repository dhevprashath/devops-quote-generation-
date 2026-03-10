# AI Quote Generator

A full-stack web application that generates motivational quotes using Google Gemini AI and stores them in a SQLite database.

## Features

- Generate AI-powered motivational quotes for software developers
- Save quotes to SQLite database
- View previously generated quotes
- Delete saved quotes
- Modern React UI
- Dockerized application
- CI/CD pipeline with GitHub Actions

## Tech Stack

- **Frontend:** React.js
- **Backend:** Python FastAPI
- **Database:** SQLite
- **AI:** Google Gemini API
- **DevOps:** Docker, Docker Compose, GitHub Actions

## Prerequisites

### Installing Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer (check "Add Python to PATH")
3. Verify installation: `python --version`

### Installing Node.js

1. Download Node.js from [nodejs.org](https://nodejs.org/)
2. Run the installer
3. Verify installation: `node --version`

### Installing Docker

1. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop)
2. Run the installer
3. Start Docker Desktop
4. Verify installation: `docker --version`

### Installing Git

1. Download Git from [git-scm.com](https://git-scm.com/)
2. Run the installer
3. Verify installation: `git --version`

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd devops-project
```

### 2. Configure API Key

1. Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Edit `backend/.env` and replace `your_api_key_here` with your actual API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

## Running the Application

### Option 1: Docker Compose (Recommended)

```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

### Option 2: Run Backend and Frontend Separately

#### Backend
```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Run the backend server
python main.py

# Or use uvicorn directly
uvicorn main:app --reload
```

#### Frontend
```bash
# Navigate to frontend directory
cd frontend

# Install npm dependencies
npm install

# Start development server
npm start

# Build for production
npm run build
```

### Option 3: Individual Docker Containers

```bash
# Build backend image
docker build -t quote-backend ./backend

# Run backend container
docker run -p 8000:8000 -e GEMINI_API_KEY=your_api_key quote-backend

# Build frontend image
docker build -t quote-frontend ./frontend

# Run frontend container
docker run -p 3000:3000 quote-frontend
```

### Common Commands

```bash
# List running containers
docker ps

# View container logs
docker logs <container_id>

# Rebuild after code changes
docker-compose build

# Restart a specific service
docker-compose restart backend

# Access container shell
docker exec -it <container_id> sh
```

### Verify Services

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /generate | Generate a new AI quote |
| GET | /quotes | Get all saved quotes |
| DELETE | /quote/{id} | Delete a quote by ID |

## Project Structure

```
devops-project/
├── backend/
│   ├── main.py           # FastAPI application
│   ├── database.py      # Database operations
│   ├── requirements.txt # Python dependencies
│   ├── .env            # Environment variables
│   └── Dockerfile      # Backend container
├── frontend/
│   ├── src/
│   │   ├── App.js      # Main React component
│   │   ├── App.css     # Styles
│   │   └── index.js    # Entry point
│   ├── public/
│   │   └── index.html  # HTML template
│   ├── package.json    # Node dependencies
│   └── Dockerfile      # Frontend container
├── docker-compose.yml  # Docker Compose configuration
├── .github/
│   └── workflows/
│       └── build.yml   # CI/CD workflow
└── README.md          # This file
```

## AWS EC2 Deployment

### 1. Launch EC2 Instance

1. Go to AWS Console > EC2
2. Launch Instance with:
   - AMI: Ubuntu Server 22.04 LTS
   - Instance Type: t3.small (or larger)
   - Security Group: Open ports 22 (SSH), 80 (HTTP), 3000, 8000

### 2. Connect to Instance

```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

### 3. Install Docker

```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker ubuntu
```

### 4. Clone and Configure

```bash
git clone <repository-url>
cd devops-project
cp backend/.env.example backend/.env
nano backend/.env  # Add your GEMINI_API_KEY
```

### 5. Build and Run

```bash
docker-compose up -d --build
```

### 6. Access Application

- Frontend: http://your-instance-ip:3000
- Backend API: http://your-instance-ip:8000

### Optional: Set up Nginx Reverse Proxy

```bash
sudo apt install -y nginx
sudo nano /etc/nginx/sites-available/default
```

Add configuration:

```nginx
server {
    listen 80;
    server_name your-instance-ip;

    location / {
        proxy_pass http://localhost:3000;
    }

    location /api {
        proxy_pass http://localhost:8000;
    }
}
```

Restart nginx:
```bash
sudo systemctl restart nginx
```

Now access at http://your-instance-ip

## GitHub Actions

The CI/CD pipeline automatically builds Docker images on push to main branch.

View workflow: `.github/workflows/build.yml`

## License

MIT License
