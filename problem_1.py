# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TVSIpZ8FMKO7UF3EoSEzrkXxGb1WMUH8
"""

sum = 0
i = 1
for i in range(1000):
  if (i % 3 == 0) or (i % 5 == 0):
    sum+=i

