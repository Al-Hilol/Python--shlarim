# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:06:47 2024

@author: Al Hilol
"""

#adib={
#'abu':{'ismi':'abdulloh muhammad ibn ismoil',
#       'tyil':810,
#       'tjoy':'buxoro',
#       'umri':60
#       },
#'abdulla':{'ismi':'qodiriy',
#       'tyil':1894,
#       'tjoy':'toshkent',
#       'umri':44
#       },
#'erkin':{'ismi':'vohidiy',
#       'tyil':1936,
#       'tjoy':'farg\'ona',
#       'umri':80
#       },
#'alisher':{'ismi':'navoiy',
#       'tyil':1441,
#       'tjoy':'xirot',
#       'umri':60
#       },
#}
#for kalit,qiymat in adib.items():
#    print(f"{kalit.title()} {qiymat['ismi'].title()},"
#          f"{qiymat['tyil']}-yilda {qiymat['tjoy'].title()}da tavallud topgan."
#          f"{qiymat['umri']}-yil umr ko\'rgan.")

    
#adib={
#'abu':{'ismi':'abdulloh muhammad ibn ismoil',
#       'tyil':810,
#       'tjoy':'buxoro',
#       'umri':60,
#       'asar':['-al-jome - as-sahih.','-al-adab almufrad.']
#       },
#'abdulla':{'ismi':'qodiriy',
#       'tyil':1894,
#       'tjoy':'toshkent',
#       'umri':44,
#       'asar':['-o\'tkan kunlar.','-obid ketmon.']
#       },
#'erkin':{'ismi':'vohidiy',
#       'tyil':1936,
#       'tjoy':'farg\'ona',
#       'umri':80,
#       'asar':['-o\'zbegim.','-tong nafasi.']
#       },
#'alisher':{'ismi':'navoiy',
#       'tyil':1441,
#       'tjoy':'xirot',
#       'umri':60,
#       'asar':['-xamsa.','-munojat.']
#       },
#}
#for kalit,qiymat in adib.items():
#    print(f"{kalit.title()} {qiymat['ismi'].title()}ning mashhur asarlari:")    
#    for nom in qiymat['asar']:
#        print(nom.title())
    
#yaqin={
#'usmon':{'kino':[' -ertuğrul','-içeride',' -hedef']
#      },
#'karim':{'kino':[' -suyunchi',' -osmon',' -qasos']
#       },
#'erkin':{'kino':[' -tungi mehmon',' -saboq',' -va\'da']
#     }
#}    
#for uzun,qisqa in yaqin.items():
#    print(f"{uzun.title()}ning sevimli filmlari:")
#    for ot in qisqa['kino']:
#        print(ot.title())
    

#davlatlar={
#'ism':{'joy':'turkiya',
#       'poytaxti':'ankara',
#       'hududi':785000,
#       'aholisi':86,
#       'pul birligi':'lira'
#     }, 
#'ot':{'joy':'germaniya',
#       'poytaxti':'berlin',
#       'hududi':387000,
#       'aholisi':82,
#       'pul birligi':'mark'
#     }
#}   
#for yuz,bet in davlat.items():
#    print(f"{bet['joy'].title()}ning poytaxti {bet['poytaxti'].title()} shahri."
#          f"Hududi {bet['hududi']} kv.km,."
#          f"Aholisi {bet['aholisi']} mln."          
#f"Pul birligi: {bet['pul birligi']}.")davr=input('Biror bir davlat nomini kiriting! :').lower()

#yurt={
#'misr':{'poytaxt':'qohira',        
#     'malumot':['hududi : 1372000 kv.km, .','aholisi :123 mln.','-pul birligi : misr dollari.']    
#    },
#'turkiya':{'poytaxt':'ankara',        
#     'malumot':['hududi : 782000 kv.km, .','aholisi :85 mln.','-pul birligi : turk lirasi.']    
#    },
#'germaniya':{'poytaxt':'berlin',
#     'malumot':['hududi : 372000 kv.km, .','aholisi :82 mln.','-pul birligi : mark.']    
#    }
#} 

#for davlat,info in yurt.items(): 
 #   print(f"{davlat.title()}ning poytaxti {info['poytaxt'].title()}")    
 #   for avlod in info['malumot']:
 #       print(avlod.title())
  
    
#davlatlar = {
#    "o'zbekiston":{'poytaxt':"toshkent",
#                   'maydon':448978,
#                   'aholi':33_000_000,
#                   'pul birligi':"so'm"
#                   },
#    "rossiya":{'poytaxt':"moskva",
#                   'maydon':17_098_246,
#                   'aholi':144_000_000,
#                   'pul birligi':"rubl"
#                   },
#    "aqsh":{'poytaxt':"vashington",
#                   'maydon':9_631_418,
#                   'aholi':327_000_000,
#                   'pul birligi':"dollar"},
#    "malayziya":{'poytaxt':"kuala-lumpur",
#                   'maydon':329750,
 #                  'aholi':25_000_000,
  #                 'pul birligi':"rinngit"}
   # }

#davlat = input('Davlat nomini kiriting: ').lower()
#if davlat in davlatlar:
#    info = davlatlar[davlat]
#    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#          f"\nHududi: {info['maydon']} kv.km"
#          f"\nAholisi: {info['aholi']}"
#          f"\nPul birligi: {info['pul birligi']}")
#else:
#    print("Bizda bu davlat haqida ma'lumot mavjud emas")
      
    
#davr=input('Biror bir davlat nomini kiriting! :')
#yurt={
# 'misr':{'poytaxti':'qohira',        
#        'maydoni':123,
#        'aholisi':123,
#        'pul birligi':'misr dollari'
#     },
# 'özbekiston':{'poytaxti':"toshkent",
#                'maydoni':448,
#                'aholisi':33,
#                'pul birligi':'söm'
#                },
# 'turkiya':{'poytaxti':'ankara',        
#            'maydoni':748,
#            'aholisi':85,
#            'pul birligi':"turk lirasi"
#     },
# 'germaniya':{'poytaxti':'berlin',
#              'maydoni':345,
#              'aholisi':82,
#              'pul birligi':"mark"
# }
#} 
#if davr in yurt:
#     info=yurt[davr]
#     print(f" {davr.title()}ning poytaxti {info['poytaxti'].title()}. "
#           f" Hududi: {info['maydoni']} ming kv.km; "
#           f" Aholisi {info['aholisi']} mln,"
#           f" Pul birligi: {info['pul birligi'].title()}.")
#else:
#     print(f"Bizda {davr.title()} haqida ma\'lumot yo\'q!") 
    
  
#ism=input('İsmingiz nima? :')
#savol=f'Salom.{ism.title()} Yoshingiz nechida? :'
#yosh=input(savol)
#yosh=int(yosh)  
#height=input('Bo\'yingiz necha metr? :')
#height=float(height)
#print('Dastur tugadi!')
  
#son=1
#while son <= 7:
#    print(son,end='')
#    son+=1
#print(' Datur tugadi!')  

#print('Kiritilgan sonning kvadratini chiqaruvchi dastur!')
#savol='Daturni to\'xtatish uchun exit deb yozing!. İstalgan son kiriting :'
#qiymat=''
#while qiymat !='exit':
#    qiymat=input(savol)
#    if qiymat !='exit':
#        print(float(qiymat)**2)
#print('Dastur tugadi!')


#print('Kiritilgan sonning kvadratini chiqaruvchi dastur!')
#savol='Daturni to\'xtatish uchun exit deb yozing!. İstalgan son kiriting :'
#ishora=True
#while ishora:
#    qiymat=input(savol)
#    if qiymat=='exit':
#        ishora=False
#    else:
#        print(float(qiymat)**2)
#    print('Datur tugadi!')



#print('Kiritilgan sonning kvadratini chiqaruvchi dastur!')
#savol='Daturni to\'xtatish uchun exit deb yozing!. İstalgan son kiriting :'
#ishora=True
#while ishora:
 #   qiymat=input(savol)
 #   if qiymat=='exit':
 #    break
 #   else:
 #    print(float(qiymat)**2)
 #   print('Dastur tugadi!')
#sonlar=list(range(1,16))
#for son in sonlar:
#    if son ==3:
 #       continue
 #   print(f"{son} ning kvadrati {son**2} ga teng !")

#son=0
#while son<10:
#    son=son+1
#    if son%2==0:
#        continue
#    else:
#        print(son)
   
#print('Obunachining sevimli kitoblar ro\'yxati!')
#savol='Sevimli kitobingizni kiriting! :'
#asar=''
#while asar!='stop':
#    asar=input(savol)
#    if asar!='stop':
#        print(f"{asar.title()}")
#print('Dastur tugadi! ')
    

#savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:
#    qiymat = input(savol)
#    if qiymat<'0':
#        continue
#    elif qiymat=='Exit' or qiymat=='exit':
#        break
#    else:
#        ildiz = float(qiymat)**(0.5)
#        print(f"{qiymat} ning ildizi {ildiz} ga teng")
#print('Dastur to\'xtadi!')

#savol=(">Bu dastur xaridorning yoshiga qarab narx belgilaydi!")
#savol+=(">Daturni to'xtatish uchun tugat yoki yetarli deb yozing!")
#savol+=(">İltimos yoshingiz yoki to'xtatish parolini kiriting! :")
#while True:
#    hujim=input(savol)
#    if hujim=='tugat' or hujim=='yetarli':
#        break
#    yosh=int(hujim)
#    if yosh<=7 or yosh>=60:
#        narx=0
#    elif yosh<=18:
#        narx=5000
#    elif yosh<=60:
#        narx=12000
#        
#    if narx==0:
#        print('-Siz uchun kirish bepul!')
#    else:
#        print(f'-Siz uchun kirish narxi {narx} so\'m!')
#print('Dastur tugadi!')    


#print("Yaqin do'stlaringiz ro'yxatini tuzing!")
#ismlar=[]
#n=1
#while True:
#    savol=f"{n}-do'stingiz ismini kiriting! :"
#    ism=input(savol)
#    ismlar.append(ism)
#    takrorlash=input("Yana ism qo'shilsinmi? (ha/yo'q) :")
#    n+=1
#    if takrorlash!='ha':
#        break
#    print("Do'stlaringiz ro'yxati:")
#    for ism in ismlar:
#        print(ism.title())
#print('Dastur tugadi!')

#print("Do'stlaringiz yoshini belgilang!")
#dostlar={}
#belgi=True
#while belgi:
#    nom=input("Do'stingiz ismini kiriting! :")
#    yosh=input(f"{nom.title()}ning yoshini kiriting!")
#    dostlar[nom]=int(yosh)
#    javob=input("Yana ma'lumot qo'shasizmi? (ha/yo'q) :")
#    if javob=="yo'q":
#        belgi=False
#for nom,yosh in dostlar.items():
#    print(f"{nom.title()} {yosh} yoshda!")
#print('Dastur tugadi!')

#cars=['audi','porsche','bmw']
#while 'audi' in cars:
#    cars.remove('audi')
#print(cars)


#cars=['audi','porsche','bmw']
#car='porsche'
#while car in cars:
#    cars.remove(car)
#print(cars)

#talabalar=['mahmud','ali','umar','usmon','murtazo']
#b_talabalar={}
#while talabalar:
#    talaba=talabalar.pop()
#    baho=input(f"{talaba.title()}ning bahosini kiriting! :")
#    print(f"-{talaba.title()} baholandi!")
#    b_talabalar[talaba]=int(baho)
#print('Dastur tugadi!')



#print('Buyurtmalarni qabul qilish boshlandi! :')
#buyurtmalar=[]
#r=1
#davom=True
#while davom:
#    savol=f"{r} - buyurtmangizni yozing? :"
#    nom=input(savol)
#    buyurtmalar.append(nom)
#    qaytarish=input("Yana buyurtma berasizmi?(ha/yo'q) :")
#    r+=1
#    if qaytarish!='ha':
#        break
#    print('Barcha buyurtmalaringiz ro\'yxati!')
#    for nom in buyurtmalar:
#        print(nom.title())
#print('Dastur tugadi!')

#print("E-bozor uchun maxsulotlar va ularning narxlar ro'yxatini tuzing!")
#maxsulotlar={}
#while True:
#    maxsulot_nomi=input("Siz oladigan maxsulot nomini yozing! :")
#    
#    narx=input('Maxsulot narxi qancha bo\'lsin? :')
#    
#    maxsulotlar[maxsulot_nomi]=int(narx)
#    
#    ilova=input("Yana maxsulot olasizmi? (xa,yo'q) :")
#    
#    if ilova=="yo'q":
#        break
#for maxsulot_nomi,narx in maxsulotlar.items():
#    print(f"{maxsulot_nomi.title()} : {narx} so'm")
#print("Dastur tugadi!")
#maxsulot_nomi=['fen','quloqchin','soat','somka','kitob']
#buyurtma={'fen':180000,
#          'kitob':65000,
#          'aqlli soat':400000,
#          'quloqchin':150000,
#          'telefon':2500000}
#while maxsulot_nomi:
#    maxsulot=maxsulot_nomi.pop()
#    if maxsulot in buyurtma.keys():
#      nom=buyurtma[maxsulot]
#      print(f"{maxsulot.title()} - {nom} so'm")
#    else:
#        print(f"Bizda {maxsulot} yo'q!")

#def salom_ber():
#    """Salom beruvchi funksiya"""
#    print("Assalomu alaykum!")
#salom_ber()

#def yosh_hisobla(t_yil,joriy_yil=2024):
#   """Foydalanuvchining tug'ilgan yilini hisoblovchi dastur!"""
#   print(f"Siz {2024-t_yil} yoshdasiz!")

