# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:10:03 2018

@author: Sajeel
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:08:10 2018

@author: Sajeel
dorm assignment
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:13:12 2018

@author: Sajeel
"""

import numpy as np
from random import *

# Read in Campers Data
# Assuming Campers are assigned camper ID's ranging from 1-48
# Creating new  48*3  array to handle dorm assignment
# col0 = ID, col1 = gender , col2 = age , col3 = dorm number (dorm 1,2,3 are male; dorm 4,5,6 are female)
# Dataset = np.zeros((48,3))

N = 48; # Total number of Campers

# Generating Sample Dataset to test dorm assignment algorithm
ID = list(range(1,49)) # Generate ID's

randBinList = lambda n: [randint(0,1) for b in range(1,n+1)] # generates random binary numbers
## Gender = randBinList(48) # 0 denotes Female, 1 denotes Male

# Create gender vector
males = np.ones((24,1))
females = np.zeros((24,1))
Gender = np.r_[males,females]

# Loop to assign age groups. Groups(13-14),(15-16),(17-18) are grouped as
# young, middle, elder respectively.

age_group = np.zeros((48,1))
lock_assignment = np.zeros((48,1)) # if 1 then person is locked to dorm.

for x in range(48): # generating random age groups 1 = young, 2 = middle, 3 = old
  age_group[x] =(randint(1,3))
"""
i = 1; # counter

while i <= N + 1:
    if age_group[i] == 1:
        age_group[i] = "young" # grouping by age to 2nd column of matrix
        i = i + 1
    elif age_group[i] == 2:
        age_group[i] = "middle" # grouping by age to 2nd column of matrix
        i = i + 1
    else:
        age_group[i] = "elder"
        i = i + 1
"""

dorm_no = np.zeros((48,1))

# Column stacking ID, Gender, age_group, dorm number

random_data = np.c_[ID, Gender, age_group, dorm_no, lock_assignment]


"""
# Loop to assign age groups. Groups(13-14),(15-16),(17-18) are grouped as
# young, middle, elder respectively.

i = 1; # counter
while i <= N + 1:
    if 13 <= Dataset[i,3] <= 14:
        Dataset[i,3] = "young" # grouping by age to 2nd column of matrix
        i = i + 1
    elif 15 <= Dataset[i,3] <= 16:
        Dataset[i,3] = "middle" # grouping by age to 2nd column of matrix
        i = i + 1
    else:
        Dataset[i,3] = "elder"
        i = i + 1
"""


# non random age data
age_y = np.ones((8,1))
age_m = ( np.ones((8,1)) ) * 2
age_e = ( np.ones((8,1)) ) * 3

age_group_deterministic = np.r_[age_y, age_m, age_e, age_y, age_m, age_e]

fixed_data = test_data = np.c_[ID, Gender, age_group_deterministic, dorm_no]





# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 22:36:10 2018

@author: Sajeel
"""

# male dorm 1 (Coded Dorm 1)

max_dorm_age = 0
        
m_dorm_1_occupancy = 0    # Total Occupancy for male dorm 1

min_no_m_dorm_1_y = 2 # minimum number of a males of age group "young" in first male  dorm
max_no_m_dorm_1_y = 3 # maximum ...
m_dorm_1_occupancy_y = 0 # no of young occupants for male dorm 1


min_no_m_dorm_1_m = 2 # middle
max_no_m_dorm_1_m = 3 #
m_dorm_1_occupancy_m = 0

min_no_m_dorm_1_e = 2 # elder
max_no_m_dorm_1_e = 3 # 
m_dorm_1_occupancy_e = 0

# male dorm 2 (Coded Dorm 2)

m_dorm_2_occupancy = 0

min_no_m_dorm_2_y = 2 # 
max_no_m_dorm_2_y = 3 # .
m_dorm_2_occupancy_y = 0

min_no_m_dorm_2_m = 2 # 
max_no_m_dorm_2_m = 3 #
m_dorm_2_occupancy_m = 0

min_no_m_dorm_2_e = 2 # 
max_no_m_dorm_2_e = 3 #
m_dorm_2_occupancy_e = 0

# male dorm 3 (Coded Dorm 3)

m_dorm_3_occupancy = 0

min_no_m_dorm_3_y = 2 # 
max_no_m_dorm_3_y = 3 # .
m_dorm_3_occupancy_y = 0

