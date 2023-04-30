import mysql.connector
import pandas as pd
import streamlit as st
import pymysql
import time

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

        #print(df.columns)

        # Display the DataFrame with column names
        st.write(df)

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
        query = 'SELECT Sensex_id, Date, Day, Open, High, Low, Close, Day_Change, Change_Prct FROM sensex'
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
