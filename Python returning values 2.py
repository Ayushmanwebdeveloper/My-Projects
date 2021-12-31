# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 00:24:41 2021
@author: Ayushman HP
"""
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result =amount_a + amount_b
print(result) 
