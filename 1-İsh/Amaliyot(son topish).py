# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:06:01 2024

@author: Al Hilol4
"""
#print("Son topish o'ynida ishtirok eting!!! ")
#while True:
# import random as r
# sonlar=r.randint(1,11)
# savol=int(input("1 dan 10 gacha son o'yladim."\
#                  "Topish uchun son kiriting! : "))
# if savol==sonlar:
#      print(f"_TOPDİNGİZ! {savol} sonini o'ylagan edim. Tabriklayman!")
#     
#      print("1 dan 10 gacha son o'ylang! Men topishga harakat qilaman!")
#      
#      ilova=int(input("Son o'yladingizmi? (xa=1\yoq=0) : "))
#      ilova==1
#      import random as m 
#      son=m.randint(1,11)
#      davom=int(input(f"Siz {son} sonini o'ylgan edingiz: to'g'ri:(15),kattaroq:(23),kichikroq:(13) : "))
#      if davom==15:
#       break
#      if davom==23:
#       if davom>son:
#          davom=input(f"Siz {son}ni o'ylagan edingiz: to'g'ri:(t),kattaroq:(+),kichikroq:(-) :") 
#          continue
#      if davom==13:
#       if davom<son:
#          davom=input(f"Siz {son}ni o'ylagan edingiz: to'g'ri:(t),kattaroq:(+),kichikroq:(-) :")
#          continue
# elif savol>sonlar:
#    savol=int(input(f"Xato! Men {savol} ni o'ylamadim!."\
 #               "Men o'ylagan son bundan kichik!"\
 #                  " Yana harakat qilib ko'ring! : "))       
 #else:
 #    savol=int(input(f"Xato! Men {savol} ni o'ylamadim!."\
  #                "Men o'ylagan son bundan katta!"\
  #                 "Yana harakat qilib ko'ring! :"))         
    
 #takror=input("Dasturni davom etirasizmi? (xa\yoq) :")
 #if takror=='yoq':   
 #    break
#print(">>>Dastur tugadi!")
          
 
        
 
# SON TOPİSH O'YİNNİNG KODİ!   
 
import random

def sontop(x=10):
    tasodifiy_son=random.randint(1,x)
    print(f"1 va {x} orasida son o'yladim. Topish uchun son kiriting!")
    taxminlar=0
    while True:
        taxminlar+=1
        taxmin=int(input(">>> : "))
        if taxmin < tasodifiy_son:
            print(f" Xato! Men o'ylagan son bundan kattaroq! Yana harakat qilib ko'ring! :") 
        elif taxmin > tasodifiy_son:
            print("Xato! Men o'ylagan son bundan kichikroq! Yana harakat qilib ko'ring!")
        else:
            print(f"_Tabriklayman. Men o'ylagan son {taxmin} edi. {taxminlar} - taxminda  topdingiz!")
            break

def sontop_pc(x=10):
    input(f"1 va {x} orasida son o'ylang men topishga harakat qilaman!"\
          f" Davom etish uchun istalgan tugmani bosing! : ")
    past=1
    baland=x
    taxminlar=0
    while True:
       taxminlar+=1
       if past !=baland:
          taxmin = random.randint(past,baland)
       else:
          taxmin=past
       javob =input(f"> Siz {taxmin} sonini o'ylagan edingiz! "\
                    f"To'g'ri:(t),Kattaroq:(+) yoki Kichikroq(-) : ".lower())
       if javob=='-':
         baland=taxmin-1
       elif javob =='+':
         past=taxmin+1
       else:
          break
    print(f"Men {taxminlar} - taxminda topdim!")
    return taxminlar
  
def play(x=10):
    yana=True
    while yana:
        user=sontop(x)
        pic=sontop_pc(x)
        
       # if user>pic:
      #     print("Men yutdim!")
       # elif user<pic:
        #    print("Siz yutdingiz!")
         #else:
         #   print("Kuchlar teng keldi!")
        yana=int(input("Davom etirasizmi? (xa=1\yoq=0) : "))
        print(">>>Dastur tugadi!")
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 