# beancount-importers-india

Importer for Banks in India. The code for SBI and ICICI has already been tested and found working for the following banks in India KVB and IOB.

Importer for ICICIBank

If you have account with ICICI Bank, the importer script icici.py can be used. This script is heavily based on the script 
importers-chase.py hosted here  https://gist.github.com/mterwill/7fdcc573dc1aa158648aacd4e33786e8

The default transaction file downloaded in csv format from ICICI Bank website will work as it is with few manual steps as detailed below. 

How to prepare icicibank statement in xls for import as csv

* remove logo and top few rows until the header row
* Change the date format as per yyyy-mm-dd. Then save it as csv in the and the file must be named as icicixxxx.csv,  where xxxx must match the entry in config.py file. 
* For eg. icici3722.csv is a valid name, for the config.py given here. This csv file must be placed in Downloads folder.
* The script icici.py needs to be placed in the folder importers\icici.

Importer for SBI

If you have account with SBI Bank, the importer script sbi.py can be used. This script is heavily based on the script 
importers-chase.py hosted here  https://gist.github.com/mterwill/7fdcc573dc1aa158648aacd4e33786e8

The default transaction file downloaded in csv format from SBI Bank website will work as it is with few manual steps as detailed below. 

How to prepare SBI Bank statement for import

* remove logo and top few rows until the header row
* Change the date format as per yyyy-mm-dd. Then save it as csv in the and the file must be named as sbixxxx.csv,  where xxxx must match the entry in config.py file. 
* For eg. sbi3722.csv is a valid name, for the config.py given here. This csv file must be placed in Downloads folder.
* The script sbi.py needs to be placed in the folder importers\sbi.

Note: The main difference in SBI and ICICI Bank importer code is in the representation of unused value. In ICICI it is given as Zero i.e "0", in SBI it is empty.

Importer for Zerodha

This is an importer for csv formatted tradebook from Indian stock broker Zerodha. Every decent broker in India, gives similar tradebook. 
So this importer can work almost for every broker who provides tradebook in csv format. 

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

Refer to the folder structure presented at the bottom of this document with the above scripts in their respective folders. 

The configuration file is named as config.py and this can be in the same folder as the main beancount file i,e here my.beancount.

Note: There is another importer for Zerodha here at https://github.com/swapi/beancount-utils. It can import xml formatted Digital Contract Note available 
from Zerodha website.



How to Extract data or import data from csv files 

The command(linux) to extract data in a format sutiable for beancount is given below. 

$bean-extract config.py Downloads

Depending on the number of matching csv files available in Downloads folder, the beancount formatted output will be displayed one by one. You can redirect it to new txt file and copy paste it later to my.beancount.To redirect

$bean-extract config.py Downloads > mytxn.txt

<pre>
Sample two line input for zerodha.csv follows:
trade_date	tradingsymbol	exchange	segment	trade_type	quantity	price	    order_id	      trade_id	order_execution_time	amount	  fees
2017-04-13	LIQUIDBEES	    NSE	        EQ	  sell	      30	    999.99	1200000000772831	59283787	2017-04-13T09:54:26	  29999.7	  30
2017-04-13	INFY	          NSE	        EQ	  buy	        3	      941.2	  1100000000419606	26200755	2017-04-13T12:37:32	  2823.6	  2.82
</pre>

The output of above command is given below
<pre>
                               
2017-04-13 * "sell LIQUIDBEES with TradeRef 59283787" ^1200000000772831
  Assets:IN:Investment:Zerodha:LIQUIDBEES      -30 LIQUIDBEES {} @ 999.99 INR
  Expenses:Financial:Taxes:Zerodha              30 INR                       
  Assets:IN:Investment:Zerodha:Cash        29969.7 INR                       
  Income:IN:Investment:PnL:LIQUIDBEES                                        

2017-04-13 * "buy INFY with TradeRef 26200755" ^1100000000419606
  Assets:IN:Investment:Zerodha:INFY     3 INFY {941.2 INR}
  Expenses:Financial:Taxes:Zerodha   2.82 INR             
  Assets:IN:Investment:Zerodha:Cash          
</pre>

This is how the original statement from ICICIBank appears in icici3722.csv after change in date format to YYYY-MM-DD:
<pre>
S No.	 Value Date	 Transaction Date	Cheque Number	Transaction Remarks	                  Withdrawal Amount (INR)	Deposit Amount (INR)	Balance (INR)
1	    2019-04-01	  2019-04-02	                	MPS/SRI AUROBIN/201904011758/012476/	  249.22	                   0                     XX,620.60
2	    2019-04-01	  2019-04-01	 	                MCD REF SRI AUROBINDO UDYO DT 190401	 	  0                       1.87	                 XX,622.47
</pre>

The output of above command is given below
<pre>
2019-04-01 * "MPS/Sri Aurobin/201904011758/012476/" ""
  Assets:IN:ICICIBank:Savings  -249.22 INR

2019-04-04 * "MCD Ref Sri Aurobindo Udyo Dt 190401" ""
  Assets:IN:ICICIBank:Savings  1.87 INR
</pre>


Example folder structure:

<pre>
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
</pre>
