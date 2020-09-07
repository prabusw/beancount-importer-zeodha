"""Import configuration file for Zerodha, an Indian stock broker, ICICI Bank, and SBI leading banks in India.
This script is heavily based on the script config.py  by Matt Terwilliger. 
Original script can be found here https://gist.github.com/mterwill/7fdcc573dc1aa158648aacd4e33786e8
in V0.2 added information related to sbi
"""
__copyright__ = "Copyright (C) 2020  Prabu Anand K"
__license__ = "GNU GPLv3"
__Version__ = "0.2"

import os, sys

# beancount doesn't run from this directory
sys.path.append(os.path.dirname(__file__))

# importers located in the importers directory
from importers.icici import icici
from importers.zerodha import zerodha
# The 3722 can be the last four character of your ICICI savings account. By suitably changing you can import from any ICICI account.
# The 3722 can be the last four character of your ICICI savings account. By suitably changing you can import from any ICICI account.
# All the accounts must be declared already in your my.beancount file, to make use of this importer.

CONFIG = [
    icici.IciciBankImporter('Assets:IN:ICICIBank:Savings', '3722'),
    sbi.SBIImporter('Assets:IN:SBI:Savings', '3722'),
    
    zerodha.ZerodhaImporter("INR",
                        "Assets:IN:Investment:Zerodha",
                        "Assets:IN:Investment:Zerodha:Cash",
                        "Income:IN:Investment:Dividend",
                        "Income:IN:Investment:PnL",
                        "Expenses:Financial:Taxes:Zerodha",
                        "Assets:IN:ICICIBank:Savings"),
]
