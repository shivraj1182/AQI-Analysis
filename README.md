# AQI-Analysis

Air Quality Index (AQI) Analysis and Forecasting for Indian Cities. Analyzes pollution trends (PM2.5, PM10, NO2, SO2) and builds predictive models using ARIMA and Prophet for actionable environmental insights.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Analysis](#data-analysis)
- [Forecasting](#forecasting)
- [Policy Recommendations](#policy-recommendations)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project focuses on comprehensive analysis of Air Quality Index (AQI) data across major Indian cities including Delhi, Mumbai, Kolkata, and Bengaluru. The project aims to:

- Analyze historical pollution trends
- Identify seasonal patterns and high-risk periods
- Build predictive models for future pollution levels
- Provide data-driven policy recommendations
- Generate actionable insights for policymakers and public health officials

## Features

- **Data Preprocessing**: Clean and handle missing values in AQI datasets
- **Exploratory Data Analysis (EDA)**: Comprehensive statistical analysis and visualization
- **Seasonal Analysis**: Identify monthly and seasonal pollution trends
- **Multiple Forecasting Models**: ARIMA and Facebook Prophet implementations
- **Interactive Visualizations**: Time series, distributions, correlations, and comparisons
- **High-Risk Zone Identification**: Detect periods with hazardous air quality
- **Policy Insights**: Evidence-based environmental recommendations

## Project Structure

```
AQI-Analysis/
├── aqi_analysis.py         # Main analysis module with AQIAnalyzer class
├── visualizations.py       # Visualization module with AQIVisualizer class
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # MIT License
└── .gitignore            # Git ignore rules
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/shivraj1182/AQI-Analysis.git
   cd AQI-Analysis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Analysis

```python
from aqi_analysis import AQIAnalyzer

# Initialize analyzer
analyzer = AQIAnalyzer()

# Load and preprocess data
data = analyzer.load_data('aqi_data.csv')
analyzer.preprocess_data()

# Perform EDA
analyzer.exploratory_data_analysis()

# Analyze seasonal trends
seasonal_trends = analyzer.analyze_seasonal_trends()

# Forecast pollution levels
arima_forecast = analyzer.forecast_arima(periods=180)
prophet_forecast = analyzer.forecast_prophet(periods=180)
```

### Visualization

```python
from visualizations import AQIVisualizer

# Initialize visualizer
visualizer = AQIVisualizer()

# Create visualizations
visualizer.plot_time_series(data)
visualizer.plot_pollutant_distribution(data)
visualizer.plot_seasonal_trends(data)
visualizer.plot_correlation_heatmap(data)
```

## Data Analysis

### Key Work Done

- Cleaned and preprocessed raw AQI data to handle missing/inconsistent values
- Conducted EDA to study pollutant distributions and seasonal trends
- Visualized data using Matplotlib, Seaborn, and interactive dashboards
- Applied Time Series Forecasting using ARIMA models
- Implemented Facebook Prophet for seasonal forecasting
- Compared models to identify best-performing approach
- Identified high-risk zones and peak pollution periods

### Pollutants Analyzed

- **PM2.5**: Fine particulate matter
- **PM10**: Coarse particulate matter
- **NO2**: Nitrogen dioxide
- **SO2**: Sulfur dioxide

## Forecasting

### ARIMA Model
- Captures temporal dependencies
- Suitable for seasonal patterns
- Provides confidence intervals

### Facebook Prophet
- Handles seasonal components
- Robust to missing data
- Interpretable trend and seasonality

## Policy Recommendations

Based on comprehensive analysis, the project suggests:

1. **Vehicle Emission Control**: Implement stricter vehicle emission standards
2. **Green Zone Promotion**: Expand green spaces and urban forests
3. **Festival Management**: Issue pollution warnings during festivals with high emissions
4. **Industrial Regulation**: Monitor and regulate industrial emissions
5. **Traffic Management**: Optimize traffic flow to reduce congestion
6. **Public Awareness**: Launch awareness campaigns on air quality and health impacts

## Technologies Used

### Data Processing
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing

### Analysis & Modeling
- **scikit-learn**: Machine learning algorithms
- **statsmodels**: ARIMA implementation
- **fbprophet**: Time series forecasting

### Visualization
- **matplotlib**: Static plots
- **seaborn**: Enhanced statistical visualization
- **plotly**: Interactive visualizations

### Development
- **Jupyter Notebook**: Interactive analysis
- **Python**: Programming language

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Shivraj1182**

- GitHub: [@shivraj1182](https://github.com/shivraj1182)

## Acknowledgments

- Central Pollution Control Board (CPCB) for AQI data
- Statsmodels for ARIMA implementation
- Facebook Prophet for time series forecasting
- Pandas and scikit-learn communities

---

Made with care for environmental analysis and sustainability in India
