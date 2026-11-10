# Workshop Energy Cost Estimator

## What it does
This program asks for each workshop machine's name, power in watts and hours used per day. It then calculates the daily and monthly energy use in kWh and the monthly cost at the tariff you enter. It checks your input and asks again if you type something wrong.

## How to run it
Install Python 3, then run: python workshop_energy_cost_estimator.py

## Sample output
```
=== Workshop Energy Cost Estimator ===
How many machines do you have? 2

Machine 1 of 2
  Name: Lathe
  Power in watts: 1500
  Hours used per day: 4

Machine 2 of 2
  Name: Drill
  Power in watts: 800
  Hours used per day: 2

Your tariff (cost per kWh): 60

==============================================================
Machine            kWh/day   kWh/month    Cost/month
--------------------------------------------------------------
Lathe                 6.00      180.00      10800.00
Drill                 1.60       48.00       2880.00
--------------------------------------------------------------
TOTAL                 7.60      228.00      13680.00
==============================================================

Biggest spender: Lathe (78.9% of your monthly bill)
Cutting Lathe by 25% saves 2700.00 per month. That is a big saving, worth doing!
```

## My own twist
The program finds the machine that costs the most, shows its share of the monthly bill, and asks what percentage you could cut its hours by. It then shows how much money that would save each month.

## What I learned
- Checking input with try/except and a while loop stops the program from crashing when someone types a letter.
- Splitting code into small functions that return values makes it easier to test and reuse.

## Author
Your name, ND2 Mechatronics Engineering, YabaTech.
