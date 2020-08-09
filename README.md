# beancount-importer-zeodha

Note: Please click on Raw option on the righthand corner to view this README in a better format.

This is an importer for csv formatted tradebook from Indias leading stock broker Zerodha. Every decent broker in India, gives similar file. 
So this can work almost for every broker who provides tradebook in csv format. 
This importer zerodha.py is based almost entirely on the sample csv importer "utrade_csv.py" provided by the Beancount author Martin Blais.

The default csv formatted tradebook from Zerodha has the following fields: 
trade_date	tradingsymbol	exchange	segment	trade_type	quantity	price	order_id	trade_id	order_execution_time

For the importer to work, you need to manually add the following fields amount, fees either in Google sheets or Openoffice or other such spreadsheet software.

The formula for amount = quantity*price and for fees = amount*0.001 rounded to 2 decimal places. 

In openoffice,
formula for amount(column k) appears as =F2*G2, where columns F and G are quantity and price respectively.
forumla for fees(column L) appears as=round(k2*0.001,2).

With the above two changes done, make sure the csv file is named as zerodhayyyymmdd.csv format. For example, zerodha20200401.csv is a valid filename. 

This csv must be placed in Downloads folder at the root of beancount.

The script zerodha.py must be placed in the following folder importers\zerodha at the root of beancount. 

Refer to the directory structure presented below as recommened in Beancount documentation with the above scripts in their respective folders.

The configuration file is named as config.py and this can be in the same folder as the main beancount file i,e here my.beancount.

If you have account with ICICI Bank, the importer script icici.py can be used. It needs to be placed in the folder importers\icici. For this import script too, 
the appropriate data file icici3722.csv must be placed in Downloads folder. 
This script icici.py is heavily based on the script importers-chase.py hosted here  https://gist.github.com/mterwill/7fdcc573dc1aa158648aacd4e33786e8

The command(linux) to extract data in a format sutiable for beancount is 

$bean-extract config.py Downloads

├── config.py
├── documents
│   ├── Assets
│   │   └── IN
│   │       ├── ICICIBank
│   │       │   └── Savings
│   │       │       ├── Icici3722-fy2017-18.CSV
│   │       ── Zerodha
│   │           ├── tradebook_2017-04-01_to_2018-03-31.csv
│   ├── Expenses
│   │   
│   ├── Income
│   │   
│   └── Liabilities
├── Downloads
│   ├── icici3722.csv
│   ├── zerodha20170401.csv
│   
├── importers
│   ├── icici
│   │   ├── icici.py
│   │   ├── __init__.py
│   └── zerodha
│       ├── __init__.py
│       └── zerodha.py
├── my.beancount

A sample two line input for zerodha csv follows:
trade_date	tradingsymbol	exchange	segment	trade_type	quantity	price	order_id	trade_id	order_execution_time	amount	fees
2017-04-13	LIQUIDBEES	NSE	EQ	sell	30	999.99	1200000000772831	59283787	2017-04-13T09:54:26	29999.7	30
2017-04-13	INFY	NSE	EQ	buy	3	941.2	1100000000419606	26200755	2017-04-13T12:37:32	2823.6	2.82
The output of above command is given below
                               
2017-04-13 * "sell LIQUIDBEES with TradeRef 59283787" ^1200000000772831
  Assets:IN:Investment:ILFSSS:LIQUIDBEES      -30 LIQUIDBEES {} @ 999.99 INR
  Expenses:Financial:Taxes:Zerodha             30 INR                       
  Assets:IN:Investment:Zerodha:Cash       29969.7 INR                       
  Income:IN:Investment:PnL:LIQUIDBEES                                       

2017-04-13 * "buy INFY with TradeRef 26200755" ^1100000000419606
  Assets:IN:Investment:ILFSSS:INFY      3 INFY {941.2 INR}
  Expenses:Financial:Taxes:Zerodha   2.82 INR             
  Assets:IN:Investment:Zerodha:Cash             





