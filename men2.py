# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:13:16 2024

@author: Al Hilol
"""

son1=float(input('1-sonni kiriting! :'))
son2=float(input('2-sonni kiriting! :'))
if son1>son2:
    print(f'{son1} > {son2}.')
elif son1==son2:
    print(f'{son1} = {son2}')
else:
     print(f'{son1} < {son2}.')   
     
     #İzoh:
     
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
  print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")    