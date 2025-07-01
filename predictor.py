from prophet import Prophet
import pandas as pd

def forecast_stock(data, periods=30):
    # Step 1: Prepare data for Prophet
    df = data.reset_index()[['Date', 'Close']]
    df.columns = ['ds', 'y']  # Prophet requires these exact column names

    # Step 2: Train the model
    model = Prophet()
    model.fit(df)

    # Step 3: Create future dates for prediction
    future = model.make_future_dataframe(periods=periods)

    # Step 4: Make forecast
    forecast = model.predict(future)

    return forecast, model
