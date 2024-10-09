import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import yfinance as yf
import plotly.express as px
import streamlit as st

# Mapping of company names to ticker symbols
st.title('Stock Market Analysis')
st.markdown(">***Smart Analysis for Informed Investing***")
st.markdown('***')
#Sidebar 
st.sidebar.markdown("# Choose Your Interested Stocks")
ticket_values=None
#Options_items 200 Stock_symbols
options_items=['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'HDFC.NS',
               'BAJFINANCE.NS', 'SBIN.NS', 'BHARTIARTL.NS', 'KOTAKBANK.NS', 'WIPRO.NS',
                  'HCLTECH.NS', 'ASIANPAINT.NS', 'DMART.NS', 'ITC.NS', 'BAJAJFINSV.NS', 'LT.NS', 
                  'AXISBANK.NS', 'MARUTI.NS', 'ULTRACEMCO.NS', 'TITAN.NS', 'SUNPHARMA.NS',
                    'NESTLEIND.NS', 'ADANIGREEN.NS', 'ONGC.NS', 'ADANIENT.NS', 'ADANITRANS.NS', 
                    'JSWSTEEL.NS', 'TATASTEEL.NS', 'ATGL.NS', 'ADANIPORTS.NS', 'HDFCLIFE.NS', 
                    'TECHM.NS', 'TATAMOTORS.NS', 'HINDZINC.NS', 'POWERGRID.NS', 'DIVISLAB.NS', 
                    'NTPC.NS', 'PIDILITIND.NS', 'VEDL.NS', 'SBILIFE.NS', 'IOC.NS', 'ZOMATO.NS',
                      'GRASIM.NS', 'BAJAJ-AUTO.NS', 'DABUR.NS', 'NYKAA.NS', 'M&M.NS', 'LTI.NS',
                        'GODREJCP.NS', 'HINDALCO.NS', 'SHREECEM.NS', 'PAYTM.NS', 'SBICARD.NS', 'COALINDIA.NS', 
                        'BPCL.NS', 'DLF.NS', 'ICICIPRULI.NS', 'BRITANNIA.NS', 'HAVELLS.NS', 'DRREDDY.NS',
                          'INDUSINDBK.NS', 'AMBUJACEM.NS', 'SIEMENS.NS', 'BERGEPAINT.NS', 'NAUKRI.NS', 'CIPLA.NS', 
                          'INDIGO.NS', 'TATACONSUM.NS', 'EICHERMOT.NS', 'MOTHERSUMI.NS', 'ICICIGI.NS', 'INDUSTOWER.NS', 
                          'MARICO.NS', 'APOLLOHOSP.NS', 'MINDTREE.NS', 'GAIL.NS', 'GLAND.NS', 'PEL.NS', 'MUTHOOTFIN.NS', 
                          'HDFCAMC.NS', 'SRF.NS', 'UNITDSPR.NS', 'UPL.NS', 'IRCTC.NS', 'TATAPOWER.NS', 'MPHASIS.NS', 'CADILAHC.NS',
                            'HEROMOTOCO.NS', 'GODREJPROP.NS', 'TORNTPHARM.NS', 'POLICYBZR.NS', 'BAJAJHLDNG.NS', 'JUBLFOOD.NS', 
                            'SAIL.NS', 'LODHA.NS', 'BEL.NS', 'IDBI.NS', 'JSWENERGY.NS', 'BANDHANBNK.NS', 'LTTS.NS', 'BOSCHLTD.NS', 
                            'STARHEALTH.NS', 'PIIND.NS', 'GUJGASLTD.NS', 'BALKRISIND.NS', 'CHOLAFIN.NS', 'PGHH.NS', 'AUROPHARMA.NS',
                              'NMDC.NS', 'LUPIN.NS', 'BANKBARODA.NS', 'BIOCON.NS', 'COLPAL.NS', 'PNB.NS', 'ASTRAL.NS', 'ALKEM.NS', 
                              'ACC.NS', 'HAL.NS', 'HINDPETRO.NS', 'ABBOTINDIA.NS', 'IOB.NS', 'UBL.NS', 'CONCOR.NS', 'ABB.NS', 'JINDALSTEL.NS',
                                'PAGEIND.NS', 'TATACOMM.NS', 'ADANIPOWER.NS', 'DALBHARAT.NS', 'ASHOKLEY.NS', 'VOLTAS.NS', 'OFSS.NS', 
                                'SRTRANSFIN.NS', 'VBL.NS', 'HONAUT.NS', 'AUBANK.NS', 'IGL.NS', 'TRENT.NS', 'BHARATFORG.NS', 'MFSL.NS', 
                                'SONACOMS.NS', 'PFC.NS', 'AARTIIND.NS', 'PETRONET.NS', 'MAXHEALTH.NS', 'MRF.NS', 'TATAELXSI.NS',
                                  'POLYCAB.NS', 'KANSAINER.NS', 'LAURUSLABS.NS', 'YESBANK.NS', 'CANBK.NS', 'COFORGE.NS', 'DEEPAKNI.NS',
                                    'RELAXO.NS', 'LALPATHLAB.NS', 'IRFC.NS', 'IDFCFIRSTB.NS', 'RUCHISOYA.NS', 'OBEROIRLTY.NS', 'NHPC.NS',
                                      'RECLTD.NS', 'IDEA.NS', 'CROMPTON.NS', 'TVSMOTOR.NS', 'SUPREMEIND.NS', 'IPCALAB.NS', 'PERSISTENT.NS',
                                        'DIXON.NS', '3MINDIA.NS', 'UNIONBANK.NS', 'SUNDARMFIN.NS', 'TIINDIA.NS', 'ATUL.NS', 'WHIRLPOOL.NS', 
                                        'ABCAPITAL.NS', 'GLAXO.NS', 'GICRE.NS', 'HATSUN.NS', 'ZEEL.NS', 'NIACL.NS', 'CUMMINSIND.NS', 
                                        'JKCEMENT.NS', 'PFIZER.NS', 'NAM-INDIA.NS', 'EMAMILTD.NS', 'SYNGENE.NS', 'TORNTPOWER.NS', 'ISEC.NS', 
                                        'BANKINDIA.NS', 'RAMCOCEM.NS', 'COROMANDEL.NS', 'ENDURANCE.NS', 'BAYERCROP.NS', 'BATAINDIA.NS',
                                          'INDIAMART.NS', 'MINDAIND.NS', 'SCHAEFFLER.NS']