#yosh_hisobla(1993)


#ism=input('İsmingizni kiriting! :')
#yosh=int(input('Yoshingizni kiriting! :'))

#def tugilgan_yil(ism,yosh):
#    """Foydalanuvchining tug'ilgan yilini hisoblovchi dastur!"""
#    print(f"{ism.title()} siz {2024-yosh} - yilda tug'ilgansiz!")

#tugilgan_yil(ism,yosh)

#son=int(input('İltimos son kiriting! :'))

#def kvadrat_kub(son):
#    """Kvadrat va Kub hisoblash"""
#    print(f"-{son} ning kvadrati {son**2} ga teng!")
#    print(f"-{son} ning kubi {son*son*son} ga teng!")

#kvadrat_kub(son)

#son=int(input('İltimos son kiriting! :'))

#def juft_toq(son):
#    """Sonning juft yoki toqligini hisoblash!"""
#if son%2:
#    print(f"{son}.toq sondir!")
#else:
#    print(f"{son}.juft sondir!")
   
#juft_toq(son)


#son1=int(input('İltimos birinchi sonni kiriting! :'))
#son2=int(input('İltimos ikkinchi sonni kiriting! :'))

#def son_holati(son1,son2):
#    """Sonlarning umumiy holatini belgilovchi funksiya"""
#if son1>son2:
#    print(f"Eng katta son {son1} !")
#elif son1==son2:
#    print(f"Sonlar bir-biriga teng!")
#else:
#    print(f"{son1},{son2} dan kichik!")

