#importuvanya
from random import randint
import math
import time
from main import num_players





#staty
name1="Bio"
shvydkosrilnist11 = 65
shvydkosrilnist12 = 70
tochnist11 = 92
tochnist12 = 83
shvydkist1 = 70
name2="Lagreid"
shvydkosrilnist21 = 70
shvydkosrilnist22 = 75
tochnist21 = 97
tochnist22 = 89
shvydkist2 = 65
name3="3"
shvydkosrilnist31 = 80
shvydkosrilnist32 = 80
tochnist31 = 80
tochnist32 = 80
shvydkist3 = 80
name4="4"
shvydkosrilnist41 = 80
shvydkosrilnist42 = 80
tochnist41 = 80
tochnist42 = 80
shvydkist4 = 80
name5="5"
shvydkosrilnist51 = 80
shvydkosrilnist52 = 80
tochnist51 = 80
tochnist52 = 80
shvydkist5 = 80
name6="6"
shvydkosrilnist61 = 80
shvydkosrilnist62 = 80
tochnist61 = 80
tochnist62 = 80
shvydkist6 = 80
name7="7"
shvydkosrilnist71 = 80
shvydkosrilnist72 = 80
tochnist71 = 80
tochnist72 = 80
shvydkist7 = 80
name8="8"
shvydkosrilnist81 = 80
shvydkosrilnist82 = 80
tochnist81 = 80
tochnist82 = 80
shvydkist8 = 80
name9="9"
shvydkosrilnist91 = 80
shvydkosrilnist92 = 80
tochnist91 = 80
tochnist92 = 80
shvydkist9 = 80
name10="10"
shvydkosrilnist101 = 80
shvydkosrilnist102 = 80
tochnist101 = 80
tochnist102 = 80
shvydkist10 = 80
name11="11"
shvydkosrilnist111 = 80
shvydkosrilnist112 = 80
tochnist111 = 80
tochnist112 = 80
shvydkist11 = 80
name12="12"
shvydkosrilnist121 = 80
shvydkosrilnist122 = 80
tochnist121 = 80
tochnist122 = 80
shvydkist12 = 80





#zminni
shtraf1=0
shtraf2=0
shtraf3=0
shtraf4=0
shtrafne_kolo=3
vsi_promahy1=""
vsi_promahy2=""
vsi_promahy3=""
vsi_promahy4=""
promahy1=0
promahy2=0
promahy3=0
promahy4=0
# promahy101=0
# promahy102=0
# promahy103=0
varianty = ""
vybir=""
sh_promahy1=0
sh_promahy2=0
sh_promahy3=0
sh_promahy4=0
sh_shvydkosrilnist1=0
sh_shvydkosrilnist2=0
sh_shvydkosrilnist3=0
sh_shvydkosrilnist4=0







#Function
def shtraf():
    global shtraf1, shtraf2, shtraf3, shtraf4, sh_promahy1, sh_promahy2, sh_promahy3, sh_promahy4

    if vybir=="11" or vybir=="12":
        shtraf1=0
        shtraf1=shtrafne_kolo*sh_promahy1

    
    if vybir=="21" or vybir=="22":
        shtraf2=0
        shtraf2=shtrafne_kolo*sh_promahy2
        

    
    if vybir=="31" or vybir=="32":
        shtraf3=0
        shtraf3=shtrafne_kolo*sh_promahy3
        
        
    
    if vybir=="41" or vybir=="42":
        shtraf4=0
        shtraf4=shtrafne_kolo*sh_promahy4
        










def hid(shvydkist, gravetc):
    global shtraf1, shtraf2, shtraf3, shtraf4, sh_shvydkosrilnist1, sh_shvydkosrilnist2, sh_shvydkosrilnist3, sh_shvydkosrilnist4
    result_hid=0
    for i in range(10):
        a=randint(1, 100)
        if a<=shvydkist:
            result_hid += 1
    print(result_hid)


    if gravetc == gravetc1:
        print(sh_shvydkosrilnist1)
        if shtraf1==0:
            print(gravetc + " - " + str(result_hid+sh_shvydkosrilnist1))
        else:
            shtraf1=shtraf1-result_hid-sh_shvydkosrilnist1
            if shtraf1<0:
                result_hid=abs(shtraf1)
                shtraf1=0
                sh_shvydkosrilnist1=0
                print(gravetc + " - " + str(result_hid))
            else:
                print(gravetc + " - на штрафному колі")
        sh_shvydkosrilnist1=0


    if gravetc == gravetc2:
        print(sh_shvydkosrilnist2)
        if shtraf2==0:
            print(gravetc + " - " + str(result_hid+sh_shvydkosrilnist2))
        else:
            shtraf2=shtraf2-result_hid-sh_shvydkosrilnist2
            if shtraf2<0:
                result_hid=abs(shtraf2)
                shtraf2=0
                sh_shvydkosrilnist2=0
                print(gravetc + " - " + str(result_hid))
            else:
                print(gravetc + " - на штрафному колі")
        sh_shvydkosrilnist2=0


    if gravetc == gravetc3:
        print(sh_shvydkosrilnist3)
        if shtraf3==0:
            print(gravetc + " - " + str(result_hid+sh_shvydkosrilnist3))
        else:
            shtraf3=shtraf3-result_hid-sh_shvydkosrilnist3
            if shtraf3<0:
                result_hid=abs(shtraf3)
                shtraf3=0
                sh_shvydkosrilnist3=0
                print(gravetc + " - " + str(result_hid))
            else:
                print(gravetc + " - на штрафному колі")
        sh_shvydkosrilnist3=0

    if gravetc == gravetc4:
        print(sh_shvydkosrilnist4)
        if shtraf4==0:
            print(gravetc + " - " + str(result_hid+sh_shvydkosrilnist4))
        else:
            shtraf4=shtraf4-result_hid-sh_shvydkosrilnist4
            if shtraf4<0:
                result_hid=abs(shtraf4)
                shtraf4=0
                
                print(gravetc + " - " + str(result_hid))
            else:
                print(gravetc + " - на штрафному колі")
        sh_shvydkosrilnist4=0
    






