# KSEB ENERGY SLABS
# Telescopic
tel_s1 = 3.15
tel_s2 = 3.70
tel_s3 = 4.80
tel_s4 = 6.40
tel_s5 = 7.60
# Non-Telescopic
ntel_s1 = 5.80
ntel_s2 = 6.60
ntel_s3 = 6.90
ntel_s4 = 7.10
ntel_s5 = 7.90
# Meter Rent
meter_rent = 14.16

#############################################################################################
energy_cost = 0.0
fixed_charges = 0
def telescopic(units):
    global energy_cost
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

def non_telescopic(units):
    global energy_cost
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

def fixed_charges_calc(units):
    global fixed_charges
    if units<=50:
        fixed_charges = 35
    elif units <=100:
        fixed_charges = 45
    elif units<=150:
        fixed_charges = 55
    elif units<=200:
        fixed_charges = 70
    elif units<=250:
        fixed_charges = 80
    elif units<=300:
        fixed_charges = 100
    elif units<=350:
        fixed_charges = 110
    elif units<=400:
        fixed_charges = 120
    elif units<=500:
        fixed_charges = 130
    else:
        fixed_charges = 150
#############################################################################################

units = int(input("Enter the number of units consumed: "))
if units<=500:
    telescopic(units)
else:
    non_telescopic(units)
fixed_charges_calc(units)
print("\nFixed Charges:",fixed_charges)
print("Meter Rent:",meter_rent)
print("Energy Charges:",energy_cost)
duty = energy_cost*0.1
print("Duty:",duty)
total = fixed_charges + meter_rent + energy_cost + duty
print("TOTAL:",round(total),"\n")
