# KSEB Bill Estimator
Python code to estimate the KSEB electricity bill for 2 months as per the slabs of KSEB in Kerala.

This program accepts the number of units and can estimate the electricity bill for two months for a single phase domestic connection using the relevant telescopic and non-telescopic slabs specified by Kerala State Electricity Board (KSEB).

This is a python code and should be run in a Python compiler.

If you wish to run the code online, copy the code and paste it into the online compiler such as https://www.programiz.com/python-programming/online-compiler/ and enter the number of units consumed when asked.



## KSEB Slabs for Electricity Consumption in Kerala
The new proposed rates for the year 2022-23 is also provided.

### Telescopic (Rate/Unit for one month)

| Unit Slabs | Rate/Unit | New Proposed Rate/Unit |
| ---------- |:---------:|:----------------------:|
| Upto 50    | ₹3.15     | ₹3.50                  |
| 51-100     | ₹3.70     | ₹4.10                  |
| 101-150    | ₹4.80     | ₹5.50                  |
| 151-200    | ₹6.40     | ₹7.00                  |
| 201-250    | ₹7.60     | ₹8.00                  |

### Non-Telescopic (Rate/Unit for one month)

| Unit Slabs | Rate/Unit | New Proposed Rate/Unit |
| ---------- |:---------:|:----------------------:|
| Upto 300   | ₹5.80     | ₹6.50                  |
| Upto 350   | ₹6.60     | ₹7.20                  |
| Upto 400   | ₹6.90     | ₹7.40                  |
| Upto 450   | ₹7.10     | ₹7.60                  |
| Above 500  | ₹7.90     | ₹8.30                  |

### Fixed Charges

| Unit Slabs | Rate | New Proposed Rate |
| ---------- |:----:|:-----------------:|
| Upto 50    | ₹35  | ₹6.50             |
| 51-100     | ₹45  | ₹7.20             |
| 101-150    | ₹55  | ₹7.40             |
| 151-200    | ₹70  | ₹7.60             |
| 201-250    | ₹80  | ₹8.30             |
| Upto 300   | ₹100 | ₹6.50             |
| Upto 350   | ₹110 | ₹7.20             |
| Upto 400   | ₹120 | ₹7.40             |
| Upto 450   | ₹130 | ₹7.60             |
| Above 500  | ₹150 | ₹8.30             |

## KSEB Forumulas for Electricity Consumption in Kerala

#### Meter Rent = ₹14.16
#### Energy Cost (Telescopic i.e. <=500 Units) for two months
```
    if units<=100:
        energy_cost = units*tel_s1
    elif units<=200:
        energy_cost = 100*tel_s1 + (units-100)*tel_s2
    elif units<=300:
        energy_cost = 100*tel_s1 + 100*tel_s2 + (units-200)*tel_s3
    elif units<=400:
        energy_cost = 100*tel_s1 + 100*tel_s2 + 100*tel_s3 + (units-300)*tel_s4
    else:
        energy_cost = 100*tel_s1 + 100*tel_s2 + 100*tel_s3 + 100*tel_s4 + (units-400)*tel_s5
```
#### Energy Cost (Non-Telescopic i.e. >500 Units) for two months
```
    if units>1000:
        energy_cost = units*ntel_s5
    elif units>800:
        energy_cost = units*ntel_s4
    elif units>700:
        energy_cost = units*ntel_s3
    elif units>600:
        energy_cost = units*ntel_s2
    else:
        energy_cost = units*ntel_s1
```
#### Duty = Energy Cost x 0.1

### Total Cost = Meter Rent + Energy Cost + Fixed Charges + Duty
N.B.: The total cost is rounded to the nearest whole number