def nasha_strilba(gravetc):
    global promahy
    input("Натисніть Enter, щоб почати: ")
    start_time = time.time()
    input("Введіть що-небудь і натисніть Enter, щоб зупинити: ")
    end_time = time.time()
    elapsed_time = end_time - start_time
    promahy=int(input("Введи кількість промахів"))
    plus=(30-elapsed_time)/2
    plus=float(plus)
    plus=round(plus)
    print("Стрільба "+gravetc+":")
    print("Швидкострільність - "+str(elapsed_time))
    print("Плюс за щвидкість - "+str(plus))
    print("Кількість промахів - "+str(promahy))












def strilba(tochnist, shvydkosrilnist):
    global promahy, sh_promahy1, sh_promahy2, sh_promahy3, sh_promahy4, sh_shvydkosrilnist1, sh_shvydkosrilnist2, sh_shvydkosrilnist3, sh_shvydkosrilnist4
    result11 = 0
    for i in range(5):
        a=randint(1, 100)
        if a<=tochnist:
            result11 += 1
    result11 = 5-result11
    result31 = 0
    for i in range(45):
        a=randint(1, 100)
        b=0
        c=randint(1,3)



        if a>shvydkosrilnist/1.5:
            result31 += 1
        if a == 100:
            b=1
            if c==1:
                result31 += 5
            if c == 2:
                result31 += 10
            if c == 3:
                result31 += 15
    if result31<15:
        result31 = 15
    if result31>35 and result31 < 40 and b < 1:
        result31 = result31 - randint(1,5)
    if result31>40 and result31 < 45 and b < 1:
        result31 = result31 - randint(1,5)
    plus1=(30-result31)/7
    plus1=float(plus1)
    plus1=round(plus1)
    print("Швидкострільність - "+str(result31))
    print("Плюс за щвидкість - "+str(plus1))
    print("Кількість промахів - "+str(result11))
    promahy=result11
    if vybir=="11" or vybir=="12":
        sh_promahy1=result11
        sh_shvydkosrilnist1=plus1
    if vybir=="21" or vybir=="22":
        sh_promahy2=result11
        sh_shvydkosrilnist2=plus1
    if vybir=="31" or vybir=="32":
        sh_promahy3=result11
        sh_shvydkosrilnist3=plus1
    if vybir=="41" or vybir=="42":
        sh_shvydkosrilnist4=plus1
        sh_promahy4=result11
    
    shtraf()