#------
ticker_values=st.sidebar.multiselect("Top 200 NSE Stocks Available",options=options_items,max_selections=5)
combine_data=pd.DataFrame()
#Date Structure
end_value=datetime.now().date()
slider_total_date=st.sidebar.slider("Number of Days to go back from today",min_value=1,max_value=365,value=90)
start_value = (pd.to_datetime(end_value) - pd.tseries.offsets.BDay(slider_total_date)).date()
selected_start_date = st.sidebar.selectbox("Start Date", [start_value], index=0)
selected_end_date = st.sidebar.selectbox("End Date", [end_value], index=0)


#Fetching Data
def fetch_data(stock_values):
    global combine_data
    for stock in stock_values:
        try:
            get_data=yf.download(stock,start=start_value,end=end_value)
            if get_data.empty:
                st.warning(f"Please try selecting again. If it still doesn't work, apologies for the inconvenience, no data is available for {stock} right now. We are working to gather the necessary data.")
                continue
            get_data['stocks']=stock
            get_data=get_data.dropna()
            combine_data=pd.concat([combine_data,get_data])
        except Exception as e:
            st.warning(f"Error fetching data for {stock}")

if not ticker_values:
    st.warning("Please select at least one stock to analyze.")
else:
    # Proceed with data fetching and analysis
    fetch_data(ticker_values)
    if combine_data.empty:
        st.error('Please select some other stock for analysis')
    else:
    # Proceed with the rest of your analysis and visualizations...

           #Displaying the Selected Stocks
        selected_stocks=combine_data['stocks'].value_counts().reset_index()
        selected_stocks.columns=selected_stocks.columns.str.replace('stocks','Selected Stocks')
        # Set the index to start from 1
        selected_stocks.index = selected_stocks.index + 1
        st.write("### *Stock Data retrived from your selection*")
        st.dataframe(selected_stocks.iloc[:,0])
        st.write('***')
        st.write("")

       #Overview of Data
        st.write("### *Overview*")
        st.write('')
        combine_data = combine_data.round(2)
        head_10 = combine_data.head(10)
        st.write(head_10)
        st.write('***')
        st.write("")
    # Change into lower case 
        combine_data.columns = combine_data.columns.str.lower()
 
        try:
