import google.generativeai as genai
import streamlit as st
#api key
genai.configure(api_key='AIzaSyBebHKyWyXzEKyyGOyz0cioDc7d3EaYZ0Q')
model=genai.GenerativeModel("gemini-2.5-flash")
st.set_page_config(
    page_title="📊 Commodity Price Analyzer",
    page_icon="💹",
    layout="wide",
)
st.title("💹 Commodity Price Analyzer")
st.markdown(
    """
    Welcome to the **Commodity Price Analyzer**!  
    Enter a commodity, select your desired outlook, and get an analysis.  
    """
)
#inputs 
commodity=st.text_input("Enter the name of the commodity you want to analyze")
purpose=st.text_input("Enter the name of the reason you need this data")
time=st.selectbox("select the time horizon for analysis",["Short-term (1 week - 1 month)","Medium-term (1 month - 6 months)","Long-term (6 months - 1 year)"])
prompt = f"""You are a financial analyst specializing in commodity markets. 
Analyze and predict the **{time}** price trend of {commodity}. 

In your response, consider:
- Historical price patterns of {commodity}
- Supply factors (e.g., production levels, weather, labor, geopolitical issues)
- Demand factors (e.g., consumption trends, industrial use, substitution, global growth)
- Recent news or events that could influence {commodity}'s price
- Currency fluctuations and overall market sentiment

Clearly explain your reasoning, highlight potential risks, 
and give predictions in plain, easy-to-understand language.

Finally, tailor your analysis toward the purpose: {purpose}.
"""
if st.button("🚀 Run Analysis"):
    with st.spinner("Analyzing market data..."):
        response = model.generate_content([prompt])

    st.success("✅ Analysis Complete!")
    st.markdown("### 📑 Analysis Report")
    st.markdown(response.text)
    st.markdown("### 📊 Quick Insights")
    col1, col2, col3 = st.columns(3)
    col1.metric("Commodity", commodity, "")
    col2.metric("Time Horizon", time.split()[0], "")
    col3.metric("Purpose", purpose, "")
        