#x=int(input('İltimos birinchi sonni kiriting! :'))
#y=int(input('İltimos ikkinchi sonni kiriting! :'))


#def daraja_hisobla(x,y):
#    """Kiritilgan 1-son(x)ning darajaini hisoblaydigan funkisya"""
#    print(f"{x} ning {y} darajasi {x**y} ga teng!")

#daraja_hisobla(x,y)



#x=int(input('İstalgan biror bir son kiriting! :'))

#def daraja_hisobla(x,y=2):
#    """Kiritilgan 1-son(x)ning darajaini hisoblaydigan funkisya"""
#    print(f"{x} ning {y} darajasi {x**y} ga teng!")

#daraja_hisobla(x)


#number=int(input('İltimos butun son kiriting! :'))

#def qoldiq_hisobla(number):
#    """Kiritilgan sonni 2 dan 10 gacha bo'lgan sonlar orasida qaysilarga qoldiqsiz bo'linishini hisoblovchi funksiya.""" 

#for son in range(2,11):
#    if not(number%son):
#        print(f"{number} soni {son} ga qoldiqsiz bo'linadi!")
#print(f"-{number} soniga 2 dan 10 gacha bo'lgan sonlar orasida qoldiqsiz bo'linadiganlari yuqorida, boshqa mavjud emas!")
#print('>>>Dastur tugadi!')
#qoldiq_hisobla(number)


