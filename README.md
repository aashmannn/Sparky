# Autonomous ESG Carbon Optimizer for Walmart

An AI-powered web platform that automates end-to-end carbon emissions tracking, forecasting, incentive optimization, and ESG compliance reporting across Walmart's global supply chain.

## Project Overview

The Autonomous ESG Carbon Optimizer is a comprehensive solution designed to help Walmart achieve its sustainability goals by:

- **Automating Data Ingestion**: NLP-powered parsing of supplier invoices, utility bills, and CSV files
- **Carbon Ledger Management**: Structured storage of carbon event data with audit trails
- **AI-Powered Forecasting**: ML models predicting future emissions by supplier, route, or SKU
- **Incentive Optimization**: Matching emissions reductions to sustainability incentives and carbon credits
- **Compliance Reporting**: One-click generation of SEC/EU compliant ESG reports

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   Database      │
│   (React.js)    │◄──►│   (FastAPI)     │◄──►│  (PostgreSQL)   │
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
- PostgreSQL 13+
- Docker (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd walmart-esg-optimizer
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

4. **Database Setup**
   ```bash
   cd database
   # Follow PostgreSQL setup instructions
   ```

5. **Start the Application**
   ```bash
   # Terminal 1: Backend
   cd backend
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   
   # Terminal 2: Frontend
   cd frontend
   npm start
   ```

## Features

### 1. Data Ingestion & Parsing
- Drag-and-drop interface for file uploads
- NLP-powered extraction using Hugging Face Transformers
- Support for PDF invoices, CSV files, and utility bills
- Automatic emission factor mapping

### 2. Carbon Ledger
- PostgreSQL-based structured storage
- Timestamped carbon events with audit flags
- Supplier and product-level tracking
- Blockchain-ready architecture

### 3. Emissions Forecasting
- ML models trained on historical data
- Predictions by supplier, route, and SKU
- RESTful API endpoints for forecasts
- Confidence intervals and trend analysis

### 4. Incentive Mapping Engine
- Rules-based matching system
- Carbon credit eligibility assessment
- Rebate opportunity detection
- Financial impact calculations

### 5. Report Generation
- SEC/EU compliance-ready reports
- PDF and CSV export options
- Blockchain hash verification
- Executive dashboard summaries

## UI/UX Design

Inspired by Tolerisk.com with a professional, executive-style interface:

- **Color Palette**: White and deep blue base with steel grey accents
- **Typography**: Modern sans-serif fonts (Inter, Open Sans)
- **Layout**: Card-based UI with elevated containers
- **Responsive**: Mobile-friendly grid layout
- **Interactions**: Smooth transitions and hover animations

## Tech Stack

### Frontend
- **React.js** - UI framework
- **Chart.js** - Data visualization
- **TailwindCSS** - Styling
- **Axios** - HTTP client

### Backend
- **FastAPI** - Python web framework
- **SQLAlchemy** - ORM
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### AI/ML
- **Hugging Face Transformers** - NLP processing
- **PyTorch** - Deep learning
- **scikit-learn** - Machine learning
- **Pandas** - Data manipulation

### Database
- **PostgreSQL** - Primary database
- **Redis** - Caching (optional)

### DevOps
- **Docker** - Containerization
- **GitHub Actions** - CI/CD
- **AWS/GCP** - Cloud hosting

## Mock Data Sources

- EPA GHG emission factors
- UCI Smart Meter Data
- Synthetic invoice PDFs
- EU carbon trading data

## API Endpoints

### Data Ingestion
- `POST /api/v1/upload` - File upload and parsing
- `POST /api/v1/parse` - Manual data entry

### Carbon Ledger
- `GET /api/v1/carbon-events` - Retrieve carbon events
- `POST /api/v1/carbon-events` - Create new carbon event
- `PUT /api/v1/carbon-events/{id}` - Update carbon event

### Forecasting
- `GET /api/v1/forecast` - Get emissions forecasts
- `POST /api/v1/forecast/train` - Retrain ML models

### Incentives
- `GET /api/v1/incentives` - Available incentives
- `POST /api/v1/incentives/match` - Match reductions to incentives

### Reports
- `GET /api/v1/reports` - Generate ESG reports
- `GET /api/v1/reports/{id}/download` - Download report

## Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