def perevirka(gravetc, nomer1_4):
    global gravetc1, gravetc2, gravetc3, gravetc4, gravetc5, gravetc6, gravetc7, gravetc8, gravetc9, gravetc10, gravetc11, gravetc12
    global n_tochnist11, n_tochnist12, n_shvydkosrilnist11, n_shvydkist1, n_shvydkosrilnist12
    global n_tochnist21, n_tochnist22, n_shvydkosrilnist21, n_shvydkist2, n_shvydkosrilnist22
    global n_tochnist31, n_tochnist32, n_shvydkosrilnist31, n_shvydkist3, n_shvydkosrilnist32
    global n_tochnist41, n_tochnist42, n_shvydkosrilnist41, n_shvydkist4, n_shvydkosrilnist42
    if nomer1_4==1:
        if gravetc=="1":
            gravetc1=name1+"(Червоний)"
            n_tochnist11=tochnist11
            n_tochnist12=tochnist12
            n_shvydkosrilnist11=shvydkosrilnist11
            n_shvydkosrilnist12=shvydkosrilnist12
            n_shvydkist1=shvydkist1
        if gravetc=="2":
            gravetc1=name2+"(Червоний)"
            n_tochnist11=tochnist21
            n_tochnist12=tochnist22
            n_shvydkosrilnist11=shvydkosrilnist21
            n_shvydkosrilnist12=shvydkosrilnist22
            n_shvydkist1=shvydkist2
        if gravetc=="3":
            gravetc1=name3+"(Червоний)"
            n_tochnist11=tochnist31
            n_tochnist12=tochnist32
            n_shvydkosrilnist11=shvydkosrilnist31
            n_shvydkosrilnist12=shvydkosrilnist32
            n_shvydkist1=shvydkist3
        if gravetc=="4":
            gravetc1=name4+"(Червоний)"
            n_tochnist11=tochnist41
            n_tochnist12=tochnist42
            n_shvydkosrilnist11=shvydkosrilnist41
            n_shvydkosrilnist12=shvydkosrilnist42
            n_shvydkist1=shvydkist4
        if gravetc=="5":
            gravetc1=name5+"(Червоний)"
            n_tochnist11=tochnist51
            n_tochnist12=tochnist52
            n_shvydkosrilnist11=shvydkosrilnist51
            n_shvydkosrilnist12=shvydkosrilnist52
            n_shvydkist1=shvydkist5
        if gravetc=="6":
            gravetc1=name6+"(Червоний)"
            n_tochnist11=tochnist61
            n_tochnist12=tochnist62
            n_shvydkosrilnist11=shvydkosrilnist61
            n_shvydkosrilnist12=shvydkosrilnist62
            n_shvydkist1=shvydkist6
        if gravetc=="7":
            gravetc1=name7+"(Червоний)"
            n_tochnist11=tochnist71
            n_tochnist12=tochnist72
            n_shvydkosrilnist11=shvydkosrilnist71
            n_shvydkosrilnist12=shvydkosrilnist72
            n_shvydkist1=shvydkist7
        if gravetc=="8":
            gravetc1=name8+"(Червоний)"
            n_tochnist11=tochnist81
            n_tochnist12=tochnist82
            n_shvydkosrilnist11=shvydkosrilnist81
            n_shvydkosrilnist12=shvydkosrilnist82
            n_shvydkist1=shvydkist8
        if gravetc=="9":
            gravetc1=name9+"(Червоний)"
            n_tochnist11=tochnist91
            n_tochnist12=tochnist92
            n_shvydkosrilnist11=shvydkosrilnist91
            n_shvydkosrilnist12=shvydkosrilnist92
            n_shvydkist1=shvydkist9
        if gravetc=="10":
            gravetc1=name10+"(Червоний)"
            n_tochnist11=tochnist101
            n_tochnist12=tochnist102
            n_shvydkosrilnist11=shvydkosrilnist101
            n_shvydkosrilnist12=shvydkosrilnist102
            n_shvydkist1=shvydkist10
        if gravetc=="11":
            gravetc1=name11+"(Червоний)"
            n_tochnist11=tochnist111
            n_tochnist12=tochnist112
            n_shvydkosrilnist11=shvydkosrilnist111
            n_shvydkosrilnist12=shvydkosrilnist112
            n_shvydkist1=shvydkist11
        if gravetc=="12":
            gravetc1=name12+"(Червоний)"
            n_tochnist11=tochnist121
            n_tochnist12=tochnist122
            n_shvydkosrilnist12=shvydkosrilnist121
            n_shvydkosrilnist12=shvydkosrilnist122
            n_shvydkist1=shvydkist12




    if nomer1_4==2:
            if gravetc=="1":
                gravetc2=name1+"(Жовтий)"
                n_tochnist21=tochnist11
                n_tochnist22=tochnist12
                n_shvydkosrilnist21=shvydkosrilnist11
                n_shvydkosrilnist22=shvydkosrilnist12
                n_shvydkist2=shvydkist1
            if gravetc=="2":
                gravetc2=name2+"(Жовтий)"
                n_tochnist21=tochnist21
                n_tochnist22=tochnist22
                n_shvydkosrilnist21=shvydkosrilnist21
                n_shvydkosrilnist22=shvydkosrilnist22
                n_shvydkist2=shvydkist2
            if gravetc=="3":
                gravetc2=name3+"(Жовтий)"
                n_tochnist21=tochnist31
                n_tochnist22=tochnist32
                n_shvydkosrilnist21=shvydkosrilnist31
                n_shvydkosrilnist22=shvydkosrilnist32
                n_shvydkist2=shvydkist3
            if gravetc=="4":
                gravetc2=name4+"(Жовтий)"
                n_tochnist21=tochnist41
                n_tochnist22=tochnist42
                n_shvydkosrilnist21=shvydkosrilnist41
                n_shvydkosrilnist22=shvydkosrilnist42
                n_shvydkist2=shvydkist4
            if gravetc=="5":
                gravetc2=name5+"(Жовтий)"
                n_tochnist21=tochnist51
                n_tochnist22=tochnist52
                n_shvydkosrilnist21=shvydkosrilnist51
                n_shvydkosrilnist22=shvydkosrilnist52
                n_shvydkist2=shvydkist5
            if gravetc=="6":
                gravetc2=name6+"(Жовтий)"
                n_tochnist21=tochnist61
                n_tochnist22=tochnist62
                n_shvydkosrilnist21=shvydkosrilnist61
                n_shvydkosrilnist22=shvydkosrilnist62
                n_shvydkist2=shvydkist6
            if gravetc=="7":
                gravetc2=name7+"(Жовтий)"
                n_tochnist21=tochnist71
                n_tochnist22=tochnist72
                n_shvydkosrilnist21=shvydkosrilnist71
                n_shvydkosrilnist22=shvydkosrilnist72
                n_shvydkist2=shvydkist7
            if gravetc=="8":
                gravetc2=name8+"(Жовтий)"
                n_tochnist21=tochnist81
                n_tochnist22=tochnist82
                n_shvydkosrilnist21=shvydkosrilnist81
                n_shvydkosrilnist22=shvydkosrilnist82
                n_shvydkist2=shvydkist8
            if gravetc=="9":
                gravetc2=name9+"(Жовтий)"
                n_tochnist21=tochnist91
                n_tochnist22=tochnist92
                n_shvydkosrilnist21=shvydkosrilnist91
                n_shvydkosrilnist22=shvydkosrilnist92
                n_shvydkist2=shvydkist9
            if gravetc=="10":
                gravetc2=name10+"(Жовтий)"
                n_tochnist21=tochnist101
                n_tochnist22=tochnist102
                n_shvydkosrilnist21=shvydkosrilnist101
                n_shvydkosrilnist22=shvydkosrilnist102
                n_shvydkist2=shvydkist10
            if gravetc=="11":
                gravetc2=name11+"(Жовтий)"
                n_tochnist21=tochnist111
                n_tochnist22=tochnist112
                n_shvydkosrilnist21=shvydkosrilnist111
                n_shvydkosrilnist22=shvydkosrilnist112
                n_shvydkist2=shvydkist11
            if gravetc=="12":
                gravetc2=name12+"(Жовтий)"
                n_tochnist21=tochnist121
                n_tochnist22=tochnist122
                n_shvydkosrilnist21=shvydkosrilnist121
                n_shvydkosrilnist22=shvydkosrilnist122
                n_shvydkist2=shvydkist12


    if nomer1_4==3:
            if gravetc=="1":
                gravetc3=name1+"(Зелений)"
                n_tochnist31=tochnist11
                n_tochnist32=tochnist12
                n_shvydkosrilnist31=shvydkosrilnist11
                n_shvydkosrilnist32=shvydkosrilnist12
                n_shvydkist3=shvydkist1
            if gravetc=="2":
                gravetc3=name2+"(Зелений)"
                n_tochnist31=tochnist21
                n_tochnist32=tochnist22
                n_shvydkosrilnist31=shvydkosrilnist21
                n_shvydkosrilnist32=shvydkosrilnist22
                n_shvydkist3=shvydkist2
            if gravetc=="3":
                gravetc3=name3+"(Зелений)"
                n_tochnist31=tochnist31
                n_tochnist32=tochnist32
                n_shvydkosrilnist31=shvydkosrilnist31
                n_shvydkosrilnist32=shvydkosrilnist32
                n_shvydkist3=shvydkist3
            if gravetc=="4":
                gravetc3=name4+"(Зелений)"
                n_tochnist31=tochnist41
                n_tochnist32=tochnist42
                n_shvydkosrilnist31=shvydkosrilnist41
                n_shvydkosrilnist32=shvydkosrilnist42
                n_shvydkist3=shvydkist4
            if gravetc=="5":
                gravetc3=name5+"(Зелений)"
                n_tochnist31=tochnist51
                n_tochnist32=tochnist52
                n_shvydkosrilnist31=shvydkosrilnist51
                n_shvydkosrilnist32=shvydkosrilnist52
                n_shvydkist3=shvydkist5
            if gravetc=="6":
                gravetc3=name6+"(Зелений)"
                n_tochnist31=tochnist61
                n_tochnist32=tochnist62
                n_shvydkosrilnist31=shvydkosrilnist61
                n_shvydkosrilnist32=shvydkosrilnist62
                n_shvydkist3=shvydkist6
            if gravetc=="7":
                gravetc3=name7+"(Зелений)"
                n_tochnist31=tochnist71
                n_tochnist32=tochnist72
                n_shvydkosrilnist31=shvydkosrilnist71
                n_shvydkosrilnist32=shvydkosrilnist72
                n_shvydkist3=shvydkist7
            if gravetc=="8":
                gravetc3=name8+"(Зелений)"
                n_tochnist31=tochnist81
                n_tochnist32=tochnist82
                n_shvydkosrilnist31=shvydkosrilnist81
                n_shvydkosrilnist32=shvydkosrilnist82
                n_shvydkist3=shvydkist8
            if gravetc=="9":
                gravetc3=name9+"(Зелений)"
                n_tochnist31=tochnist91
                n_tochnist32=tochnist92
                n_shvydkosrilnist31=shvydkosrilnist91
                n_shvydkosrilnist32=shvydkosrilnist92
                n_shvydkist3=shvydkist9
            if gravetc=="10":
                gravetc3=name10+"(Зелений)"
                n_tochnist31=tochnist101
                n_tochnist32=tochnist102
                n_shvydkosrilnist31=shvydkosrilnist101
                n_shvydkosrilnist32=shvydkosrilnist102
                n_shvydkist3=shvydkist10
            if gravetc=="11":
                gravetc3=name11+"(Зелений)"
                n_tochnist31=tochnist111
                n_tochnist32=tochnist112
                n_shvydkosrilnist31=shvydkosrilnist111
                n_shvydkosrilnist32=shvydkosrilnist112
                n_shvydkist3=shvydkist11
            if gravetc=="12":
                gravetc3=name12+"(Зелений)"
                n_tochnist31=tochnist121
                n_tochnist32=tochnist122
                n_shvydkosrilnist31=shvydkosrilnist121
                n_shvydkosrilnist32=shvydkosrilnist122
                n_shvydkist3=shvydkist12



    if nomer1_4==4:
            if gravetc=="1":
                gravetc4=name1+"(Синій)"
                n_tochnist41=tochnist11
                n_tochnist42=tochnist12
                n_shvydkosrilnist41=shvydkosrilnist11
                n_shvydkosrilnist42=shvydkosrilnist12
                n_shvydkist4=shvydkist1
            if gravetc=="2":
                gravetc4=name2+"(Синій)"
                n_tochnist41=tochnist21
                n_tochnist42=tochnist22
                n_shvydkosrilnist41=shvydkosrilnist21
                n_shvydkosrilnist42=shvydkosrilnist22
                n_shvydkist4=shvydkist2
            if gravetc=="3":
                gravetc4=name3+"(Синій)"
                n_tochnist41=tochnist31
                n_tochnist42=tochnist32
                n_shvydkosrilnist41=shvydkosrilnist31
                n_shvydkosrilnist42=shvydkosrilnist32
                n_shvydkist4=shvydkist3
            if gravetc=="4":
                gravetc4=name4+"(Синій)"
                n_tochnist41=tochnist41
                n_tochnist42=tochnist42
                n_shvydkosrilnist41=shvydkosrilnist41
                n_shvydkosrilnist42=shvydkosrilnist42
                n_shvydkist4=shvydkist4
            if gravetc=="5":
                gravetc4=name5+"(Синій)"
                n_tochnist41=tochnist51
                n_tochnist42=tochnist52
                n_shvydkosrilnist41=shvydkosrilnist51
                n_shvydkosrilnist42=shvydkosrilnist52
                n_shvydkist4=shvydkist5
            if gravetc=="6":
                gravetc4=name6+"(Синій)"
                n_tochnist41=tochnist61
                n_tochnist42=tochnist62
                n_shvydkosrilnist41=shvydkosrilnist61
                n_shvydkosrilnist42=shvydkosrilnist62
                n_shvydkist4=shvydkist6
            if gravetc=="7":
                gravetc4=name7+"(Синій)"
                n_tochnist41=tochnist71
                n_tochnist42=tochnist72
                n_shvydkosrilnist41=shvydkosrilnist71
                n_shvydkosrilnist42=shvydkosrilnist72
                n_shvydkist4=shvydkist7
            if gravetc=="8":
                gravetc4=name8+"(Синій)"
                n_tochnist41=tochnist81
                n_tochnist42=tochnist82
                n_shvydkosrilnist41=shvydkosrilnist81
                n_shvydkosrilnist42=shvydkosrilnist82
                n_shvydkist4=shvydkist8
            if gravetc=="9":
                gravetc4=name9+"(Синій)"
                n_tochnist41=tochnist91
                n_tochnist42=tochnist92
                n_shvydkosrilnist41=shvydkosrilnist91
                n_shvydkosrilnist42=shvydkosrilnist92
                n_shvydkist4=shvydkist9
            if gravetc=="10":
                gravetc4=name10+"(Синій)"
                n_tochnist41=tochnist101
                n_tochnist42=tochnist102
                n_shvydkosrilnist41=shvydkosrilnist101
                n_shvydkosrilnist42=shvydkosrilnist102
                n_shvydkist4=shvydkist10
            if gravetc=="11":
                gravetc4=name11+"(Синій)"
                n_tochnist41=tochnist111
                n_tochnist42=tochnist112
                n_shvydkosrilnist41=shvydkosrilnist111
                n_shvydkosrilnist42=shvydkosrilnist112
                n_shvydkist4=shvydkist11
            if gravetc=="12":
                gravetc4=name12+"(Синій)"
                n_tochnist41=tochnist121
                n_tochnist42=tochnist122
                n_shvydkosrilnist41=shvydkosrilnist121
                n_shvydkosrilnist42=shvydkosrilnist122
                n_shvydkist4=shvydkist12

















