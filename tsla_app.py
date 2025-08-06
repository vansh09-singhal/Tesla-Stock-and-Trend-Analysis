import streamlit as st
from PIL import Image

st.set_page_config(page_title="Tesla Stock Analysis Dashboard", layout="wide")

st.title("📈 Tesla Stock Price Analysis Dashboard")

# -------------------
st.header("Project Purpose & Motivation")

st.write("""
While many projects jump directly into building complex models or applying machine learning,  
I chose to take a step back and focus on something more foundational: **data understanding**.

Tesla, being a volatile and influential stock, offered the perfect dataset to showcase how much can be uncovered just through:
- Clean SQL queries,
- Visual exploration using Python (matplotlib),
- And strong storytelling.

---

Too often, raw data is fed into models without being truly understood.  
But **data becomes powerful only when deeply explored** — patterns, anomalies, trends, and relationships must be revealed before any modeling has real meaning.

This project was a conscious decision to build that **core analytical mindset** — to treat data as more than numbers, but as a source of insight.

In a way, this isn't a "simple" project — it's a **strategic foundation** for everything more advanced that comes next in my data career.
""")

st.header("1. Dataset Overview")

st.write("""
We analyzed Tesla stock performance using a dataset that includes:

- Daily prices (Open, High, Low, Close)
- Trading Volume
- Timestamps

The data was stored in a MySQL table named `mytable`. Here's a look at the structure of this table:
""")

st.image("table_structure_sql.jpg")

st.write("""
- This step helps us verify the schema before performing any analysis.
- We confirm that dates, prices, and volume are correctly typed.
""")

# -------------------
st.header("2. Average Monthly Closing Price")

st.image("avg_monthly_price.jpg")

st.markdown("**SQL Query Used:**")
st.image("avg_close_price_sql.jpg")

st.write("""
- **Explanation:** This plot shows how Tesla's average monthly closing price evolved.
- A visible uptrend in late 2024 indicates strong market sentiment.
""")

# -------------------
st.header("3. High vs Low Price Comparison")

st.image("high_vs_low.jpg")

st.markdown("**SQL Query Used:**")
st.image("high_vs_low_sql.jpg")

st.write("""
- **Explanation:** Daily High and Low prices capture Tesla's intra-day price volatility.
- Wide gaps signal uncertainty or news impact.
""")

# -------------------
st.header("4. Closing Price Over Time")

st.image("close_price.jpg")

st.markdown("**SQL Query Used:**")
st.image("close_price_sql.jpg")

st.write("""
- **Explanation:** This chart shows Tesla's closing price trend.
- Sharp growth toward end of 2024 points to strong investor confidence.
""")

# -------------------
st.header("5. Trade Volume Trend")

st.image("trade_volume.jpg")

st.markdown("**SQL Query Used:**")
st.image("trade_volume_sql.jpg")

st.write("""
- **Explanation:** Trading volume shows investor activity.
- Spikes usually correlate with major events or earnings announcements.
""")

# -------------------
st.header("6. Daily Return Distribution")

st.image("daily_return.jpg")

st.write("""
- **Explanation:** Daily returns are calculated as percent change from the previous close.
- A bell-shaped curve indicates normal fluctuations. Extreme values signal risky days.
""")

# -------------------
st.header("7. Correlation Heatmap")

st.image("correlation_heatmap.jpg")

st.write("""
- **Explanation:** Correlation between variables like Open, Close, High, Low is strong (near 1).
- Volume has weak correlation with price, showing it's influenced by different factors.
""")

# -------------------
st.header("8. 20-Day Rolling Volatility")

st.image("rolling_volatility.jpg")

st.write("""
- **Explanation:** This plot helps assess risk over time.
- Peaks in volatility suggest uncertainty or reaction to major events.
""")

# -------------------
st.header("9. Price vs 20-Day Moving Average")

st.image("rolling_avg.jpg")

st.write("""
- **Explanation:** The 20-day moving average smooths out fluctuations.
- When price crosses above the average, it can indicate bullish signals (and vice versa).
""")

# -------------------
st.subheader("📌 Final Conclusion")

st.write("""
- Tesla stock showed strong growth especially in the second half of 2024.
- Technical indicators like moving averages and volatility help interpret trends.
- SQL + Python (matplotlib) allowed us to blend structured data querying with advanced visual storytelling.
""")