#def toliq_ism_yoz(ism,familiya):
#    """To'liq ism qaytaruvchi funksiya"""
#    toliq_ism=f"{ism} {familiya}"
#    return toliq_ism
#inson=toliq_ism_yoz('asror','ibrohim')



#def toliq_ism_yoz(ism,familiya):
     #    """To'liq ism qaytaruvchi funksiya"""
       
#    toliq_ism=f"{ism} {familiya}"
#    return toliq_ism
#inson1=toliq_ism_yoz('asror','ibrohim')
#inson2=toliq_ism_yoz('ahmad','ismoil')
#print(f"Darsga kelmagan talabalar: {inson1.title()} va {inson2.title()}. "\
#      f" {inson1.title()} esa darsga kechikib keldi!")

#def toliq_ism_yoz(ism,familiya,otasining_ismi):
#        """To'liq ism qaytaruvchi funksiya"""
#        if otasining_ismi:
#          toliq_ism=f"{ism} {otasining_ismi} {familiya}"
#        else:
#          toliq_ism=f"{ism} {familiya}"
#        return toliq_ism.title()
#inson1=toliq_ism_yoz('asror', 'olim','ibrohimiy')
#inson2=toliq_ism_yoz('ahmad','irfon','ilhomiy')
#print(f"Darsga kelmagan talabalar {inson1}. {inson2} esa allaqachon sinfda!")