# Uchasnyky
# varianty = ""
# kilkist=input("Введи число компютерних гравців(1-4)")
# if kilkist="1":
#     gravetc1=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
#     if gravetc1=="1":
#         gravetc1=name1+"(Червоний)"
#     if gravetc1=="2":
#         gravetc1=name2+"(Червоний)"
#     if gravetc1=="3":
#         gravetc1=name3+"(Червоний)"
#     if gravetc1=="4":
#         gravetc1=name4+"(Червоний)"
#     if gravetc1=="5":
#         gravetc1=name5+"(Червоний)"
#     if gravetc1=="6":
#         gravetc1=name6+"(Червоний)"
#     if gravetc1=="7":
#         gravetc1=name7+"(Червоний)"
#     if gravetc1=="8":
#         gravetc1=name8+"(Червоний)"
#     if gravetc1=="9":
#         gravetc1=name9+"(Червоний)"
#     if gravetc1=="10":
#         gravetc1=name10+"(Червоний)"
#     if gravetc1=="11":
#         gravetc1=name11+"(Червоний)"
#     if gravetc1=="12":
#         gravetc1=name12+"(Червоний)"










# if kilkist="2":
#     gravetc1=input("Введи імя першого гравця цифрою, обираючи з варіантів:" + varianty)
#     if gravetc1=="1":
#         gravetc1=name1+"(Червоний)"
#     if gravetc1=="2":
#         gravetc1=name2+"(Червоний)"
#     if gravetc1=="3":
#         gravetc1=name3+"(Червоний)"
#     if gravetc1=="4":
#         gravetc1=name4+"(Червоний)"
#     if gravetc1=="5":
#         gravetc1=name5+"(Червоний)"
#     if gravetc1=="6":
#         gravetc1=name6+"(Червоний)"
#     if gravetc1=="7":
#         gravetc1=name7+"(Червоний)"
#     if gravetc1=="8":
#         gravetc1=name8+"(Червоний)"
#     if gravetc1=="9":
#         gravetc1=name9+"(Червоний)"
#     if gravetc1=="10":
#         gravetc1=name10+"(Червоний)"
#     if gravetc1=="11":
#         gravetc1=name11+"(Червоний)"
#     if gravetc1=="12":
#         gravetc1=name12+"(Червоний)"



