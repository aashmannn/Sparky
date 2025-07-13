-- Walmart ESG Carbon Optimizer Database Setup
-- Run this script to create the database and tables

-- Create database (run this as superuser)
-- CREATE DATABASE walmart_esg;

-- Connect to the database
-- \c walmart_esg;

-- Create carbon_events table
CREATE TABLE IF NOT EXISTS carbon_events (
    id SERIAL PRIMARY KEY,
    supplier_id VARCHAR(100) NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    emissions_kg_co2e DECIMAL(10, 2) NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    verification_status VARCHAR(20) DEFAULT 'pending',
    source_document VARCHAR(255),
    extracted_data JSONB,
    confidence_score DECIMAL(3, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create forecasts table
CREATE TABLE IF NOT EXISTS forecasts (
    id SERIAL PRIMARY KEY,
    supplier_id VARCHAR(100),
    forecast_date DATE NOT NULL,
    predicted_emissions DECIMAL(10, 2) NOT NULL,
    confidence_interval_lower DECIMAL(10, 2),
    confidence_interval_upper DECIMAL(10, 2),
    model_version VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create incentives table
CREATE TABLE IF NOT EXISTS incentives (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    emission_reduction_threshold DECIMAL(10, 2),
    financial_incentive DECIMAL(10, 2),
    eligibility_criteria JSONB,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create reports table
CREATE TABLE IF NOT EXISTS reports (
    id SERIAL PRIMARY KEY,
    report_type VARCHAR(50) NOT NULL,
    report_date DATE NOT NULL,
    data_period_start DATE,
    data_period_end DATE,
    total_emissions DECIMAL(10, 2),
    report_data JSONB,
    file_path VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_carbon_events_supplier_id ON carbon_events(supplier_id);
CREATE INDEX IF NOT EXISTS idx_carbon_events_timestamp ON carbon_events(timestamp);
CREATE INDEX IF NOT EXISTS idx_carbon_events_event_type ON carbon_events(event_type);
CREATE INDEX IF NOT EXISTS idx_forecasts_supplier_id ON forecasts(supplier_id);
CREATE INDEX IF NOT EXISTS idx_forecasts_forecast_date ON forecasts(forecast_date);

-- Insert sample data
INSERT INTO carbon_events (supplier_id, event_type, emissions_kg_co2e, verification_status, source_document) VALUES
('SUP001', 'transport', 1250.50, 'verified', 'invoice_001.pdf'),
('SUP002', 'manufacturing', 890.20, 'verified', 'manufacturing_report_001.pdf'),
('SUP001', 'energy', 650.80, 'verified', 'utility_bill_001.pdf'),
('SUP003', 'transport', 2100.30, 'verified', 'transport_log_001.csv'),
('SUP002', 'waste', 320.45, 'verified', 'waste_report_001.pdf');

INSERT INTO forecasts (supplier_id, forecast_date, predicted_emissions, confidence_interval_lower, confidence_interval_upper, model_version) VALUES
('SUP001', '2024-02-15', 1800.50, 1650.20, 1950.80, 'v1.0'),
('SUP002', '2024-02-15', 1200.30, 1100.50, 1300.10, 'v1.0'),
('SUP003', '2024-02-15', 2500.75, 2300.40, 2700.10, 'v1.0');

INSERT INTO incentives (name, description, emission_reduction_threshold, financial_incentive, eligibility_criteria) VALUES
('Carbon Credit Program', 'Earn carbon credits for emissions reductions above 10%', 1000.00, 500.00, '{"min_reduction_percent": 10, "verification_required": true}'),
('Green Supplier Bonus', 'Additional payment for suppliers with emissions below threshold', 500.00, 250.00, '{"max_emissions": 1000, "sustainability_certification": true}'),
('Efficiency Grant', 'Grant funding for energy efficiency improvements', 2000.00, 1000.00, '{"project_based": true, "roi_requirement": 15}');

INSERT INTO reports (report_type, report_date, data_period_start, data_period_end, total_emissions, report_data) VALUES
('monthly', '2024-01-31', '2024-01-01', '2024-01-31', 5211.25, '{"suppliers": 3, "events": 5, "trend": "decreasing"}'),
('quarterly', '2024-01-31', '2024-01-01', '2024-03-31', 15000.00, '{"suppliers": 5, "events": 15, "trend": "stable"}'); 