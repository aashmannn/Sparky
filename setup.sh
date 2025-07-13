#!/bin/bash

echo "Setting up Walmart ESG Carbon Optimizer..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3.9+ and try again."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is required but not installed. Please install Node.js 16+ and try again."
    exit 1
fi

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
    echo "PostgreSQL is required but not installed. Please install PostgreSQL 13+ and try again."
    echo "You can install it using: brew install postgresql (macOS) or apt-get install postgresql (Ubuntu)"
    exit 1
fi

echo "Prerequisites check passed!"

# Setup Backend
echo "Setting up backend..."
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    cp env.example .env
    echo "Created .env file. Please update the DATABASE_URL in backend/.env with your PostgreSQL credentials."
fi

cd ..

# Setup Frontend
echo "Setting up frontend..."
cd frontend

# Install dependencies
npm install

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    cp env.example .env
    echo "Created .env file for frontend."
fi

cd ..

# Database setup instructions
echo ""
echo "Database Setup Instructions:"
echo "1. Start PostgreSQL service"
echo "2. Create a database named 'walmart_esg'"
echo "3. Run the setup script: psql -d walmart_esg -f database/setup.sql"
echo ""
echo "To start the application:"
echo "1. Backend: cd backend && source venv/bin/activate && python main.py"
echo "2. Frontend: cd frontend && npm start"
echo ""
echo "The application will be available at:"
echo "- Frontend: http://localhost:3000"
echo "- Backend API: http://localhost:8000"
echo "- API Documentation: http://localhost:8000/docs" 