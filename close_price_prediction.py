

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:38:43 2023

@author: NONZOOU
"""

"""Description
This program uses an artificial rucurrent neural network called Long Short Term Memory (LSTM)
To predict the closing price stock of a corporation (Apple Inc.) using the past 60 days stock price
"""
# =============================================================================
# import the librairies
# =============================================================================

import math
import numpy as np
import pandas_datareader as web
import pandas as pn
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

import yfinance as yf

# Specify the stock symbol and date range
stock_symbol = 'AAPL'
#stock_symbol = 'GBPUSD=X'
start_date = '2010-01-01'
# Fetch the data from Yahoo Finance
df = yf.download(stock_symbol, start=start_date)
# Print the DataFrame
print(df)

# =============================================================================
# Visualize the closing price history
# =============================================================================
plt.figure(figsize=(16, 8))
plt.title('Closed Price History')
plt.plot(df['Close'], color ='red')
#plt.plot(df['Open'], color ='blue')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)',fontsize=18)
plt.grid(False)
plt.show()

# =============================================================================
# Create a new dataframe with only the 'close column'
# =============================================================================
close_data = df.filter(['Close'])
#convert the dataframe to a numpy array
dataset = close_data.values
# get the number of rows to train the model on
training_data_len = math.ceil(len(dataset)*.8)
print(training_data_len)

# scaler the data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data= scaler.fit_transform(dataset)
#print(scaled_data)

#create the training dataset
# create the scaled training dataset
train_data = scaled_data[0:training_data_len, :]

#split the data into x_train and y_train datasets
x_train =[]
y_train = []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i,0])
    if i<=60 :
        print(x_train)
        print(y_train)
        print()

# convert the x_train and y_train to numpy arrays
x_train, y_train = np.array(x_train), np.array(y_train)
# reshape the data
x_train=np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
print(x_train.shape)

# building the LSTM model
model =Sequential()
model.add(LSTM(50, return_sequences=True, input_shape =(x_train.shape[1],1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
#☻ to compile it using an optimizer and a loss function
model.compile(optimizer='adam', loss='mean_squared_error')
#model traning 
model.fit(x_train, y_train, batch_size=1, epochs=1)

# create the testing datasets
#ccreate a new array containing scaler values from 2736 to 3495
test_data = scaled_data[training_data_len-60 : , : ]
#create the datasets x_test  and y_test 
x_test = []
y_test =dataset[training_data_len :, :]

for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])
    
#convert the data to a numpy array
x_test=np.array(x_test)
# reshape the data
x_test= np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
#get the models predicted price values
predictions =model.predict(x_test)
predictions=scaler.inverse_transform(predictions)

# get the root mean squard error (RMSE)
rmse = np.sqrt(np.mean(predictions-y_test)**2)
print(rmse)

# plot the data 
# plot the data
train = close_data[:training_data_len]
valid = close_data[training_data_len:].copy()  # Create a copy to avoid SettingWithCopyWarning
valid.loc[:, 'Predictions'] = predictions  # Use loc to modify the copy

# visualize the data
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date', fontsize = 18)
plt.ylabel('Close Price USD ($', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc ='lower right')
plt.show()

#show the valid and predicted prices
print(valid)

#get the quote
apple_quote =yf.download('AAPL', start='2010-01-01')
# create a new dataframe
new_df = apple_quote.filter(['Close'])
#get the last 60 days closing price values and convert the dataframe to an array
last_60_days_ = new_df[-60:].values
#scale the data to be values between 0 and 1
last_60_days_scaled = scaler.transform(last_60_days_)
#create an empty list
X_test= []
#append the past 60 days
X_test.append(last_60_days_scaled)
#convert the X_test data set to a numpy array
X_test=np.array(X_test)
#Reshape the data
X_test=np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
#get the predicted scaled price
pred_prcie = model.predict(X_test)
#undo the scaling
pred_prcie=scaler.inverse_transform(pred_prcie)
print(pred_prcie)

 
# get the last date in the existing dataset
last_date = df.index[-1]

# get the quote for the next day
next_day_quote = yf.download('AAPL', start=last_date + pn.Timedelta(days=1), end=last_date + pn.Timedelta(days=1))
print(next_day_quote)