###############################################

            #Descriptive Analysis
            st.markdown('### *Descriptive Analysis*')
            st.write('')
            combine_data_pivot=combine_data.pivot_table(index='Date',columns='stocks',values='close')
            describe_table=combine_data_pivot.describe().round(2)
            st.write(describe_table)

            st.markdown('***')
            st.write("")

            #Stock Prices Line Plot
            st.markdown("### *Stock Price Overview*")
            combine_data_no_index=combine_data
            combine_data_no_index=combine_data_no_index.reset_index()
            fig=px.line(combine_data_no_index,x='Date',y='close',color='stocks')
            fig.update_layout(xaxis_title='Date',yaxis_title='Close')
            st.plotly_chart(fig)

            st.markdown('***')
            st.write("")

            #Volatility Analysis
            st.markdown("### *Volatility Analysis*")
            st.markdown(f'> The change in prices (standard deviation of returns) of stocks over the last {slider_total_date} days.')
            stocks_group=combine_data.groupby('stocks')['close'].describe()['std'].round(2)
            stocks_group=stocks_group.reset_index()
            #Volatility Analysis-Bar Chart
            fig=px.bar(stocks_group,x='stocks',y='std',text='std')
            fig.update_layout(xaxis_title='Stock',yaxis_title='Standard Deviation')
            fig.update_traces(textposition='outside', textfont=dict(size=12)) 
            st.plotly_chart(fig)

            st.markdown('***')
            st.write("")


            #Heatmap
            st.markdown('### *Heat Map*')
            st.write('> Correlation of the Stocks')
            corr_table=combine_data_pivot.corr()
            corr_table=corr_table.round(3)
            #Heatmap - Chart
            fig=px.imshow(corr_table,text_auto=True,color_continuous_scale='Viridis')
            st.plotly_chart(fig)

            st.markdown('***')
            st.write("")


            #Comparative Analysis
            st.markdown('### *Comparative Analysis*')
            st.markdown(f'> % Of Prices Changes in last {slider_total_date} days')
            percentage_changes=((combine_data_pivot.iloc[-1]-combine_data_pivot.iloc[0])/combine_data_pivot.iloc[0])*100
            percentage_change=percentage_changes.round(2)
            #Comparative Analysis - Bar Chart
            fig=px.bar(percentage_change,x=percentage_change.index,
                    y=percentage_change.values,
                    text=percentage_change.values)
            fig.update_layout(xaxis_title='Stocks',yaxis_title='Prices Change')
            # Add percentage symbols to text values in the bar chart
            fig.for_each_trace(lambda t: t.update(text=[f"{value}%" for value in t.text]))
            fig.update_traces(textposition='outside')
            st.plotly_chart(fig)

            st.markdown('***')
            st.write('')


            #Risk and Return Analysis
            st.markdown("### *Risk and Return Analysis*")
            st.markdown(f'>  The risk (standard deviation of returns) and average daily return over the last {slider_total_date} days.')

            daily_return=combine_data_pivot.pct_change().dropna()
            average_daily_return=daily_return.mean()
            risk=daily_return.std()
            risk_return=pd.DataFrame({'Risk':risk,'Average Daily Return':average_daily_return})
            #Risk and Return Analysis - Scatter Plot Chart
            fig = px.scatter(
                risk_return,
                x='Risk',
                y='Average Daily Return',
                text=risk_return.index,  
                labels={
                    'Risk': 'Risk (Standard Deviation)',
                    'Average Daily Return': 'Average Daily Return'
                })
            fig.update_traces(marker=dict(size=10))  
            fig.update_traces(textposition='top center')
            st.plotly_chart(fig)

            st.markdown('***')
            st.write('')
        except KeyError:
             # Custom message for KeyError
            st.error("There is something wrong on our end. We will rectify it as soon as possible. Sorry for the inconvenience.")
        
    