#def oraliq(min,max):
#    sonlar=[]
#    while min<max:
#        sonlar.append(min)
#        min+=1
#    return sonlar
#print(oraliq(0, 10))
#print(oraliq(10, 21))
#     

#def oraliq(min,max,qadam):
#    sonlar=[]
#    while min<max:
#        sonlar.append(min)
#        min+=3
#    return sonlar
#print(oraliq(0, 10,0))
#print(oraliq(10, 21,1))
#print(oraliq(21,31,0))
     
#def avto_info(kompaniyasi,modeli,rangi,yili,narxi=None):
#    avto={'kompaniya':kompaniyasi,
#          'model':modeli,
#          'rang':rangi,
#          'yil':yili,
#          'narx':narxi}
#    return avto
#avto1=avto_info("porsche","thander","gray",2023,120000)
#avto2=avto_info("BMW",'x6','qora',2021,90000)
#avtolar=[avto1,avto2]
#print("Ochiq bozordagi mavjud avtomobillar:")
#for avto in avtolar:
#    if avto['narx']:
#        narx=avto['narx']
#    else:
#        narx="Noma'lum"
#    print(f"{avto['kompaniya'].title()}, {avto['rang']} {avto['model']}, narxi:{narx} $.")
 
#def avto_info(kompaniya,model,rangi,yili,narxi=None):
#    avto={'kompaniya':kompaniya,
#          'model':model,
#           'rang':rangi,
#           'yil':yili,
#           'narx':narxi}
 #   return avto 
#print("Saytdagi avtomobillar ro'yxatini shaklandirish!")
#avtolar=[]
#while True:
#  print("Quydagi ma'lumotlarni kiriting!")
#  kompaniya=input("İshlab chiqaruvchi:")
#  model=input("Modeli:")
#  rangi=input("Rangi:")
#  turi=input("Turi:")
#  yil=input("İshlab chiqarilgan yili:")
#  narxi=input("Narxi:")
#  avtolar.append(avto_info(kompaniya,model,rangi,yil,narxi))
#  savol=input("Yana ma'lumot kiritasizmi? (xa\yo'q) :")
#  if savol=="yo'q":
#    break
#print("Salonimizdagi avtomobillar:")
#for avto in avtolar:
#      if avto['narx']:
#          narx=avto['narx']
#      else:
 #         narx="Noma'lum"
#print(f"{avto['kompaniya'].upper()}, {avto['rang'].title()} {avto['model'].title()},turi:{turi}, Narxi:{narx} $.")

#def biografiya(ismi,familiya,tyili,tjoyi,email,telefon):
#   bio ={"ismi":ismi,
#         "familiya":familiya,        
#         "tyili":tyili,
#         "tjoyi":tjoyi,
#         "email":email,
#         "telefon":telefon}
 #   return bio
#print("Foydalanuvchi haqida ma'lumot beruvchi funksiya!")
#biografiyasi=[]
#while True:
#    print("Quydagi ma'lumotlarni kiriting! ")
#    ismi=input("İsmi! : ")
#    familiya=input("Familiyasi! : ")
#    tyili=int(input("Tug'ilgan yili! : "))
#    tjoyi=input("Qayerda tug'ilgan! : ")
#    email=input("E-pochta manzili! (ixtiyoriy): ")
#    telefon=int(input("Telefon raqami! : "))
#    biografiyasi.append(biografiya(ismi,familiya,tyili,tjoyi,email,telefon))
#    ilova=input("Yana ma'lumot kiritasizmi?  (xa\yo'q) : ")
#    if ilova!='xa':
#        break
#print("-Foydalanuvchi haqida ba'zi  bir ma'lumotlar !")
#for bio in biografiyasi:
#  print(f"Mijoz {bio['ismi'].title()} {bio['familiya'].title()}, {bio['tyili']}-yil {bio['tjoyi'].title()}da tug'ilgan. "\
#        f" E-pochta manzili :{bio['email']}, Telefon raqami esa {bio['telefon']}.")
#print(">>>Dastur tugadi!")
#biografiya(ismi,familiya,tyili,tjoyi,email,telefon)