min_no_m_dorm_3_m = 2 # 
max_no_m_dorm_3_m = 3 #
m_dorm_3_occupancy_m = 0

min_no_m_dorm_3_e = 2 # 
max_no_m_dorm_3_e = 3 #
m_dorm_3_occupancy_e = 0

# female dorm 1 (Coded dorm 4)

f_dorm_1_occupancy = 0 

min_no_f_dorm_1_y = 2 # 
max_no_f_dorm_1_y = 3 # 
f_dorm_1_occupancy_y = 0

min_no_f_dorm_1_m = 2 # 
max_no_f_dorm_1_m = 3 #
f_dorm_1_occupancy_m = 0

min_no_f_dorm_1_e = 2 # 
max_no_f_dorm_1_e = 3 #
f_dorm_1_occupancy_e = 0

# female dorm 2 (Coded dorm 5)

f_dorm_2_occupancy = 0

min_no_f_dorm_2_y = 2 # 
max_no_f_dorm_2_y = 3 # .
f_dorm_2_occupancy_y = 0

min_no_f_dorm_2_m = 2 # 
max_no_f_dorm_2_m = 3 #
f_dorm_2_occupancy_m = 0

min_no_f_dorm_2_e = 2 # 
max_no_f_dorm_2_e = 3 #
f_dorm_2_occupancy_e = 0

# female dorm 3 (coded dorm 6)

f_dorm_3_occupancy = 0

min_no_f_dorm_3_y = 2 # 
max_no_f_dorm_3_y = 3 #
f_dorm_3_occupancy_y  = 0

min_no_f_dorm_3_m = 2 # 
max_no_f_dorm_3_m = 3 #
f_dorm_3_occupancy_m  = 0

min_no_f_dorm_3_e = 2 # 
max_no_f_dorm_3_e = 3 #
f_dorm_3_occupancy_e  = 0


no_males = 24
no_females = 24

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 17:45:42 2018

