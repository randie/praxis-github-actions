#! /usr/bin/env python

from datetime import datetime

TODAY = datetime.now().strftime("%a %x")

if __name__ == "__main__":
    print(f"Today is {TODAY}")
