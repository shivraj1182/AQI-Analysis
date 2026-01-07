"""Data Visualization Module for AQI Analysis"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class AQIVisualizer:
    """Visualization class for AQI analysis results"""
    
    def __init__(self, style='seaborn-v0_8-darkgrid'):
        """Initialize visualizer with style"""
        plt.style.use(style)
        sns.set_palette("husl")
        
    def plot_time_series(self, data, date_column='Date', aqi_column='AQI', title='AQI Time Series'):
        """Plot AQI time series"""
        plt.figure(figsize=(14, 6))
        plt.plot(data[date_column], data[aqi_column], linewidth=2, color='#1f77b4')
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('AQI', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        return plt
    
    def plot_pollutant_distribution(self, data, pollutants=['PM2.5', 'PM10', 'NO2', 'SO2']):
        """Plot distribution of pollutants"""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Pollutant Distributions', fontsize=16, fontweight='bold')
        
        for idx, pollutant in enumerate(pollutants):
            ax = axes[idx // 2, idx % 2]
            if pollutant in data.columns:
                data[pollutant].hist(bins=30, ax=ax, color='#ff7f0e', alpha=0.7)
                ax.set_title(f'{pollutant} Distribution', fontweight='bold')
                ax.set_xlabel('Concentration')
                ax.set_ylabel('Frequency')
        
        plt.tight_layout()
        return plt
    
    def plot_seasonal_trends(self, data, pollutants=['PM2.5', 'PM10', 'NO2', 'SO2']):
        """Plot seasonal trends"""
        if 'Month' not in data.columns:
            print("Month column not found in data")
            return None
        
        plt.figure(figsize=(12, 6))
        monthly_avg = data.groupby('Month')[pollutants].mean()
        
        for pollutant in pollutants:
            if pollutant in monthly_avg.columns:
                plt.plot(monthly_avg.index, monthly_avg[pollutant], marker='o', label=pollutant, linewidth=2)
        
        plt.title('Seasonal Pollutant Trends', fontsize=14, fontweight='bold')
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Average Concentration', fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(range(1, 13))
        plt.tight_layout()
        return plt
    
    def plot_correlation_heatmap(self, data, columns=None):
        """Plot correlation heatmap"""
        if columns is None:
            columns = ['PM2.5', 'PM10', 'NO2', 'SO2', 'AQI']
        
        # Filter only numeric columns that exist
        cols_to_use = [col for col in columns if col in data.columns]
        
        if len(cols_to_use) == 0:
            print("No valid columns found for correlation analysis")
            return None
        
        corr_matrix = data[cols_to_use].corr()
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                    square=True, linewidths=1, cbar_kws={"shrink": 0.8})
        plt.title('Pollutant Correlation Matrix', fontsize=14, fontweight='bold')
        plt.tight_layout()
        return plt
    
    def plot_forecast_comparison(self, actual_data, arima_forecast=None, prophet_forecast=None):
        """Compare actual vs forecasted AQI values"""
        plt.figure(figsize=(14, 6))
        
        # Plot actual data
        plt.plot(actual_data.index, actual_data.values, 'b-', label='Actual AQI', linewidth=2)
        
        # Plot forecasts if available
        if arima_forecast is not None:
            plt.plot(arima_forecast.index, arima_forecast.values, 'r--', label='ARIMA Forecast', linewidth=2)
        
        if prophet_forecast is not None:
            plt.plot(prophet_forecast.index, prophet_forecast.values, 'g--', label='Prophet Forecast', linewidth=2)
        
        plt.title('AQI Forecast Comparison', fontsize=14, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('AQI', fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt
    
    def plot_city_comparison(self, data, city_column='City', aqi_column='AQI'):
        """Compare AQI across different cities"""
        if city_column not in data.columns:
            print(f"{city_column} column not found")
            return None
        
        city_aqi = data.groupby(city_column)[aqi_column].mean().sort_values(ascending=False)
        
        plt.figure(figsize=(12, 6))
        city_aqi.plot(kind='bar', color='#2ca02c', alpha=0.7)
        plt.title('Average AQI by City', fontsize=14, fontweight='bold')
        plt.xlabel('City', fontsize=12)
        plt.ylabel('Average AQI', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        return plt


if __name__ == "__main__":
    visualizer = AQIVisualizer()
    print("AQI Visualization Module Ready")
