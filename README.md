# ESG Carbon Optimizer

An AI-powered web platform that automates end-to-end carbon emissions tracking, forecasting, incentive optimization, and ESG compliance reporting.

## Project Overview

The ESG Carbon Optimizer is a comprehensive solution designed to help organizations achieve their sustainability goals by:

- **Automating Data Ingestion**: NLP-powered parsing of supplier invoices, utility bills, and CSV files
- **Carbon Ledger Management**: Structured storage of carbon event data with audit trails
- **AI-Powered Forecasting**: ML models predicting future emissions by supplier, route, or SKU
- **Incentive Optimization**: Matching emissions reductions to sustainability incentives and carbon credits
- **Compliance Reporting**: One-click generation of SEC/EU compliant ESG reports

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   Database      │
│   (React.js)    │◄──►│   (FastAPI)     │◄──►│   (SQLite)      │
│                 │    │                 │    │                 │
│ • Dashboard     │    │ • Data Ingestion│    │ • Carbon Ledger │
│ • Upload UI     │    │ • ML Models     │    │ • User Data     │
│ • Reports       │    │ • API Endpoints │    │ • Audit Logs    │
│ • Charts        │    │ • NLP Processing│    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aashmannn/Sparky.git
   cd Sparky
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Start the Application**
   ```bash
   # Terminal 1: Backend
   cd backend
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   
   # Terminal 2: Frontend
   cd frontend
   npm start
   ```

5. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Features

### 1. Data Ingestion & Parsing
- Drag-and-drop interface for file uploads
- NLP-powered extraction using Google Gemini
- Support for PDF invoices, CSV files, and utility bills
- Automatic emission factor mapping

### 2. Carbon Ledger
- SQLite-based structured storage (PostgreSQL for production)
- Timestamped carbon events with audit flags
- Supplier and product-level tracking
- Real-time data visualization

### 3. Emissions Forecasting
- ML models for emissions prediction
- Predictions by supplier, route, and SKU
- RESTful API endpoints for forecasts
- Interactive charts and trend analysis

### 4. Incentive Mapping Engine
- Rules-based matching system
- Carbon credit eligibility assessment
- Rebate opportunity detection
- Financial impact calculations

### 5. Report Generation
- ESG compliance-ready reports
- PDF and CSV export options
- Executive dashboard summaries
- Real-time analytics

## UI/UX Design

Professional, executive-style interface with:

- **Color Palette**: White and deep blue base with steel grey accents
- **Typography**: Modern sans-serif fonts
- **Layout**: Card-based UI with elevated containers
- **Responsive**: Mobile-friendly grid layout
- **Interactions**: Smooth transitions and hover animations

## Tech Stack

### Frontend
- **React.js** - UI framework
- **Chart.js** - Data visualization
- **TailwindCSS** - Styling
- **Axios** - HTTP client
- **TypeScript** - Type safety

### Backend
- **FastAPI** - Python web framework
- **SQLAlchemy** - ORM
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### AI/ML
- **Google Gemini** - NLP processing
- **scikit-learn** - Machine learning
- **Pandas** - Data manipulation

### Database
- **SQLite** - Development database
- **PostgreSQL** - Production database (recommended)

## Deployment

### Frontend (Netlify)
The frontend is configured for deployment on Netlify with:
- Build command: `npm run build`
- Publish directory: `frontend/build`
- Environment variables for backend API URL

### Backend (Recommended Platforms)
- **Render**: Easy deployment with PostgreSQL
- **Railway**: Simple setup with database
- **Heroku**: Traditional platform with add-ons
- **Fly.io**: Modern container platform

## API Endpoints

### Data Ingestion
- `POST /api/v1/upload/file` - File upload and parsing

### Carbon Ledger
- `GET /api/v1/carbon-events` - Retrieve carbon events
- `POST /api/v1/carbon-events` - Create new carbon event

### Forecasting
- `GET /api/v1/forecasts` - Get emissions forecasts
- `POST /api/v1/forecast/generate` - Generate new forecast

### Incentives
- `GET /api/v1/incentives` - Available incentives

### Reports
- `GET /api/v1/reports` - Generate ESG reports

## Environment Variables

### Frontend (.env)
```
REACT_APP_BACKEND_URL=http://localhost:8000
REACT_APP_GEMINI_API_KEY=your_gemini_api_key
```

### Backend (.env)
```
DATABASE_URL=sqlite:///./esg_optimizer.db
GEMINI_API_KEY=your_gemini_api_key
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

