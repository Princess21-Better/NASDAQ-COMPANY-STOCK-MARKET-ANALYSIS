import streamlit as st
import joblib

# load the model 
model = joblib.load('Stockmarket_model_Lr.model')

col1,col2= st.columns(2)

ticker_symbol =col1.number_input(label = "input the stock ticker_symbol", min_value = 0, max_value = 5)
close_value =col1.number_input(label = "input the stock close_value", min_value =15.800000, max_value =2497.940000)
open_value =col2.number_input(label = "input the stock open_value ", min_value =16.140000, max_value = 2500.000000)
high_value =col1.number_input(label = "input the stock high_value", min_value = 16.630000, max_value = 2525.450000)
low_value =col2.number_input(label = "input the stock low_value", min_value = 14.980000, max_value = 2467.270000)
daily_return =col1.number_input(label ="input the stock daily_return", min_value = -9.053085, max_value = 8.688595)
year =col2.number_input(label ="input the stock year", min_value =2010, max_value = 2020)
day =col1.number_input(label ="input the stock day", min_value = 1, max_value = 31)
month =col2.number_input(label ="input the stock month", min_value = 1, max_value = 12)



#creating button to submit for input  
if st.button('Predict'):
            input_data = [[ticker_symbol,close_value,open_value,high_value,low_value,daily_return,year,day,month]]
            prediction = model.predict(input_data)
     # ensure correct comparison 
            if prediction[0]==1:
                 st.success('The model predicts that the stock value is high')
            else:
                st.warning('This model predicts that the Stock value is low')