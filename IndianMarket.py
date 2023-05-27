import mysql.connector
import pandas as pd
import streamlit as st
import pymysql
import time
import plotly.graph_objects as go
import plotly.express as px



# Create a connection to the MySQL database
host = "localhost"
user = "root"
password = "MySQL$2022"
database = "indian_indices"

# Connect to the database
mydb = pymysql.connect( 
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to execute queries
cursor = mydb.cursor()

def Indian_Indices():
    # Set the app title
    st.set_page_config(page_title="Indian Indices App", page_icon="🧊")

    # Create the sidebar menu
    menu = ['Home','Nifty50', 'Bank Nifty', 'Sensex', 'View Nifty50 Data']
    choice = st.sidebar.selectbox("Select a page",menu)

    def process_request():
        with st.spinner(f"Firing up the database engines....get ready for takeoff...!"):
            time.sleep(10)
            st.success("Nifty50 data successfully added to the database!")

    # Show the appropriate page based on user choice
    if choice == 'Home':
        st.title('Welcome to the Indian Indices App!')
        st.write('This is a simple application built with Streamlit that allows users to input Nifty50 data and store it in a database.')
        # https://www.nseindia.com/assets/images/logo_nifty50.png

    elif choice == 'Nifty50':
        st.title('Add Nifty50 Data')
        with st.form(key='columns_in_form'):
            c1, c2 = st.columns(2)

            with c1:
                date_input = st.date_input("Enter a date")
            
            with c2:
                day_input = st.selectbox("Select a Day from dropdown",["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

        #with st.form(key1='columns_in_form'):
            c3, c4 = st.columns(2)
            with c3:
                open_input = st.number_input("Enter a Open Value")

            with c4:
                high_input = st.number_input("Enter a High Value")

        #with st.form(key2='columns_in_form'):
            c5, c6 = st.columns(2)
            with c5:
                low_input = st.number_input("Enter a Low Value")

            with c6:
                close_input = st.number_input("Enter a Close Value")

        #with st.form(key3='columns_in_form'):
            c7, c8 = st.columns(2)
            with c7:
                day_change_input = st.number_input("Enter a Day Change Value")

            with c8:
                day_changeper_input = st.number_input("Enter a Day Change Percent Value")

            #Add a button to submit the data to the database

            if st.form_submit_button("Submit"):
                cursor.execute("INSERT INTO nifty_50(Date, Day, Open, High, Low, Close, Day_Change, Change_Prct) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(date_input,day_input,open_input,high_input,low_input,close_input,day_change_input,day_changeper_input))
                mydb.commit()
                process_request()

        st.title("View Nifty50 Data")
        # Retrive nifty50 data from the database
        # Example query - select all rows from a table
        query = 'SELECT Nifty_id, Date, Day, Open, High, Low, Close, Day_Change, Change_Prct FROM nifty_50 ORDER BY Nifty_id ASC'
        cursor.execute(query)

        # Fetch the data returned by the SQL query using the curser
        data = cursor.fetchall()

        # Create a Dataframe from the data
        df = pd.DataFrame(list(data),columns=[desc[0] for desc in cursor.description])

        df=df.set_index('Nifty_id')

        # Format negative values
        df['Day_Change'] = df['Day_Change'].apply(lambda x: '-{:,.2f}'.format(abs(x)) if x < 0 else '{:,.2f}'.format(x))
        df['Change_Prct'] = df['Change_Prct'].apply(lambda x: '-{:,.2f}'.format(abs(x)) if x < 0 else '{:,.2f}'.format(x))

        # Display the DataFrame with column names
        st.write(df)

        # display a horizontal separator line
        st.markdown('---')

        # get the total number of rows
        num_rows = df.shape[0]
        st.subheader(f'The dataset contains {num_rows} rows.')

        # display a horizontal separator line
        st.markdown('---')

        query = 'SELECT Date, Day_Change FROM nifty_50 ORDER BY Date ASC'
        cursor.execute(query)

        # Fetch the data returned by the SQL query using the curser
        datadc = cursor.fetchall()

        # Create a Dataframe from the data
        dfdc = pd.DataFrame(list(datadc),columns=[desc[0] for desc in cursor.description])

         # Format negative values
        dfdc['Day_Change'] = dfdc['Day_Change'].apply(lambda x: '-{:,.2f}'.format(abs(x)) if x < 0 else '{:,.2f}'.format(x))

        # Display the DataFrame with column names
        st.write(dfdc)


        # Define your data
        x = df['Date']
        y = df['Day_Change']

        # Define a color scale
        color_scale = [
    [0, 'rgb(255, 0, 0)'],   # Red
    #[0.5, 'rgb(255, 255, 0)'],   # Yellow
    [1, 'rgb(0, 255, 0)']   # Green
]

        # Set the color scale domain to span the full range of y values
        color_scale_domain = [min(y), max(y)]

        # Create a trace with color based on value
        trace = go.Bar(x=x, y=y, marker=dict(color=y, colorscale=color_scale, cmin=color_scale_domain[0], cmax=color_scale_domain[1]))

        # Create a layout
        layout = go.Layout(
    title='Nifty Value Changes Overview',
    xaxis=dict(title="Date"),
    yaxis=dict(title="Value Change")
)

        # Create a figure and add the trace and layout
        fig = go.Figure(data=[trace], layout=layout)

        # Display the chart using plotly
        fig.show()


        # Create a candlestick chart with the Open, High, Low, and Close prices
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'],
                                     increasing_line_color='royalblue',
                                     decreasing_line_color='red')])

        # Add title and axis labels
        fig.update_layout(title='Nifty 50 Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Price')

        # Add a line chart with the Open prices
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Open'],
                         mode='lines', line=dict(color='royalblue'),
                         name='Open'))

        # Add a line chart with the High prices
        fig.add_trace(go.Scatter(x=df['Date'], y=df['High'],
                         mode='lines', line=dict(color='green'),
                         name='High'))

        #  Add a line chart with the Low prices
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Low'],
                         mode='lines', line=dict(color='red'),
                         name='Low'))

        # Add a line chart with the Close prices
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'],
                         mode='lines', line=dict(color='gold'),
                         name='Close'))

        # Display the chart in Streamlit
        st.plotly_chart(fig)


        # Create a candlestick chart with the Open, High, Low, and Close prices
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'],
                                     increasing_line_color='royalblue',
                                     decreasing_line_color='red')])

        # Add title and axis labels
        fig.update_layout(title='Nifty 50 Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Close Price')

        
        # Add a line chart with the Close prices
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'],
                         mode='lines', line=dict(color='gold'),
                         name='Close'))

        # Display the chart in Streamlit
        st.plotly_chart(fig)


        # Create a candlestick chart with the Open, High, Low, and Close prices
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     close=df['Close'],
                                     increasing_line_color='royalblue',
                                     decreasing_line_color='red')])

        # Add title and axis labels
        fig.update_layout(title='Nifty 50 Closing Chart',
                  xaxis_title='Date',
                  yaxis_title='Close Price')

        
        # Add a line chart with the Close prices
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'],
                         mode='lines', line=dict(color='royalblue'),
                         name='Close'))

        # Display the chart in Streamlit
        st.plotly_chart(fig)

        # display a horizontal separator line
        st.markdown('---')

        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     close=df['Close'],
                                     increasing_line_color='royalblue',
                                     decreasing_line_color='red')])

        fig.update_layout(title='Nifty 50 Closing Chart',
                  xaxis_title='Date',
                  yaxis_title='Close Price',
                  xaxis_rangeslider_visible=True)

        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'],
                         mode='lines', line=dict(color='royalblue'),
                         name='Close'))

        st.plotly_chart(fig)
        # display a horizontal separator line
        st.markdown('---')

        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     close=df['Close'],
                                     increasing_line_color='royalblue',
                                     decreasing_line_color='red')])

        fig.update_layout(title='Nifty 50 Closing Chart',
                  xaxis_title='Date',
                  yaxis_title='Close Price')

        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'],
                         mode='lines', line=dict(color='royalblue'),
                         name='Close'))

        # Find the highest and lowest value of Close
        max_close = df['Close'].max()
        min_close = df['Close'].min()

        # Add annotations for the highest and lowest value of Close
        fig.add_annotation(x=df.loc[df['Close'] == max_close, 'Date'].iloc[0],
                   y=max_close,
                   text=f"Highest Close: {max_close:.2f}",
                   showarrow=True,
                   arrowhead=1,
                   ax=-50,
                   ay=-50)
        fig.add_annotation(x=df.loc[df['Close'] == min_close, 'Date'].iloc[0],
                   y=min_close,
                   text=f"Lowest Close: {min_close:.2f}",
                   showarrow=True,
                   arrowhead=1,
                   ax=50,
                   ay=50)

        st.plotly_chart(fig)

        # Compute the difference between the high and low columns
        diff = df['High'] - df['Low']

        # Add the difference column to the DataFrame
        df['Diff'] = diff

        # Create a bar chart of the differences
        fig = go.Figure(data=[go.Bar(x=df['Date'], y=df['Diff'], marker_color='royalblue')])

        fig.update_layout(title='Difference between Day High and Day Low',
                  xaxis_title='Date',
                  yaxis_title='Difference')

        st.plotly_chart(fig)



        # Close the cursor and connection
        cursor.close()
        mydb.close()

        
            

            #Insert the data into the database
            #query = 'INSERT INTO nifty_50(Date, Day, Open, High, Low, Close, Day_Change, Change_Prct) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(date_input,day_input,open_input,high_input,low_input,close_input,day_change_input,day_changeper_input)
            
            
            #sql="insert into nifty_50(Date, Day, Open, High, Low, Close, Day_Change, Change_Prct)values(%s,%s,%s,%s,%s,%s,%s,%s)"
            #player1=[(date_input,day_input,open_input,high_input,low_input,close_input,day_change_input,day_changeper_input),]
            #cursor.execute('INSERT INTO nifty_50(Date, Day, Open, High, Low, Close, Day_Change, Change_Prct) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(date_input,day_input,open_input,high_input,low_input,close_input,day_change_input,day_changeper_input))
            #cursor.execute(sql,player1)

    elif choice == 'Bank Nifty':
        st.title('Add Bank Nifty Data')
        with st.form(key='columns_in_form'):
            c1, c2 = st.columns(2)

            with c1:
                date_input = st.date_input("Enter a date")
            
            with c2:
                day_input = st.selectbox("Select a Day from dropdown",["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

        #with st.form(key1='columns_in_form'):
            c3, c4 = st.columns(2)
            with c3:
                open_input = st.number_input("Enter a Open Value")

            with c4:
                high_input = st.number_input("Enter a High Value")

        #with st.form(key2='columns_in_form'):
            c5, c6 = st.columns(2)
            with c5:
                low_input = st.number_input("Enter a Low Value")

            with c6:
                close_input = st.number_input("Enter a Close Value")

        #with st.form(key3='columns_in_form'):
            c7, c8 = st.columns(2)
            with c7:
                day_change_input = st.number_input("Enter a Day Change Value")

            with c8:
                day_changeper_input = st.number_input("Enter a Day Change Percent Value")

            #Add a button to submit the data to the database

            if st.form_submit_button("Submit"):
                cursor.execute("INSERT INTO bank_nifty(Date, Day, Open, High, Low, Close, Day_Change, Change_Prct) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(date_input,day_input,open_input,high_input,low_input,close_input,day_change_input,day_changeper_input))
                mydb.commit()

        st.title("View Bank Nifty Data")
        # Retrive nifty50 data from the database
        # Example query - select all rows from a table
        query = 'SELECT Bank_Nifty_id, Date, Day, Open, High, Low, Close, Day_Change, Change_Prct FROM bank_nifty'
        cursor.execute(query)

        # Fetch the data returned by the SQL query using the curser
        data = cursor.fetchall()

        # Create a Dataframe from the data
        df = pd.DataFrame(list(data),columns=[desc[0] for desc in cursor.description])

        df=df.set_index('Bank_Nifty_id')

        # Format negative values
        df['Day_Change'] = df['Day_Change'].apply(lambda x: '-{:,.2f}'.format(abs(x)) if x < 0 else '{:,.2f}'.format(x))
        df['Change_Prct'] = df['Change_Prct'].apply(lambda x: '-{:,.2f}'.format(abs(x)) if x < 0 else '{:,.2f}'.format(x))

        #print(df.columns)

        # Display the DataFrame with column names
        st.write(df)

        # Close the cursor and connection

        cursor.close()
        mydb.close()


    elif choice == 'Sensex':
        st.title('Add Sensex Data')
        with st.form(key='columns_in_form'):
            c1, c2 = st.columns(2)

            with c1:
                date_input = st.date_input("Enter a date")
            
            with c2:
                day_input = st.selectbox("Select a Day from dropdown",["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

        #with st.form(key1='columns_in_form'):
            c3, c4 = st.columns(2)
            with c3:
                open_input = st.number_input("Enter a Open Value")

            with c4:
                high_input = st.number_input("Enter a High Value")

        #with st.form(key2='columns_in_form'):
            c5, c6 = st.columns(2)
            with c5:
                low_input = st.number_input("Enter a Low Value")

            with c6:
                close_input = st.number_input("Enter a Close Value")

        #with st.form(key3='columns_in_form'):
            c7, c8 = st.columns(2)
            with c7:
                day_change_input = st.number_input("Enter a Day Change Value")

            with c8:
                day_changeper_input = st.number_input("Enter a Day Change Percent Value")

            #Add a button to submit the data to the database

            if st.form_submit_button("Submit"):
                cursor.execute("INSERT INTO sensex(Date, Day, Open, High, Low, Close, Day_Change, Change_Prct) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(date_input,day_input,open_input,high_input,low_input,close_input,day_change_input,day_changeper_input))
                mydb.commit()
                process_request()

        st.title("View Sensex Data")
        # Retrive nifty50 data from the database
        # Example query - select all rows from a table
        query = 'SELECT Sensex_id, Date, Day, Open, High, Low, Close, Day_Change, Change_Prct FROM sensex order by Sensex_id asc,Date '
        cursor.execute(query)

        # Fetch the data returned by the SQL query using the curser
        data = cursor.fetchall()

        # Create a Dataframe from the data
        df = pd.DataFrame(list(data),columns=[desc[0] for desc in cursor.description])

        df=df.set_index('Sensex_id')

        # Format negative values
        df['Day_Change'] = df['Day_Change'].apply(lambda x: '-{:,.2f}'.format(abs(x)) if x < 0 else '{:,.2f}'.format(x))
        df['Change_Prct'] = df['Change_Prct'].apply(lambda x: '-{:,.2f}'.format(abs(x)) if x < 0 else '{:,.2f}'.format(x))

        #print(df.columns)

        # Display the DataFrame with column names
        st.write(df)

        # Close the cursor and connection

        cursor.close()
        mydb.close()
        
    
    elif choice == 'View Nifty50 Data':
        st.title("View Nifty50 Data")
        # Retrive nifty50 data from the database
        # Example query - select all rows from a table
        query = 'SELECT Nifty_id, Date, Day, Open, High, Low, Close, Day_Change, Change_Prct FROM nifty_50'
        cursor.execute(query)

        # Fetch the data returned by the SQL query using the curser
        data = cursor.fetchall()

        # Create a Dataframe from the data
        df = pd.DataFrame(list(data),columns=[desc[0] for desc in cursor.description])

        df=df.set_index('Nifty_id')

        # Format negative values
        df['Day_Change'] = df['Day_Change'].apply(lambda x: '-{:,.2f}'.format(abs(x)) if x < 0 else '{:,.2f}'.format(x))
        df['Change_Prct'] = df['Change_Prct'].apply(lambda x: '-{:,.2f}'.format(abs(x)) if x < 0 else '{:,.2f}'.format(x))

        #print(df.columns)

        # Display the DataFrame with column names
        st.write(df)

        # Close the cursor and connection

        cursor.close()
        mydb.close()

# Run the app
if __name__=='__main__':
    Indian_Indices()