#     gravetc2=input("Введи імя другого гравця цифрою, обираючи з варіантів:" + varianty)
#     if gravetc2=="1":
#         gravetc2=name1+"(Червоний)"
#     if gravetc2=="2":
#         gravetc2=name2+"(Червоний)"
#     if gravetc2=="3":
#         gravetc2=name3+"(Червоний)"
#     if gravetc1=="4":
#         gravetc1=name4+"(Червоний)"
#     if gravetc1=="5":
#         gravetc1=name5+"(Червоний)"
#     if gravetc1=="6":
#         gravetc1=name6+"(Червоний)"
#     if gravetc1=="7":
#         gravetc1=name7+"(Червоний)"
#     if gravetc1=="8":
#         gravetc1=name8+"(Червоний)"
#     if gravetc1=="9":
#         gravetc1=name9+"(Червоний)"
#     if gravetc1=="10":
#         gravetc1=name10+"(Червоний)"
#     if gravetc1=="11":
#         gravetc1=name11+"(Червоний)"
#     if gravetc1=="12":
#         gravetc1=name12+"(Червоний)"












# if kilkist="3":
#     gravetc1=input("Введи імя першого гравця цифрою, обираючи з варіантів:" + varianty)
#     gravetc2=input("Введи імя другого гравця цифрою, обираючи з варіантів:" + varianty)
#     gravetc3=input("Введи імя третього гравця цифрою, обираючи з варіантів:" + varianty)
# if kilkist="4":
#     gravetc1=input("Введи імя першого гравця цифрою, обираючи з варіантів:" + varianty)
#     gravetc2=input("Введи імя другого гравця цифрою, обираючи з варіантів:" + varianty)
#     gravetc3=input("Введи імя третього гравця цифрою, обираючи з варіантів:" + varianty)
#     gravetc4=input("Введи імя четвертого гравця цифрою, обираючи з варіантів:" + varianty)



#Uchasnyky



if kilkist=="1":
    gravetc1=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc1, 1)
    gravetc2=input("Введи імя першого справжнього гравця буквами")
    gravetc3=input("Введи імя другого справжнього гравця буквами")
    gravetc4=input("Введи імя третього справжнього гравця буквами")