#son1=int(input("Birinchi sonni kiriting! :"))
#son2=int(input("İkkinchi sonni kiriting! :"))
#son3=int(input("Uchinchi sonni kiriting! :"))

#def eng_kattasi(son1,son2,son3):

# if son1 >= son2 and son3:
#    print(f"-Eng katta {son1}.")
# elif son2 >= son3 and son1:
#    print(f"-Eng katta son {son2}.")
# elif son3 >= son1 and son2:
#    print(f"Eng katta son {son3}.")
# else:
#    print("İltimos butun son kiriting!")
#eng_kattasi(son1,son2,son3)

#print(">>>Dastur tugadi!")


#print("Aylananing radius,diametr,perimetr,yuzi aniqlovchi funksiya")

#def olchov(radius,diametr,perimetr,yuzi):
#    """Aylananing radius,diametr,perimetr,yuzi aniqlovchi funksiya"""
#    aylana={"radius":radius,
#            "diametr":diametr,
#            "perimetr":perimetr,
#            "yuzi":yuzi
#            }
#    return aylana
#aylanasi=[]
#while True:
#    radius=int(input("Radiusi :"))
#    diametr=int(input("Diametr :"))
#    perimetr=int(input("Perimetr :"))
#    yuzi=int(input("Yuzi :"))
#    aylanasi.append(olchov(radius,diametr,perimetr,yuzi))
#    ilova=input("-Yana ma'lumot kiritasizmi? (xa\yo'q) :")
#    if ilova=="yo'q":
#       break
#print("O'lchov birliklari haqida ba'zi bir ma'lumotlar!")
#for aylana in aylanasi:
# print(f"-Aylananing radiusi : {aylana['radius']} m ga,diametri : {aylana['diametr']} sm ga,"\
#       f"Perimetri : {aylana['perimetr']} sm ga, Yuzi esa {aylana['yuzi']} m ga teng!")
    
#print(">>>Dastur tugadi!")


#def qoldiq_hisobla(number):
#    """Kiritilgan sonni 2 dan 10 gacha bo'lgan sonlar orasida qaysilarga qoldiqsiz bo'linishini hisoblovchi funksiya.""" 

#for son in range(2,11):
#    if not(number%son):
#        print(f"{number} soni {son} ga qoldiqsiz bo'linadi!")
#print(f"-{number} soniga 2 dan 10 gacha bo'lgan sonlar orasida qoldiqsiz bo'linadiganlari yuqorida, boshqa mavjud emas!")
#print('>>>Dastur tugadi!')
#qoldiq_hisobla(number)



#def tub_sonlar(tub_son):
#    """Tub sonlarni aniqlovchi funksiya"""
#tub_son=list(range(3,21,2))
#print(tub_son)

#tub_sonlar(tub_son)
#print(">>>Dastur tugadi!")


#def tub_sonlar_top(min, max):
#    tub_sonlar = []
#    for n in range(min, max + 1):
#        tub = True
#        if n == 1:
#            tub = False
#        elif n == 2:
#            tub = True
#        else:
#            for x in range(2, n):
#                if n % x == 0:
#                    tub = False
#        if tub:
#            tub_sonlar.append(n)


#    return tub_sonlar


#def fibonacci(n):
#    sonlar = []
#    for x in range(n):
#        if x == 0 or x == 1:
#            sonlar.append(1)
#        else:
#            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#    return sonlar


#print(fibonacci(10))


#def ketma_ketlik(raqam):
#    son = []
#    for nom in range(raqam):
#        if nom==0 or nom==1:
#            son.append(1)
#        else:
#            son.append(son[nom-1] + son[nom-2])
#    return son

#print(ketma_ketlik(15))
    


 

#def baholash(nomlar):
 #   """Bosh harfni kichikdan kattaga o'tkazish"""
