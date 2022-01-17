#!/usr/bin/python3
"""
KEK MUST FLOW
"""

import os

import fiobank
import dotenv


# load secrets from .env file
dotenv.load_dotenv()


def kekflow():
    client = fiobank.FioBank(token=os.environ['TOKEN'])

    i = client.info()
    print(f"kekistani treasury: {i['account_number']} / {i['bank_code']}")
    print(f"\nkek balance: {i['balance']} {i['currency']}")

    kekz = client.last(from_date='2022-01-01')
    print("\nkekz:")
    for k in kekz:
        date = k['date']
        d = f"{date.day}.{date.month}.{date.year}"
        print(f"  -  {d}: {k['amount']} from {k['account_name']}")


if __name__ == '__main__':
    kekflow()