if kilkist=="2":
    gravetc1=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc1, 1)
    gravetc2=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc2, 2)
    gravetc3=input("Введи імя першого справжнього гравця буквами")
    gravetc4=input("Введи імя другого справжнього гравця буквами")
if kilkist=="3":
    gravetc1=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc1, 1)
    gravetc2=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc2, 2)
    gravetc3=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc3, 3)
    gravetc4=input("Введи імя першого справжнього гравця буквами")
if kilkist=="4":
    gravetc1=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc1, 1)
    gravetc2=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc2, 2)
    gravetc3=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc3, 3)
    gravetc4=input("Введи імя компютерного гравця цифрою, обираючи з варіантів:" + varianty)
    perevirka(gravetc4, 4)




























#main
if kilkist=="1":
    vybir = input("-хід; 1-стрільба " + gravetc1 + "; к-кінець. Якщо стрільба лежачи дописуєте 1, якщо стояче 2. Стрільби першого справжнього гравця(" + gravetc2 + ") - 101. Стрільба другого справжнього гравця(" + gravetc3 + ") - 102. Стрільби третього справжнього гравця(" + gravetc4 + ") - 103.")
    while vybir != "к":
        if vybir == "11":
            print("Стрільба лежачи "+gravetc1+":")
            strilba(n_tochnist11, n_shvydkosrilnist11)
            promahy1+=promahy
            if vsi_promahy1 != "":
                vsi_promahy1+=" + "+str(promahy)
            else:
                vsi_promahy1+=str(promahy)
        if vybir == "12":
            print("Стрільба стоячи "+gravetc1+":")
            strilba(n_tochnist12, n_shvydkosrilnist12)
            promahy1+=promahy
            if vsi_promahy1 != "":
                vsi_promahy1+=" + "+str(promahy)
            else:
                vsi_promahy1+=str(promahy)
        if vybir == "101":
            nasha_strilba(gravetc2)
            promahy2+=promahy
            if vsi_promahy2 != "":
                vsi_promahy2+=" + "+str(promahy)
            else:
                vsi_promahy2+=str(promahy)
        if vybir == "102":
            nasha_strilba(gravetc3)
            promahy3+=promahy
            if vsi_promahy3 != "":
                vsi_promahy3+=" + "+str(promahy)
            else:
                vsi_promahy3+=str(promahy)
        if vybir == "103":
            nasha_strilba(gravetc4)
            promahy4+=promahy
            if vsi_promahy4 != "":
                vsi_promahy4+=" + "+str(promahy)
            else:
                vsi_promahy4+=str(promahy)
        if vybir=="":
            hid(n_shvydkist1, gravetc1)
        vybir = input("-хід; 1-стрільба " + gravetc1 + "; к-кінець. Якщо стрільба лежачи дописуєте 1, якщо стояче 2. Стрільби першого справжнього гравця(" + gravetc2 + ") - 101. Стрільба другого справжнього гравця(" + gravetc3 + ") - 102. Стрільби третього справжнього гравця(" + gravetc4 + ") - 103.")








if kilkist=="2":
    vybir = input("-хід; 1-стрільба " + gravetc1 + "; 2-стрільба " + gravetc2 + "; к-кінець. Якщо стрільба лежачи дописуєте 1, якщо стояче 2. Стрільби першого справжнього гравця(" + gravetc3 + ") - 101. Стрільба другого справжнього гравця(" + gravetc4 + ") - 102.")
    while vybir != "к":
        if vybir == "11":
            print("Стрільба лежачи "+gravetc1+":")
            strilba(n_tochnist11, n_shvydkosrilnist11)
            promahy1+=promahy
            if vsi_promahy1 != "":
                vsi_promahy1+=" + "+str(promahy)
            else:
                vsi_promahy1+=str(promahy)
        if vybir == "12":
            print("Стрільба стоячи "+gravetc1+":")
            strilba(n_tochnist12, n_shvydkosrilnist12)
            promahy1+=promahy
            if vsi_promahy1 != "":
                vsi_promahy1+=" + "+str(promahy)
            else:
                vsi_promahy1+=str(promahy)
        if vybir == "21":
            print("Стрільба лежачи "+gravetc2+":")
            strilba(n_tochnist21, n_shvydkosrilnist21)
            promahy2+=promahy
            if vsi_promahy2 != "":
                vsi_promahy2+=" + "+str(promahy)
            else:
                vsi_promahy2+=str(promahy)
        if vybir == "22":
            print("Стрільба стоячи "+gravetc2+":")
            strilba(n_tochnist22, n_shvydkosrilnist22)
            promahy2+=promahy
            if vsi_promahy2 != "":
                vsi_promahy2+=" + "+str(promahy)
            else:
                vsi_promahy2+=str(promahy)
        if vybir == "101":
            nasha_strilba(gravetc3)
            promahy3+=promahy
            if vsi_promahy3 != "":
                vsi_promahy3+=" + "+str(promahy)
            else:
                vsi_promahy3+=str(promahy)
        if vybir == "102":
            nasha_strilba(gravetc4)
            promahy4+=promahy
            if vsi_promahy4 != "":
                vsi_promahy4+=" + "+str(promahy)
            else:
                vsi_promahy4+=str(promahy)
        if vybir=="":
            hid(n_shvydkist1, gravetc1)
            hid(n_shvydkist2, gravetc2)
        vybir = input("-хід; 1-стрільба " + gravetc1 + "; 2-стрільба " + gravetc2 + "; к-кінець. Якщо стрільба лежачи дописуєте 1, якщо стояче 2. Стрільби першого справжнього гравця(" + gravetc2 + ") - 101. Стрільба другого справжнього гравця(" + gravetc3 + ") - 102.")







