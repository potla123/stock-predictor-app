from stock_data import get_stock_data
from predictor import forecast_stock
import matplotlib.pyplot as plt

# Get stock data
data = get_stock_data("AAPL", "2023-01-01", "2024-01-01")

# Predict next 30 days
forecast, model = forecast_stock(data)

# Plot the forecast
fig = model.plot(forecast)
plt.show()
