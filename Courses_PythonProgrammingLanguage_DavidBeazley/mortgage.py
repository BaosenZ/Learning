#!/usr/bin/env python
# coding: utf-8

# In[10]:


#mortgageV1.py
#
#find out how long to pay off a mortgage

principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0

while principal > 0:
    interest = principal*(0.05/12)
    principal = principal + interest - payment
    total_paid += payment

print('Total_paid:', total_paid)


# In[11]:


#mortgageV2.py
#
#find out how long to pay off a mortgage

principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0

#extra payment info
extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0

while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal*(0.05/12)
    principal = principal + interest - total_payment
    total_paid += total_payment

print('Total_paid:', total_paid)

