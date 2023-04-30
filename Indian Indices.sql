# create database database_name;
create database Indian_Indices;

# use database_name;
use Indian_Indices;

SHOW databases;

SHOW tables;

CREATE TABLE nifty_50
(
Nifty_id int AUTO_INCREMENT,
Date date,
Day varchar(10) NOT NULL,
Open decimal(7,2) NOT NULL,
Low decimal(7,2) NOT NULL,
High decimal(7,2) NOT NULL,
Close decimal(7,2) NOT NULL,
Day_Change decimal(5,2) NOT NULL,
Change_Prct decimal(3,2) NOT NULL,
inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() ON UPDATE NOW(),
PRIMARY KEY (Nifty_id),
UNIQUE KEY (Date)
);

describe nifty_50;

INSERT INTO nifty_50(Date,Day,Open,High,Low,Close,Day_Change,Change_Prct) 
values('2023-02-07','Tuesday',17790.10,17811.15,17652.55,17721.50,-43.10,-0.24);

INSERT INTO nifty_50(Open,High,Low,Close,Day_Change,Change_Prct) 
values(17031.75,17061.75,16913.75,16951.70,-34,-0.20);

select * from nifty_50;

UPDATE nifty_50 SET Change_Prct=-0.20 WHERE Nifty_id=87;

select count(*) from nifty_50;

select * from nifty_50 where Nifty_id = 4;

update nifty_50 set Nifty_id = 35 where Nifty_id = 39;
update nifty_50 set Nifty_id = 36 where Nifty_id = 40;

CREATE TABLE sensex
(
Sensex_id int AUTO_INCREMENT,
Date date,
Day varchar(10) NOT NULL,
Open decimal(7,2) NOT NULL,
Low decimal(7,2) NOT NULL,
High decimal(7,2) NOT NULL,
Close decimal(7,2) NOT NULL,
Day_Change decimal(6,2) NOT NULL,
Change_Prct decimal(3,2) NOT NULL,
inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() ON UPDATE NOW(),
PRIMARY KEY (Sensex_id),
UNIQUE KEY (Date)
);

describe sensex;

select * from sensex;

INSERT INTO sensex(Date,Day,Open,High,Low,Close,Day_Change,Change_Prct) 
values('2023-02-06','Monday',60847.21,60847.21,60345.61,60506.90,-334.98,-0.55);

INSERT INTO sensex(Date,Day,Open,High,Low,Close,Day_Change,Change_Prct) 
values('2023-02-07','Tuesday',60511.32,60655.14,60063.49,60286.04,-220.86,-0.37);

CREATE TABLE nifty50_companies
(
Serial_id int AUTO_INCREMENT,
Date date,
Day varchar(10) NOT NULL,
Open decimal(7,2) NOT NULL,
High decimal(7,2) NOT NULL,
Low decimal(7,2) NOT NULL,
Close decimal(7,2) NOT NULL,
Day_Change decimal(5,2) NOT NULL,
Change_Prct decimal(3,2) NOT NULL,
inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() ON UPDATE NOW(),
PRIMARY KEY (Serial_id),
UNIQUE KEY (Date)
);

update sensex set Sensex_id = 38 where Sensex_id = 39;

update Bank_Nifty set Bank_Nifty_id = 10 where Bank_Nifty_id = 11;

CREATE TABLE Bank_Nifty
(
Bank_Nifty_id int AUTO_INCREMENT,
Date date,
Day varchar(10) NOT NULL,
Open decimal(7,2) NOT NULL,
Low decimal(7,2) NOT NULL,
High decimal(7,2) NOT NULL,
Close decimal(7,2) NOT NULL,
Day_Change decimal(6,2) NOT NULL,
Change_Prct decimal(3,2) NOT NULL,
inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() ON UPDATE NOW(),
PRIMARY KEY (Bank_Nifty_id),
UNIQUE KEY (Bank_Nifty_id)
);

describe Bank_Nifty;

INSERT INTO Bank_Nifty(Date,Day,Open,High,Low,Close,Day_Change,Change_Prct) 
values('2023-02-07','Tuesday',41513.10,41630.75,41095.10,41490.95,116.30,0.28);

select * from Bank_Nifty;

update Bank_Nifty SET Bank_Nifty_id=38 where Bank_Nifty_id=41;

describe nifty_50;

Insert into nifty_50(Date,Day,Open,Low,High,Close,Day_Change,Change_Prct) values('2022-12-22','Tuesday',17830.40,17967.45,18149.25,18132.30,117.70,0.65);

select * from nifty_50;

select * from Bank_Nifty;

select * from sensex;

select Nifty_id,Date,Day,Open,High,Low,Close,Day_Change,Change_Prct from nifty_50;

update nifty_50 set Day='Tuesday' where Nifty_id=1;

update Bank_Nifty set Day='Tuesday' where Nifty_id=1;

select MIN(Low) as 52_Week_Low FROM nifty_50;

select MAX(High) as 52_Week_High FROM nifty_50;

Select Open AS Open FROM nifty_50 WHERE Date=curdate();

Select High AS Todays_High FROM nifty_50 WHERE Date=curdate();

Select Low AS Todays_Low FROM nifty_50 WHERE Date=curdate();

Select Close AS Todays_Close FROM nifty_50 WHERE Date=curdate();

SELECT Close as Previous_Close FROM nifty_50 WHERE Date=curdate()-1;

SELECT *
, RANK() OVER(ORDER BY Date ASC) AS ranks
, DENSE_RANK() OVER(ORDER BY Date ASC) AS dense_ranks
, ROW_NUMBER() OVER(ORDER BY Date ASC) AS row_numbers
FROM nifty_50;

SELECT 
DENSE_RANK() OVER(ORDER BY Date ASC) AS dense_ranks,Close,     
LAG(Close,1) OVER (   
ORDER BY Date) AS Previous_Close    
FROM nifty_50 WHERE dense_ranks=count(Date)-1; 

self.var_total_investment=DoubleVar()

#Total  Investment
        lbl_total_investment=Label(labelframeleft,text="Total Investment:-",font=("arial",11),padx=2,pady=6)
        lbl_total_investment.grid(row=5,column=0,sticky=W)

        txttotal_investment=ttk.Entry(labelframeleft,width=25,textvariable=self.var_total_investment,font=("arial",11,"bold"))
        txttotal_investment.grid(row=5,column=1,sticky=W)


self.var_total_investment.set("")

def total(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="nava_services")
        my_cursor=conn.cursor()
        my_cursor.execute("select round(SUM(Investment),2) from groww")
        row=my_cursor.fetchone()
        self.var_total_investment.set(row)
        
CREATE TABLE stock_data (
    Serial_id INT PRIMARY KEY AUTO_INCREMENT,
    Symbol VARCHAR(10) NOT NULL,
    Open DECIMAL(10,2),
    High DECIMAL(10,2),
    Low DECIMAL(10,2),
    Ltp DECIMAL(10,2),
    Chng DECIMAL(10,2),
    pct_Chng DECIMAL(10,2),
    Volume INT,
    Status VARCHAR(10),
    Date DATE,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE stock_data
MODIFY COLUMN Symbol VARCHAR(30);

describe stock_data;