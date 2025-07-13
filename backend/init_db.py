from sqlalchemy import create_engine, text
from app.core.database import Base, engine
from app.models.carbon_event import CarbonEvent
from app.models.forecast import Forecast
from app.models.incentive import Incentive
from app.models.report import Report
from datetime import datetime, timedelta
import json

def init_database():
    """Initialize the database with tables and sample data"""
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create a connection to insert sample data
    with engine.connect() as conn:
        # Check if data already exists
        result = conn.execute(text("SELECT COUNT(*) FROM carbon_events"))
        if result.scalar() > 0:
            print("Database already contains data. Skipping initialization.")
            return
        
        # Insert sample carbon events
        sample_events = [
            {
                'supplier_id': 'SUP001',
                'event_type': 'transport',
                'emissions_kg_co2e': 1250.50,
                'timestamp': datetime.now() - timedelta(days=1),
                'verification_status': 'verified',
                'source_document': 'invoice_001.pdf',
                'extracted_data': json.dumps({
                    'fuel_consumption': 500.0,
                    'distance_km': 2000.0,
                    'vehicle_type': 'diesel_truck'
                }),
                'confidence_score': 0.95
            },
            {
                'supplier_id': 'SUP002',
                'event_type': 'manufacturing',
                'emissions_kg_co2e': 890.20,
                'timestamp': datetime.now() - timedelta(days=2),
                'verification_status': 'verified',
                'source_document': 'manufacturing_report_001.pdf',
                'extracted_data': json.dumps({
                    'energy_consumption': 2500.0,
                    'raw_materials': 1000.0,
                    'waste_generated': 50.0
                }),
                'confidence_score': 0.92
            },
            {
                'supplier_id': 'SUP001',
                'event_type': 'energy',
                'emissions_kg_co2e': 650.80,
                'timestamp': datetime.now() - timedelta(days=3),
                'verification_status': 'verified',
                'source_document': 'utility_bill_001.pdf',
                'extracted_data': json.dumps({
                    'electricity_consumption': 1500.0,
                    'gas_consumption': 200.0
                }),
                'confidence_score': 0.88
            },
            {
                'supplier_id': 'SUP003',
                'event_type': 'transport',
                'emissions_kg_co2e': 2100.30,
                'timestamp': datetime.now() - timedelta(days=4),
                'verification_status': 'verified',
                'source_document': 'transport_log_001.csv',
                'extracted_data': json.dumps({
                    'fuel_consumption': 800.0,
                    'distance_km': 3500.0,
                    'vehicle_type': 'refrigerated_truck'
                }),
                'confidence_score': 0.94
            },
            {
                'supplier_id': 'SUP002',
                'event_type': 'waste',
                'emissions_kg_co2e': 320.45,
                'timestamp': datetime.now() - timedelta(days=5),
                'verification_status': 'verified',
                'source_document': 'waste_report_001.pdf',
                'extracted_data': json.dumps({
                    'waste_volume': 100.0,
                    'waste_type': 'industrial',
                    'disposal_method': 'landfill'
                }),
                'confidence_score': 0.87
            }
        ]
        
        for event in sample_events:
            conn.execute(text("""
                INSERT INTO carbon_events 
                (supplier_id, event_type, emissions_kg_co2e, timestamp, verification_status, 
                 source_document, extracted_data, confidence_score, created_at, updated_at)
                VALUES (:supplier_id, :event_type, :emissions_kg_co2e, :timestamp, :verification_status,
                        :source_document, :extracted_data, :confidence_score, :created_at, :updated_at)
            """), {
                **event,
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            })
        
        # Insert sample forecasts
        sample_forecasts = [
            {
                'supplier_id': 'SUP001',
                'forecast_date': datetime.now().date() + timedelta(days=30),
                'predicted_emissions': 1800.50,
                'confidence_interval_lower': 1650.20,
                'confidence_interval_upper': 1950.80,
                'model_version': 'v1.0'
            },
            {
                'supplier_id': 'SUP002',
                'forecast_date': datetime.now().date() + timedelta(days=30),
                'predicted_emissions': 1200.30,
                'confidence_interval_lower': 1100.50,
                'confidence_interval_upper': 1300.10,
                'model_version': 'v1.0'
            },
            {
                'supplier_id': 'SUP003',
                'forecast_date': datetime.now().date() + timedelta(days=30),
                'predicted_emissions': 2500.75,
                'confidence_interval_lower': 2300.40,
                'confidence_interval_upper': 2700.10,
                'model_version': 'v1.0'
            }
        ]
        
        for forecast in sample_forecasts:
            conn.execute(text("""
                INSERT INTO forecasts 
                (supplier_id, forecast_date, predicted_emissions, confidence_interval_lower, 
                 confidence_interval_upper, model_version, created_at)
                VALUES (:supplier_id, :forecast_date, :predicted_emissions, :confidence_interval_lower,
                        :confidence_interval_upper, :model_version, :created_at)
            """), {
                **forecast,
                'created_at': datetime.now()
            })
        
        # Insert sample incentives
        sample_incentives = [
            {
                'name': 'Carbon Credit Program',
                'description': 'Earn carbon credits for emissions reductions above 10%',
                'emission_reduction_threshold': 1000.00,
                'financial_incentive': 500.00,
                'eligibility_criteria': json.dumps({
                    'min_reduction_percent': 10,
                    'verification_required': True
                }),
                'active': True
            },
            {
                'name': 'Green Supplier Bonus',
                'description': 'Additional payment for suppliers with emissions below threshold',
                'emission_reduction_threshold': 500.00,
                'financial_incentive': 250.00,
                'eligibility_criteria': json.dumps({
                    'max_emissions': 1000,
                    'sustainability_certification': True
                }),
                'active': True
            },
            {
                'name': 'Efficiency Grant',
                'description': 'Grant funding for energy efficiency improvements',
                'emission_reduction_threshold': 2000.00,
                'financial_incentive': 1000.00,
                'eligibility_criteria': json.dumps({
                    'project_based': True,
                    'roi_requirement': 15
                }),
                'active': True
            }
        ]
        
        for incentive in sample_incentives:
            conn.execute(text("""
                INSERT INTO incentives 
                (name, description, emission_reduction_threshold, financial_incentive, 
                 eligibility_criteria, active, created_at)
                VALUES (:name, :description, :emission_reduction_threshold, :financial_incentive,
                        :eligibility_criteria, :active, :created_at)
            """), {
                **incentive,
                'created_at': datetime.now()
            })
        
        # Insert sample reports
        sample_reports = [
            {
                'report_type': 'monthly',
                'report_date': datetime.now().date(),
                'data_period_start': datetime.now().replace(day=1).date(),
                'data_period_end': datetime.now().date(),
                'total_emissions': 5211.25,
                'report_data': json.dumps({
                    'suppliers': 3,
                    'events': 5,
                    'trend': 'decreasing'
                }),
                'file_path': 'reports/monthly_2024_01.pdf'
            },
            {
                'report_type': 'quarterly',
                'report_date': datetime.now().date(),
                'data_period_start': datetime.now().replace(month=1, day=1).date(),
                'data_period_end': datetime.now().date(),
                'total_emissions': 15000.00,
                'report_data': json.dumps({
                    'suppliers': 5,
                    'events': 15,
                    'trend': 'stable'
                }),
                'file_path': 'reports/quarterly_2024_Q1.pdf'
            }
        ]
        
        for report in sample_reports:
            conn.execute(text("""
                INSERT INTO reports 
                (report_type, report_date, data_period_start, data_period_end, total_emissions,
                 report_data, file_path, created_at)
                VALUES (:report_type, :report_date, :data_period_start, :data_period_end, :total_emissions,
                        :report_data, :file_path, :created_at)
            """), {
                **report,
                'created_at': datetime.now()
            })
        
        conn.commit()
        print("Database initialized successfully with sample data!")

if __name__ == "__main__":
    init_database() 