@author: Sajeel
"""
# Creating new  48*3  array to handle dorm assignment
# col0 = ID, col1 = gender , col2 = age , col3 = dorm number (dorm 1,2,3 are male; dorm 4,5,6 are female)

i = 0; # counter for number of campers assigned to a dorm
bal_cntr = 0 # counter for subsequent  round of assignments # outer loop for bal counter
outer_cntr = 1 # counter for outer loop
#assignment_data = fixed_data
assignment_data = random_data

while outer_cntr <= 12:
    
        while i < 24: # Segment for Male Dorm Assignment  
            if (                                   # Dorm 1
                m_dorm_1_occupancy < 8    and  # check if dorm is full
                assignment_data [i,2] == 1 and  # check for age group
                m_dorm_1_occupancy_y <= max_dorm_age + bal_cntr
               ): 
                assignment_data [i,3] = 1  # Assignment of young males to male dorm 1
                m_dorm_1_occupancy_y += 1# increment age occupancy for dorm 1
                m_dorm_1_occupancy += 1 # increment dorm occupancy
                i += 1
                
            elif (                                   #  Dorm 1
                  m_dorm_1_occupancy < 8    and  # check if dorm is full
                  assignment_data [i,2] == 2 and  # check for age group
                  m_dorm_1_occupancy_m <= max_dorm_age + bal_cntr 
                 ): 
                  assignment_data [i,3] = 1  # Assignment "middle" males to male dorm 1
                  m_dorm_1_occupancy_m += 1
                  m_dorm_1_occupancy += 1
                  i += 1
                  
            elif (                                   # Dorm 1
                  m_dorm_1_occupancy < 8    and  # check if dorm is full
                  assignment_data [i,2] == 3 and  # check for age group
                  m_dorm_1_occupancy_e <= max_dorm_age + bal_cntr
                 ): 
                  assignment_data [i,3] = 1  # Assignment of "elder" males to male dorm 1
                  m_dorm_1_occupancy_e += 1
                  m_dorm_1_occupancy += 1
                  i += 1
                  
                  # Assignment of males to Dorm 2
                  
            elif (                                   # Dorm 1
                m_dorm_2_occupancy < 8    and  # check if dorm is full
                assignment_data [i,2] == 1 and  # check for age group
                m_dorm_2_occupancy_y <= max_dorm_age + bal_cntr
                 ): 
                assignment_data [i,3] = 2  # Assignment of young males to male dorm 2
                m_dorm_2_occupancy_y += 1 # increment age occupancy for dorm 1
                m_dorm_2_occupancy += 1 # increment dorm occupancy
                i += 1
                
            elif (                                   #  Dorm 1
                  m_dorm_2_occupancy < 8    and  # check if dorm is full
                  assignment_data [i,2] == 2 and  # check for age group
                  m_dorm_2_occupancy_m <= max_dorm_age + bal_cntr
                 ): 
                  assignment_data [i,3] = 2  # Assignment "middle" males to male dorm 2
                  m_dorm_2_occupancy_m += 1
                  m_dorm_2_occupancy += 1
                  i += 1
                  
            elif (                                   # Dorm 1
                  m_dorm_2_occupancy < 8    and  # check if dorm is full
                  assignment_data [i,2] == 3 and  # check for age group
                  m_dorm_2_occupancy_e <= max_dorm_age + bal_cntr
                 ): 
                  assignment_data [i,3] = 2  # Assignment of "elder" males to male dorm 2
                  m_dorm_2_occupancy_e += 1
                  m_dorm_2_occupancy += 1
                  i += 1
                  
                  # Assignment of Males to Dorm 3
                  
            elif (                                   # Dorm 1
                m_dorm_3_occupancy < 8    and  # check if dorm is full
                assignment_data [i,2] == 1 and  # check for age group
                m_dorm_3_occupancy_y <= max_dorm_age + bal_cntr
                 ): 
                assignment_data [i,3] = 3  # Assignment of young males to male dorm 3
                m_dorm_3_occupancy_y += 1 # increment age occupancy for dorm 1
                m_dorm_3_occupancy += 1 # increment dorm occupancy
                i += 1
                
            elif (                                   #  Dorm 1
                  m_dorm_3_occupancy < 8    and  # check if dorm is full
                  assignment_data [i,2] == 2 and  # check for age group
                  m_dorm_3_occupancy_m <= max_dorm_age + bal_cntr
                 ): 
                  assignment_data [i,3] = 3  # Assignment "middle" males to male dorm 3
                  m_dorm_3_occupancy_m += 1
                  m_dorm_3_occupancy += 1
                  i += 1
                  
            elif (                                   # Dorm 1
                  m_dorm_3_occupancy < 8    and  # check if dorm is full
                  assignment_data [i,2] == 3 and  # check for age group
                  m_dorm_3_occupancy_e <= max_dorm_age + bal_cntr
                 ): 
                  assignment_data [i,3] = 3  # Assignment of "elder" males to male dorm 3
                  m_dorm_3_occupancy_e += 1
                  m_dorm_3_occupancy += 1
                  i = i + 1
            else:
                break
        
        outer_cntr += 1
        bal_cntr += 1
    
          



    
          

# np.unique(assignment_data[0:24,3],return_counts=True) # frequency check
# np.unique(z,return_counts=True) # frequency check for age balance  
        


            
            
                
               
                
                
           
           
           
        
        
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:36:43 2018

@author: Sajeel
automated_test
"""
import matplotlib.pyplot as plt

z = assignment_data[0:24,(2,3)]
males = assignment_data[0:24,:]
females = assignment_data[24:48,:]

male_age_freuency = np.unique(age_group[0:24],return_counts=True)

male_dorm_1_distribution = (m_dorm_1_occupancy_y,m_dorm_1_occupancy_m,m_dorm_1_occupancy_e)
male_dorm_2_distribution = (m_dorm_2_occupancy_y,m_dorm_2_occupancy_m,m_dorm_2_occupancy_e)
male_dorm_3_distribution = (m_dorm_3_occupancy_y,m_dorm_3_occupancy_m,m_dorm_3_occupancy_e)   

overall_male_distribution = np.c_[male_dorm_1_distribution,male_dorm_2_distribution,male_dorm_3_distribution]
print(overall_male_distribution)
"""
plt.plot([1,2,3],male_dorm_1_distribution,'bo',[1,2,3],male_dorm_2_distribution,'go',[1,2,3],male_dorm_3_distribution,'yo')
plt.xlabel('age_group')
plt.ylabel('frequency')
plt.show()
"""









        
            
            
                
               
                
                
           
           
           
        
        
    
    