#nomlar=[]
#r=1
#while True:
#     savol=f"{r}-İsm kiriting! :"
#    nom=input(savol)
#    nomlar.append(nom)
#    ilova=input("Yana ism qo'shasizmi? (xa\yo'q) :")
#    r+=1 
#    if ilova=="yo'q":
#       break
#for nom in nomlar:
#   print(nom)    
#print(nomlar)
#baholash(nomlar)

#def katta_harf(matnlar):
#    for i in range(len(matnlar)):
#        matnlar[i]=matnlar[i].title()

#ismlar=['ali','vali','olim','ahmad']
#yangi_royxat=ismlar[:]
#katta_harf(ismlar)
#print(yangi_royxat)
#print(ismlar)    

#talabalar=['ali','vali','ahmad','mahmud']
#def bahola(ismlar):
#    baholar={}
#    for ism in ismlar:
#        baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#        baholar[ism]=baho
#    return baholar

#baholar=bahola(talabalar)
#print(baholar)
#print(talabalar)

#def summa(*sonlar):
#    """Yig'indini hisoblovchi funksiya"""
#    yigindi=0
#    for son in sonlar:
#        yigindi+=son
#    return yigindi

#print(summa(3,6))


#def raqam(*nomlar):
 #   """sonlarning yig'indisini hisoblaovchi funksiya"""
 #   return sum(nomlar)
#print(raqam(7,3))

#def son(l,t,*raqamlar):
#    """Yig'indi hisobovchi funksiya"""
#    return l+t+sum(raqamlar)
#print(son(45,12))
#def avto_malumot(ishlab_chiqaruvchi,masofa,yili,**malumot):
#    """Avtomobil haqida malumot beruvchi funksiya"""
#    malumot['ishlab_chiqaruvchi']=ishlab_chiqaruvchi
#    malumot['masofa']=masofa
#    malumot['yili']=yili
#    return malumot
#avtosalon=avto_malumot('porsche','0',2022,rangi='qora',narxi='60000 €')
    
#def son(*raqam):
#    """Sonlarning ko'paytmasini kaytaruvchi dastur"""
#    kopaytma=1
#    for nom in raqam:
#       kopaytma*=nom
#    return kopaytma
#print(son(4,2))    

#def talaba_nomi(ism,familiya,**malumot):
#    """Talabalar haqida umumiy ma'lumot"""
#    malumot['ism']=ism
#    malumot['familiya']=familiya
 #    return malumot

#talaba=talaba_nomi("ulug'bek",'xoliq',tugilgan_yili='1971',kasbi='shifokor')




#def daraja(n):
#    return lambda x:x**n
#kvadrat=daraja(2)
# kub=daraja(3)
#print(f"5-ning kvadrati {kvadrat(5)} ga teng!. Kubi esa {kub(5)} ga teng!")

#from math import sqrt
#sonlar=list(range(6))
#ildiz=list(map(sqrt,sonlar))

#print(ildiz)


#from math import sqrt
#sonlar=list(range(6))
#ildiz=list(map(sqrt,sonlar))

#def daraja2(x):
 #   """Berilgan sonning kvadratini qaytaruvchi funksiya"""
 #   return x*x
#print(list(map(daraja2,sonlar)))



#from math import sqrt

#sonlar=list(range(6))
#kvadrat=list(map(lambda x:x*x,sonlar))
#print(kvadrat)

#a=[7,8]
#b=[3,6]
#ekle=list(map(lambda x,y:x+y,a,b))
#print(ekle)


#import random
#sonlar=random.sample(range(100),10)
#print(sonlar)
#def juftmi(r):
#    """r juft son bo'lsa true ,aks holda false qaytaradigan funksiya"""
#    return r%2==0
#juft=list(filter(juftmi,sonlar))
#print(juft)


#import random
#sonlar=random.sample(range(100),10)
#print(sonlar)

#def toqmi(u):
 #  """Agar u toq bo'lsa true,aks holda false qaytaruvchi funksiya"""
#jft=list(filter(lambda son:son%2==1,sonlar))
#print(jft)






#mevalar=['gilos','hurmo','olxori','anor','bexi']
#harf='h'
#mevas=list(filter(lambda meva:meva.startswith(harf),mevalar))
#print(meva)



#harf='h'
#mevas=list(filter(lambda meva:meva.startswith(harf),mevalar))
mevalar=['gilos','hurmo','olxori','anor','bexi']
meva2=list(filter(lambda meva:len(meva)>=6,mevalar))
print(meva2)


























  
  
    
  
