# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:40:36 2024

@author: Al Hilol
"""

#men=input('Biror bir so\'z kiriting! :')
#if men.lower()=='hilol':
#    print('Parol to\'g\'ri!')
#elif men.lower()=='qasos':
#    print('Ehtiyot bo\'ling, xafli harakat qilmoqdasiz !')
#elif men.lower()=='salom':
#    print('Parol noto\'g\'ri !')
#else:
#    print('İltimos yaxshiroq o\'ylang !')

#dokon=['un','guruch','go\'sht','olma','moy','kartoshka','shakar','ziravorlar']
#mahsulotlar=['go\'sht','sabzi' ,'shakar','qulpunay','moy']
#if mahsulotlar:
# for narsa in mahsulotlar:
#    if narsa in dokon:
#        print(f'Do\'konimizda {narsa} bor !')   
#    else:
#        print(f'Afsuski {narsa} yo\'q!')


#dokon=['un','guruch','go\'sht','olma','moy','kartoshka','shakar','ziravorlar']
#mahsulot=[]
#for savdo in range(4):
#    mahsulot.append(input(f'{savdo+1} - mahsulot nomini kiriting! :'))
#for savdo in mahsulot:
#    if savdo in dokon:
#       print(f'Buyerda {savdo} topiladi !')
#    else:
#       print(f'Bizning do\'konda hozircha {savdo} yo\'q!')
        

#car={'model':'TOGG','color':'gray'}
#print(f"Men kelajakda {car['model']} modelli va {car['color']} rangli avtomobil olaman!")       
#en_uz={'apple':'olma','apricot':'o\'rik'}
#print(en_uz['apricot'])       
        
#mevalar={'olma':1000,'tavruz':8000}
#print(f"Olma narxi {mevalar['olma']} so\'m !  ") 

#talaba={'ism':'mahmud olimiy','yosh':'27','kurs':'2'}
#print(f"{talaba['ism'].title()} {talaba['yosh']} yoshda va {talaba['kurs']}-kursda o\'qimoqda!")
#talaba['kurs']=3
#talaba['fakultet']='İqtisodiyot'


#talaba={}
#talaba['ism']='qobil rasuliy'
#talaba['kasbi']='muhandis'
#talaba['yosh']='25'
#print(f"Janob {talaba['ism'].title()}, kasbi {talaba['kasbi']},yoshi {talaba['yosh']} da !")

#talaba['holati']='uylanmagan'
#talaba['moddiy holat']='boy'
#del talaba['yosh']
#print('talaba')
#talaba['2-nomi']='al-hilol'


#telefon={
#    'asad':'iphone 15 pro',
#    'muhtor':'galaxy',    
#    'umar':'mi a6',
#    'rasul':'nokia 1210'
#}
#phone=telefon.get('bobur','Bunday ism mavjud emas!')
#print(phone)

#Onajonim={'ismi':'mahfiratxon xoliqiy','tugilgan_yili':'1968','tugilgan_joyi':'asaka tumani'}
#print(f"Mening Onam {Onajonim['ismi'].title()} {Onajonim['tugilgan_yili']}-yil {Onajonim['tugilgan_joyi'].title()}da tugilgan!")
#vakil={'ism':'dadam','dadam':'kabob','ismi':'onam','onam':'xonim','nom':'akam','akam':'tandir'}
#print(f"1-{vakil['ism'].title()}ning sevimli taomi {vakil['dadam']}!,\
#2-{vakil['ismi'].title()}ning sevimli taomi {vakil['onam']}!,\
#2-{vakil['nom'].title()}ning sevimli taomi {vakil['akam']}!")

#ism={
#     'translator':'tarjima',
#     'integer':'butun son',
#    'float':'o\'nlik son',
#     'string':'matn',
#     'if':'agar',
#     'else':'aks holda',
#     'or':'yoki',
#     'and':'va',
#     'elif':'agar aks holda',
#     'type':'turi',
#     'do':'bajar'
#}
#kalit=input('Kalit so\'zni kiriting! :').lower()
#print(ism.get(kalit,'Bunday so\'z mavjud emas!'))

#ism={
#     'translator':'tarjima',
#     'integer':'butun son',
#     'float':'o\'nlik son',
#     'string':'matn',
#     'if':'agar',
#     'else':'aks holda',
#     'or':'yoki',
#     'and':'va',
#     'elif':'agar aks holda',
#     'type':'turi',
#     'do':'bajar'
#}
#kalit=input("Kalit so\'z kiriting! :".lower())
#tarjima=ism.get(kalit)
#if tarjima==None:
#    print('Bunday qiymat mavjud emas!')
#else:
#    print(f'{kalit.title()} so\'zi {tarjima} deb tarjima qilimadi!')
#lugat=input('Kalit so\'zni kiriting! :')
#nom={'human':'inson',
 #    'male':'erkak',
  #   'female':'ayol',
   #  'child':'bolalar'
#} 
#print(nom.get(lugat,'Bunday nom mavjud emas!'))

#talaba={
#'ism':'ali',
#'familiya':'shams',
#'yosh':22
#}
#print(talaba.items())

#for kalit,qiymat in talaba.items():
#    print(f"Kalit:{kalit}")
#    print(f"Qiymat:{qiymat} \n")

#telefon={
#'ali':'iphone x',
#'olim':'galaxy s9',
#'iso':'mi06',
#'nur':'oppo',
#'karim':'mi06',
#'bunyod':'iphone x'
#}
#print('Foydalanuvchining telefon modellari! :')
#for tel in set(telefon.values()):
 #   print(tel)
#for k,q in telefon.items():
#    print(f"{k.title()}ning telefoni {q}")
#ishchilar={
#'ali':'iphone x',
#'olim':'galaxy s9',
#'jasur':'mi7',
#'bahrom':'reel 23'
#}
#print('Do\'kondagi ishchilar:')
#for ism in sorted(ishchilar):
#    print(ism.title())
#mahsulotlar={
#'uzum':2500,
#'nok':3000    
#}


#bozorlik=['anor','uzum','nok','gilos']
#for mahsulot in mahsulotlar:    
#  if mahsulot in bozorlik:
#      print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#     
#
#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"iltimos,Do\'koningizga {buyum.title()} ham olib keling!")



#meva={'olma','nok','anor'}
#print(type(meva))



#lugat={
#     'translator':'tarjima',
#    'integer':'butun son',
#     'float':'o\'nlik son',
#    'string':'matn',
#     'if':'agar',
#     'else':'aks holda',
#     'or':'yoki',
#     'and':'va',
#     'elif':'agar aks holda',
#     'type':'turi',
#     'do':'bajar'
#}
#for kalit,qiymat in sorted(lugat.items()):
#    print(f"{kalit} - {qiymat}")
#
#print('_Davlat nomlari :')
#davlati={
#'o\'zbekiston':'toshkent',
#'singapur':'sungapur',
#'turkiya':'anqara',
#'germaniya':'berlin',
#'aqsh':'washington',
#'saudiya arabistoni':'jiddah'
#}
#for davlat in sorted(davlati):
#    print(davlat.upper())

#print('_Davlat poytaxtlari :')
#poytaxti={
#'o\'zbekiston':'toshkent',
#'singapur':'sungapur',
#'turkiya':'anqara',
#'germaniya':'berlin',
#'aqsh':'washington',
#'saudiya arabistoni':'jiddah'
#}
#for poytaxt in sorted(poytaxti.values()):
#   print(poytaxt.title())

#davlat=input('İstalgan davlat nomini kiriting! :')
#nom={
#  'o\'zbekiston':'toshkent',
#  'singapur':'sungapur',
#  'turkiya':'anqara',
#  'germaniya':'berlin',
#  'aqsh':'washington',
#  'saudiya arabistoni':'jiddah'   
#}
#ism=nom.get(davlat)
#if ism==None:
#    print('Kechirasiz,Bizda bunday ma\'lumot mavjud emas!')
#else:
#    print(f"{davlat.title()}ning poytaxti {ism.title()} shahri!")


#print('Xush kelibsiz,Buyurtma berishingiz mumkin!')
#menu={
#'kabob':1500,
#'palov':1000,
#'tandir':2000,
#'salat':1500,
#'issiq non':3000,
#'choy':1000
#}
#buyurtmalar=[]
#for ism in range(4):
#    buyurtmalar.append(input(f"{ism+1}- taomni kiriting! :"))
#    for buyurtma in buyurtmalar:
#        if buyurtma in menu:
#            print(f"{buyurtma.title()} {menu[buyurtma]} so'm ")
#        else:
#            print(f"Kechirasiz,Bizda {buyurtma} mavjud emas!")
 

#car0={
# 'model':'audi 08',
# 'rang':'oq',
# 'yil':2019,
# 'narx':'120000'
#}
#car1={
# 'model':'bmw',
# 'rang':'gray',
# 'yil':2022,
# 'narx':'100000'
#}
#car2={
# 'model':'togg',
# 'rang':'oq',
# 'yil':2024,
# 'narx':'50000'
#}
#cars=[car0,car1,car2]
#for car in cars:
#    print(f"{car['model'].title()}, {car['rang']} rang {car['yil']} yil {car['narx']} $")

#print(f"{cars[1] ['rang'].title()} {cars[2] ['model'].title()


    if malibu['turi']=='avto'
         malibu['narx']=35000
    else:
       malibu['narx']=23000
    for malibu in malibus:
      

dastur={
 'ali':['python','c++'],
 'nozim':['html','java'],
 'mahmud':['js','css']
}
for ism,tillar in dastur.items():
    print(f" {ism.title()} quydagi dasturlarni biladi:")
    for til in tillar:
        print(til.upper())


hamkasb={
    'umar':{'familiya':'ergashbek',
        't_yil':1997,
        'malumoti':'oliy',
        'kasbi':'oshpaz',
        'tillar':['-python','-c++']
        },
    'orif':{'familiya':'bekali',
        't_yil':1993,
        'malumoti':'o\'rta maxsus',
        'kasbi':'muhandis',
        'tillar':['-c#','-java']
        },
    'nozim':{'familiya':'quddusiy',
        't_yil':1999,
        'malumoti':'oliy',
        'kasbi':'dasturchi',
        'tillar':['-html','-css','-js']},
    }
}
for ism,info in hamkasb.items():
    print(f"{ism.title()} {info['familiya'].title()},"
          f"{info['t_yil']}- yilda tug\'ilgan. "
          f"Malumoti : {info['malumoti']}, "
          f"Kasbi esa {info['kasbi']}dir."
          f"Quydagi dasturlash tillarini biladi! :")
    for til in info ['tillar']:
        print(til.title())