if kilkist=="3":
    vybir = input("-хід; 1-стрільба " + gravetc1 + "; 2-стрільба " + gravetc2 + "; 3-стрільба " + gravetc3 + "; к-кінець. Якщо стрільба лежачи дописуєте 1, якщо стояче 2. Стрільби першого справжнього гравця(" + gravetc4 + ") - 101.")
    while vybir != "к":
        if vybir == "11":
            print("Стрільба лежачи "+gravetc1+":")
            strilba(n_tochnist11, n_shvydkosrilnist11)
            promahy1+=promahy
            if vsi_promahy1 != "":
                vsi_promahy1+=" + "+str(promahy)
            else:
                vsi_promahy1+=str(promahy)
        if vybir == "12":
            print("Стрільба стоячи "+gravetc1+":")
            strilba(n_tochnist12, n_shvydkosrilnist12)
            promahy1+=promahy
            if vsi_promahy1 != "":
                vsi_promahy1+=" + "+str(promahy)
            else:
                vsi_promahy1+=str(promahy)
        if vybir == "21":
            print("Стрільба лежачи "+gravetc2+":")
            strilba(n_tochnist21, n_shvydkosrilnist21)
            promahy2+=promahy
            if vsi_promahy2 != "":
                vsi_promahy2+=" + "+str(promahy)
            else:
                vsi_promahy2+=str(promahy)
        if vybir == "22":
            print("Стрільба стоячи "+gravetc2+":")
            strilba(n_tochnist22, n_shvydkosrilnist22)
            promahy2+=promahy
            if vsi_promahy2 != "":
                vsi_promahy2+=" + "+str(promahy)
            else:
                vsi_promahy2+=str(promahy)
        if vybir == "31":
            print("Стрільба лежачи "+gravetc3+":")
            strilba(n_tochnist31, n_shvydkosrilnist31)
            promahy3+=promahy
            if vsi_promahy3 != "":
                vsi_promahy3+=" + "+str(promahy)
            else:
                vsi_promahy3+=str(promahy)
        if vybir == "32":
            print("Стрільба стоячи "+gravetc3+":")
            strilba(n_tochnist32, n_shvydkosrilnist32)
            promahy3+=promahy
            if vsi_promahy3 != "":
                vsi_promahy3+=" + "+str(promahy)
            else:
                vsi_promahy3+=str(promahy)
        if vybir == "101":
            nasha_strilba(gravetc4)
            promahy4+=promahy
            if vsi_promahy4 != "":
                vsi_promahy4+=" + "+str(promahy)
            else:
                vsi_promahy4+=str(promahy)
        if vybir=="":
            hid(n_shvydkist1, gravetc1)
            hid(n_shvydkist2, gravetc2)
            hid(n_shvydkist3, gravetc3)
        vybir = input("-хід; 1-стрільба " + gravetc1 + "; 2-стрільба " + gravetc2 + "; 3-стрільба " + gravetc3 + "; к-кінець. Якщо стрільба лежачи дописуєте 1, якщо стояче 2. Стрільби першого справжнього гравця(" + gravetc2 + ") - 101.")








if kilkist=="4":
    vybir = input("-хід; 1-стрільба " + gravetc1 + "; 2-стрільба " + gravetc2 + "; 3-стрільба " + gravetc3 + "; 4-стрільба " + gravetc4 + "; к-кінець. Якщо стрільба лежачи дописуєте 1, якщо стояче 2.")
    while vybir != "к":
        if vybir == "11":
            print("Стрільба лежачи "+gravetc1+":")
            strilba(n_tochnist11, n_shvydkosrilnist11)
            promahy1+=promahy
            if vsi_promahy1 != "":
                vsi_promahy1+=" + "+str(promahy)
            else:
                vsi_promahy1+=str(promahy)
        if vybir == "12":
            print("Стрільба стоячи "+gravetc1+":")
            strilba(n_tochnist12, n_shvydkosrilnist12)
            promahy1+=promahy
            if vsi_promahy1 != "":
                vsi_promahy1+=" + "+str(promahy)
            else:
                vsi_promahy1+=str(promahy)
        if vybir == "21":
            print("Стрільба лежачи "+gravetc2+":")
            strilba(n_tochnist21, n_shvydkosrilnist21)
            promahy2+=promahy
            if vsi_promahy2 != "":
                vsi_promahy2+=" + "+str(promahy)
            else:
                vsi_promahy2+=str(promahy)
        if vybir == "22":
            print("Стрільба стоячи "+gravetc2+":")
            strilba(n_tochnist22, n_shvydkosrilnist22)
            promahy2+=promahy
            if vsi_promahy2 != "":
                vsi_promahy2+=" + "+str(promahy)
            else:
                vsi_promahy2+=str(promahy)
        if vybir == "31":
            print("Стрільба лежачи "+gravetc3+":")
            strilba(n_tochnist31, n_shvydkosrilnist31)
            promahy3+=promahy
            if vsi_promahy3 != "":
                vsi_promahy3+=" + "+str(promahy)
            else:
                vsi_promahy3+=str(promahy)


        if vybir == "32":
            print("Стрільба стоячи "+gravetc3+":")
            strilba(n_tochnist32, n_shvydkosrilnist32)
            promahy3+=promahy
            if vsi_promahy3 != "":
                vsi_promahy3+=" + "+str(promahy)
            else:
                vsi_promahy3+=str(promahy)


        if vybir == "41":
            print("Стрільба лежачи "+gravetc4+":")
            strilba(n_tochnist41, n_shvydkosrilnist41)
            promahy4+=promahy
            if vsi_promahy4 != "":
                vsi_promahy4+=" + "+str(promahy)
            else:
                vsi_promahy4+=str(promahy)
        if vybir == "42":
            print("Стрільба стоячи "+gravetc4+":")
            strilba(n_tochnist42, n_shvydkosrilnist42)
            promahy4+=promahy
            if vsi_promahy4 != "":
                vsi_promahy4+=" + "+str(promahy)
            else:
                vsi_promahy4+=str(promahy)
        if vybir=="":
            hid(n_shvydkist1, gravetc1)
            hid(n_shvydkist2, gravetc2)
            hid(n_shvydkist3, gravetc3)
            hid(n_shvydkist4, gravetc4)           
        vybir = input("-хід; 1-стрільба " + gravetc1 + "; 2-стрільба " + gravetc2 + "; 3-стрільба " + gravetc3 + "; 4-стрільба " + gravetc4 + "; к-кінець. Якщо стрільба лежачи дописуєте 1, якщо стояче 2.")














