import os, sys

# beancount doesn't run from this directory
sys.path.append(os.path.dirname(__file__))

# importers located in the importers directory
from importers.icici import icici
from importers.zerodha import zerodha

CONFIG = [
    icici.IciciBankImporter('Assets:IN:ICICIBank:Savings', '3722'),

    zerodha.ZerodhaImporter("INR",
                        "Assets:IN:Investment:ILFSSS",
                        "Assets:IN:Investment:Zerodha:Cash",
                        "Income:IN:Investment:Dividend",
                        "Income:IN:Investment:PnL",
                        "Expenses:Financial:Taxes:Zerodha",
                        "Assets:IN:ICICIBank:Savings"),
]
