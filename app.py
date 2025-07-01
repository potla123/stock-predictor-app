import streamlit as st
from stock_data import get_stock_data
from predictor import forecast_stock
import matplotlib.pyplot as plt
from datetime import date

# Page settings
st.set_page_config(page_title="📈 Stock Prices Forecast App")

# Title
st.title("📊 Stock Prices Analysis and Prediction")

# User Inputs
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)", value="AAPL")
start = st.date_input("Start Date", value=date(2020, 1, 1))
end = st.date_input("End Date", value=date.today())

if st.button("Fetch & Predict"):
    with st.spinner("Fetching data and building forecast..."):
        try:
            # Fetch data
            data = get_stock_data(ticker, start, end)

            if data.empty:
                st.error("No data found for the given ticker and dates. Please check and try again.")
            else:
                # Show data preview
                st.subheader("📄 Recent Stock Data")
                st.write(data.tail())

                # Show line chart
                st.subheader("📉 Historical Closing Prices")
                st.line_chart(data['Close'])

                # Forecast
                forecast, model = forecast_stock(data)

                # Show forecast plot
                st.subheader("🔮 Forecast for Next 30 Days")
                fig = model.plot(forecast)
                st.pyplot(fig)

        except Exception as e:
            st.error(f"❌ Error: {e}")
