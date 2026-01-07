"""Air Quality Index (AQI) Analysis and Forecasting Module"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.arima.model import ARIMA
from fbprophet import Prophet
import warnings
warnings.filterwarnings('ignore')

class AQIAnalyzer:
    """Comprehensive AQI Analysis and Forecasting Class"""
    
    def __init__(self, data_path=None):
        """Initialize AQI Analyzer"""
        self.data = None
        self.data_path = data_path
        self.preprocessed_data = None
        self.forecast_results = {}
        
    def load_data(self, csv_path):
        """Load AQI data from CSV"""
        try:
            self.data = pd.read_csv(csv_path)
            print(f"Data loaded successfully. Shape: {self.data.shape}")
            return self.data
        except FileNotFoundError:
            print(f"File {csv_path} not found.")
            return None
    
    def preprocess_data(self):
        """Clean and preprocess AQI data"""
        if self.data is None:
            print("No data loaded. Please load data first.")
            return None
            
        # Handle missing values
        self.data.fillna(self.data.mean(), inplace=True)
        
        # Remove duplicates
        self.data.drop_duplicates(inplace=True)
        
        # Convert date column to datetime
        if 'Date' in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'])
        
        self.preprocessed_data = self.data.copy()
        print("Data preprocessing completed.")
        return self.preprocessed_data
    
    def exploratory_data_analysis(self):
        """Perform EDA on AQI data"""
        if self.preprocessed_data is None:
            print("Please preprocess data first.")
            return
        
        print("\n=== Exploratory Data Analysis ===")
        print(f"\nData Shape: {self.preprocessed_data.shape}")
        print(f"\nData Types:\n{self.preprocessed_data.dtypes}")
        print(f"\nBasic Statistics:\n{self.preprocessed_data.describe()}")
        print(f"\nMissing Values:\n{self.preprocessed_data.isnull().sum()}")
    
    def analyze_seasonal_trends(self):
        """Analyze seasonal and trend patterns in AQI data"""
        if 'Date' not in self.preprocessed_data.columns:
            print("Date column not found. Cannot analyze trends.")
            return
        
        # Extract month for seasonal analysis
        self.preprocessed_data['Month'] = pd.to_datetime(self.preprocessed_data['Date']).dt.month
        self.preprocessed_data['Year'] = pd.to_datetime(self.preprocessed_data['Date']).dt.year
        
        print("\n=== Seasonal Analysis ===")
        seasonal_avg = self.preprocessed_data.groupby('Month')[['PM2.5', 'PM10', 'NO2', 'SO2']].mean()
        print(seasonal_avg)
        return seasonal_avg
    
    def forecast_arima(self, target_column='AQI', periods=180):
        """Forecast using ARIMA model"""
        print(f"\n=== ARIMA Forecasting ({periods} days) ===")
        
        try:
            model = ARIMA(self.preprocessed_data[target_column], order=(1, 1, 1))
            fitted_model = model.fit()
            forecast = fitted_model.get_forecast(steps=periods)
            forecast_df = forecast.conf_int()
            
            self.forecast_results['ARIMA'] = {
                'model': fitted_model,
                'forecast': forecast,
                'forecast_df': forecast_df
            }
            print(f"ARIMA forecast completed for next {periods} days")
            return forecast_df
        except Exception as e:
            print(f"ARIMA forecasting error: {str(e)}")
            return None
    
    def forecast_prophet(self, target_column='AQI', periods=180):
        """Forecast using Facebook Prophet model"""
        print(f"\n=== Prophet Forecasting ({periods} days) ===")
        
        try:
            # Prepare data for Prophet
            prophet_data = self.preprocessed_data[['Date', target_column]].copy()
            prophet_data.columns = ['ds', 'y']
            
            # Fit model
            model = Prophet(yearly_seasonality=True, daily_seasonality=False)
            model.fit(prophet_data)
            
            # Make forecast
            future = model.make_future_dataframe(periods=periods)
            forecast = model.predict(future)
            
            self.forecast_results['Prophet'] = {
                'model': model,
                'forecast': forecast
            }
            print(f"Prophet forecast completed for next {periods} days")
            return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
        except Exception as e:
            print(f"Prophet forecasting error: {str(e)}")
            return None
    
    def identify_high_risk_zones(self, threshold=200):
        """Identify high pollution risk zones/periods"""
        high_risk = self.preprocessed_data[self.preprocessed_data['AQI'] > threshold]
        print(f"\n=== High Risk Zones (AQI > {threshold}) ===")
        print(f"High risk periods identified: {len(high_risk)}")
        return high_risk
    
    def generate_recommendations(self):
        """Generate policy recommendations based on analysis"""
        print("\n=== Policy Recommendations ===")
        recommendations = [
            "1. Vehicle Emission Control: Implement stricter vehicle emission standards",
            "2. Green Zone Promotion: Expand green spaces and urban forests",
            "3. Festival Management: Issue pollution warnings during festivals",
            "4. Industrial Regulation: Monitor and regulate industrial emissions",
            "5. Traffic Management: Optimize traffic flow to reduce congestion",
            "6. Public Awareness: Launch awareness campaigns on air quality"
        ]
        for rec in recommendations:
            print(rec)
        return recommendations


if __name__ == "__main__":
    # Example usage
    analyzer = AQIAnalyzer()
    print("AQI Analysis Module Ready")