# vybir = input("-хід; 1-стрільба червоного; 2-стрільба жовтого; 3-стрільба зеленого; к-кінець")
# while vybir != "к":
#     if vybir == "1":
#         strilba
#     if vybir == "2":
#         result12 = 0
#         for i in range(5):
#             a=randint(1, 100)
#             if a<=tochnist1:
#                 result12 += 1
#         result12 = 5-result12
#         result32 = 0
#         for i in range(45):
#             a=randint(1, 100)
#             b=0
#             c=randint(1,3)
#             if a>shvydkosrilnist2/1.5:
#                 result32 += 1
#             if a == 100:
#                 b=1
#                 if c == 1:
#                     result32 += 5
#                 if c == 2:
#                     result32 += 10
#                 if c == 3:
#                     result32 += 15
#         if result32<15:
#             result32 = 15
#         if result32>35 and result32 < 40 and b < 1:
#             result32 = result32 - randint(1,5)
#         if result32>40 and result32 < 45 and b < 1:
#             result32 = result32 - randint(1,5)
#         plus2=(30-result32)/2
#         plus2=math.ceil(plus2)
#         print("Швидкострільність - "+str(result32))
#         print("Плюс за щвидкість - "+str(plus2))
#         print("Кількість промахів - "+str(result12))







#    if vybir == "2":
#        result12 = 0
#        for i in range(5):
#            a=randint(1, 100)
#            if a<=tochnist2:
#                result12 += 1
#        print(result12)







    # if vybir == "3":
    #     result13 = 0
    #     for i in range(5):
    #         a=randint(1, 100)
    #         if a<=tochnist3:
    #             result13 += 1
    #     result13 = 5 - result13
    #     result33 = 0
    #     for i in range(45):
    #         a=randint(1, 100)
    #         b=0
    #         c = randint(1, 3)
    #         if a>shvydkosrilnist3/1.5:
    #             result33 += 1
    #         if a == 100:
    #             b=1
    #             if c ==1:
    #                 result33 += 5
    #             if c ==2:
    #                 result33 += 10
    #             if c ==3:
    #                 result33 += 15
    #     if result33<15:
    #         result33 = 15
    #     if result33>35 and result33 < 40 and b < 1:
    #         result33 = result33 - randint(1,5)
    #     if result33>40 and result33 < 45 and b < 1:
    #         result33 = result33 - randint(1,5)
    #     plus3=(30-result33)/2
    #     plus3 = math.ceil(plus3)
    #     print("Швидкострільність - "+str(result33))
    #     print("Плюс за щвидкість - "+str(plus3))
    #     print("Кількість промахів - "+str(result13))








    # if vybir == "":
    #     result21 = 0
    #     result22 = 0
    #     result23 = 0
    #     for i in range(10):
    #         a=randint(1, 100)
    #         if a<=shvydkist1:
    #             result21 += 1
    #     print("Червоний - " + str(result21))
    #     for i in range(10):
    #         a=randint(1, 100)
    #         if a<=shvydkist2:
    #             result22 += 1
    #     print("Жовтий - " + str(result22))
    #     for i in range(10):
    #         a=randint(1, 100)
    #         if a<=shvydkist3:
    #             result23 += 1
    #     print("Зелений - " + str(result23))
    # vybir = input("-хід; 1-стрільба червоного; 2-стрільба жовтого; 3-стрільба зеленого; k-кінець")











#End
print("Гонка завершилась.")
# print("Кількість неточних пострілів у компютерних гравців/гравця:")
# if kilkist=="1":
#     print("Перший гравець("+gravetc1+") допустив " + str(promahy1) + " хиб")
# if kilkist=="2":
#     print("Перший гравець("+gravetc1+") допустив " + str(promahy1) + " хиб")
#     print("Другий гравець("+gravetc2+") допустив " + str(promahy2) + " хиб")
# if kilkist=="3":
#     print("Перший гравець("+gravetc1+") допустив " + str(promahy1) + " хиб")
#     print("Другий гравець("+gravetc2+") допустив " + str(promahy2) + " хиб")
#     print("Третій гравець("+gravetc3+") допустив " + str(promahy3) + " хиб")
# if kilkist=="4":
    # print("Перший гравець("+gravetc1+") допустив " + str(promahy1) + " хиб")
    # print("Другий гравець("+gravetc2+") допустив " + str(promahy2) + " хиб")
    # print("Третій гравець("+gravetc3+") допустив " + str(promahy3) + " хиб")
    # print("Четвертий гравець("+gravetc4+") допустив " + str(promahy4) + " хиб")
print("Кількість промахів якиі допустив перший гравець("+gravetc1+"): " + vsi_promahy1 + " = " + str(promahy1))
print("Кількість промахів якиі допустив другий гравець("+gravetc2+"): " + vsi_promahy2 + " = " + str(promahy2))
print("Кількість промахів якиі допустив третій гравець("+gravetc3+"): " + vsi_promahy3 + " = " + str(promahy3))
print("Кількість промахів якиі допустив четвертий гравець("+gravetc4+"): " + vsi_promahy4 + " = " + str(promahy4))
# print("Другий гравець("+gravetc2+") допустив " + str(promahy2) + " хиб")
# print("Третій гравець("+gravetc3+") допустив " + str(promahy3) + " хиб")
# print("Четвертий гравець("+gravetc4+") допустив " + str(promahy4) + " хиб")