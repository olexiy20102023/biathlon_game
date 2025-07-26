from flask import *
from random import randint
import math
import time
from flask import session
app.secret_key = 'super_secret_key_123456'
from flask import make_response


app = Flask(__name__)
app.config["SECRET_KEY"] = "MySecretKey"


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response













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
prh=""
shtraf1=0
shtraf2=0
shtraf3=0
shtraf4=0
shtrafne_kolo=10
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
def hid(shvydkist, gravetc):
    global prh, shtraf1, shtraf2, shtraf3, shtraf4, sh_shvydkosrilnist1, sh_shvydkosrilnist2, sh_shvydkosrilnist3, sh_shvydkosrilnist4
    result_hid=0
    for i in range(10):
        a=randint(1, 100)
        if a<=shvydkist:
            result_hid += 1
    print(result_hid)


    if gravetc == name1:
        # print("yes")
        # print(sh_shvydkosrilnist1)
        if shtraf1==0:
            prh+="<br>"+gravetc + " - " + str(result_hid+sh_shvydkosrilnist1)

            
        else:
            shtraf1=shtraf1-result_hid-sh_shvydkosrilnist1
            if shtraf1<0:
                result_hid=abs(shtraf1)
                shtraf1=0
                sh_shvydkosrilnist1=0
                prh+="<br>"+gravetc + " - " + str(result_hid)
            else:
                prh+="<br>"+gravetc + " - на штрафному колі"
        sh_shvydkosrilnist1=0


    if gravetc == name2:
        # print(sh_shvydkosrilnist2)
        if shtraf2==0:
            prh+="<br>"+gravetc + " - " + str(result_hid+sh_shvydkosrilnist2)
        else:
            shtraf2=shtraf2-result_hid-sh_shvydkosrilnist2
            if shtraf2<0:
                result_hid=abs(shtraf2)
                shtraf2=0
                sh_shvydkosrilnist2=0
                prh+="<br>"+gravetc + " - " + str(result_hid)
            else:
                prh+="<br>"+gravetc + " - на штрафному колі"
        sh_shvydkosrilnist2=0


    if gravetc == name3:
        # print(sh_shvydkosrilnist3)
        if shtraf3==0:
            prh+="<br>"+gravetc + " - " + str(result_hid+sh_shvydkosrilnist3)
        else:
            shtraf3=shtraf3-result_hid-sh_shvydkosrilnist3
            if shtraf3<0:
                result_hid=abs(shtraf3)
                shtraf3=0
                sh_shvydkosrilnist3=0
                prh+="<br>"+gravetc + " - " + str(result_hid)
            else:
                prh+="<br>"+gravetc + " - на штрафному колі"
        sh_shvydkosrilnist3=0

    if gravetc == name4:
        # print(sh_shvydkosrilnist4)
        if shtraf4==0:
            prh+="<br>"+gravetc + " - " + str(result_hid+sh_shvydkosrilnist4)
        else:
            shtraf4=shtraf4-result_hid-sh_shvydkosrilnist4
            if shtraf4<0:
                result_hid=abs(shtraf4)
                shtraf4=0
                
                prh+="<br>"+gravetc + " - " + str(result_hid)
            else:
                prh+="<br>"+gravetc + " - на штрафному колі"
        sh_shvydkosrilnist4=0



















def strilba(tochnist, shvydkosrilnist):
    print(vybir)
    global prh, promahy, sh_promahy1, sh_promahy2, sh_promahy3, sh_promahy4, sh_shvydkosrilnist1, sh_shvydkosrilnist2, sh_shvydkosrilnist3, sh_shvydkosrilnist4
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
    prh+="<br>"+"Швидкострільність - "+str(result31)
    prh+="<br>"+"Плюс за щвидкість - "+str(plus1)
    prh+="<br>"+"Кількість промахів - "+str(result11)
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









def nasha_strilba(gravetc):
    global promahy, prh
    plus=(30-elapsed_time)/2
    plus=float(plus)
    plus=round(plus)
    prh+="Стрільба "+gravetc+":"
    prh+="<br>"+"Швидкострільність - "+str(elapsed_time)
    prh+="<br>"+"Плюс за щвидкість - "+str(plus)
    prh+="<br>"+"Кількість промахів - "+str(promahy)














def shtraf():
    global shtraf1, shtraf2, shtraf3, shtraf4, sh_promahy1, sh_promahy2, sh_promahy3, sh_promahy4

    if vybir=="11" or vybir=="12":
        shtraf1=0
        print("yes")
        shtraf1=shtrafne_kolo*sh_promahy1
        print(shtraf1)

    
    if vybir=="21" or vybir=="22":
        shtraf2=0
        shtraf2=shtrafne_kolo*sh_promahy2
        

    
    if vybir=="31" or vybir=="32":
        shtraf3=0
        shtraf3=shtrafne_kolo*sh_promahy3
        
        
    
    if vybir=="41" or vybir=="42":
        shtraf4=0
        shtraf4=shtrafne_kolo*sh_promahy4
        








def perevirka(gravetc, nomer1_4):
    global gravetc1, gravetc2, gravetc3, gravetc4, gravetc5, gravetc6, gravetc7, gravetc8, gravetc9, gravetc10, gravetc11, gravetc12
    global n_tochnist11, n_tochnist12, n_shvydkosrilnist11, n_shvydkist1, n_shvydkosrilnist12
    global n_tochnist21, n_tochnist22, n_shvydkosrilnist21, n_shvydkist2, n_shvydkosrilnist22
    global n_tochnist31, n_tochnist32, n_shvydkosrilnist31, n_shvydkist3, n_shvydkosrilnist32
    global n_tochnist41, n_tochnist42, n_shvydkosrilnist41, n_shvydkist4, n_shvydkosrilnist42
    global name1, name2, name3, name4
    if nomer1_4==1:
        if gravetc=="1":
            # str(name1)
            name1+=" (Червоний)"
            n_tochnist11=tochnist11
            n_tochnist12=tochnist12
            n_shvydkosrilnist11=shvydkosrilnist11
            n_shvydkosrilnist12=shvydkosrilnist12
            n_shvydkist1=shvydkist1
        if gravetc=="2":
            name1+=" (Червоний)"
            n_tochnist11=tochnist21
            n_tochnist12=tochnist22
            n_shvydkosrilnist11=shvydkosrilnist21
            n_shvydkosrilnist12=shvydkosrilnist22
            n_shvydkist1=shvydkist2
        if gravetc=="3":
            name1+=" (Червоний)"
            n_tochnist11=tochnist31
            n_tochnist12=tochnist32
            n_shvydkosrilnist11=shvydkosrilnist31
            n_shvydkosrilnist12=shvydkosrilnist32
            n_shvydkist1=shvydkist3
        if gravetc=="4":
            name1+=" (Червоний)"
            n_tochnist11=tochnist41
            n_tochnist12=tochnist42
            n_shvydkosrilnist11=shvydkosrilnist41
            n_shvydkosrilnist12=shvydkosrilnist42
            n_shvydkist1=shvydkist4
        if gravetc=="5":
            name1+=" (Червоний)"
            n_tochnist11=tochnist51
            n_tochnist12=tochnist52
            n_shvydkosrilnist11=shvydkosrilnist51
            n_shvydkosrilnist12=shvydkosrilnist52
            n_shvydkist1=shvydkist5
        if gravetc=="6":
            name1+=" (Червоний)"
            n_tochnist11=tochnist61
            n_tochnist12=tochnist62
            n_shvydkosrilnist11=shvydkosrilnist61
            n_shvydkosrilnist12=shvydkosrilnist62
            n_shvydkist1=shvydkist6
        if gravetc=="7":
            name1+=" (Червоний)"
            n_tochnist11=tochnist71
            n_tochnist12=tochnist72
            n_shvydkosrilnist11=shvydkosrilnist71
            n_shvydkosrilnist12=shvydkosrilnist72
            n_shvydkist1=shvydkist7
        if gravetc=="8":
            name1+=" (Червоний)"
            n_tochnist11=tochnist81
            n_tochnist12=tochnist82
            n_shvydkosrilnist11=shvydkosrilnist81
            n_shvydkosrilnist12=shvydkosrilnist82
            n_shvydkist1=shvydkist8
        if gravetc=="9":
            name1+=" (Червоний)"
            n_tochnist11=tochnist91
            n_tochnist12=tochnist92
            n_shvydkosrilnist11=shvydkosrilnist91
            n_shvydkosrilnist12=shvydkosrilnist92
            n_shvydkist1=shvydkist9
        if gravetc=="10":
            name1+=" (Червоний)"
            n_tochnist11=tochnist101
            n_tochnist12=tochnist102
            n_shvydkosrilnist11=shvydkosrilnist101
            n_shvydkosrilnist12=shvydkosrilnist102
            n_shvydkist1=shvydkist10
        if gravetc=="11":
            name1+=" (Червоний)"
            n_tochnist11=tochnist111
            n_tochnist12=tochnist112
            n_shvydkosrilnist11=shvydkosrilnist111
            n_shvydkosrilnist12=shvydkosrilnist112
            n_shvydkist1=shvydkist11
        if gravetc=="12":
            name1+=" (Червоний)"
            n_tochnist11=tochnist121
            n_tochnist12=tochnist122
            n_shvydkosrilnist12=shvydkosrilnist121
            n_shvydkosrilnist12=shvydkosrilnist122
            n_shvydkist1=shvydkist12




    if nomer1_4==2:
        if gravetc=="1":
            # str(name1)
            name2+=" (Жовтий)"
            n_tochnist21=tochnist11
            n_tochnist22=tochnist12
            n_shvydkosrilnist21=shvydkosrilnist11
            n_shvydkosrilnist22=shvydkosrilnist12
            n_shvydkist2=shvydkist1
        if gravetc=="2":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist21
            n_tochnist22=tochnist22
            n_shvydkosrilnist21=shvydkosrilnist21
            n_shvydkosrilnist22=shvydkosrilnist22
            n_shvydkist2=shvydkist2
        if gravetc=="3":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist31
            n_tochnist22=tochnist32
            n_shvydkosrilnist21=shvydkosrilnist31
            n_shvydkosrilnist22=shvydkosrilnist32
            n_shvydkist2=shvydkist3
        if gravetc=="4":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist41
            n_tochnist22=tochnist42
            n_shvydkosrilnist21=shvydkosrilnist41
            n_shvydkosrilnist22=shvydkosrilnist42
            n_shvydkist2=shvydkist4
        if gravetc=="5":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist51
            n_tochnist22=tochnist52
            n_shvydkosrilnist21=shvydkosrilnist51
            n_shvydkosrilnist22=shvydkosrilnist52
            n_shvydkist2=shvydkist5
        if gravetc=="6":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist61
            n_tochnist22=tochnist62
            n_shvydkosrilnist21=shvydkosrilnist61
            n_shvydkosrilnist22=shvydkosrilnist62
            n_shvydkist2=shvydkist6
        if gravetc=="7":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist71
            n_tochnist22=tochnist72
            n_shvydkosrilnist21=shvydkosrilnist71
            n_shvydkosrilnist22=shvydkosrilnist72
            n_shvydkist2=shvydkist7
        if gravetc=="8":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist81
            n_tochnist22=tochnist82
            n_shvydkosrilnist21=shvydkosrilnist81
            n_shvydkosrilnist22=shvydkosrilnist82
            n_shvydkist2=shvydkist8
        if gravetc=="9":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist91
            n_tochnist22=tochnist92
            n_shvydkosrilnist21=shvydkosrilnist91
            n_shvydkosrilnist22=shvydkosrilnist92
            n_shvydkist2=shvydkist9
        if gravetc=="10":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist101
            n_tochnist22=tochnist102
            n_shvydkosrilnist21=shvydkosrilnist101
            n_shvydkosrilnist22=shvydkosrilnist102
            n_shvydkist2=shvydkist10
        if gravetc=="11":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist111
            n_tochnist22=tochnist112
            n_shvydkosrilnist21=shvydkosrilnist111
            n_shvydkosrilnist22=shvydkosrilnist112
            n_shvydkist2=shvydkist11
        if gravetc=="12":
            name2+=" (Жовтий)"
            n_tochnist21=tochnist121
            n_tochnist22=tochnist122
            n_shvydkosrilnist22=shvydkosrilnist121
            n_shvydkosrilnist22=shvydkosrilnist122
            n_shvydkist2=shvydkist12

    if nomer1_4==3:
        if gravetc=="1":
            # str(name1)
            name3+=" (Зелений)"
            n_tochnist31=tochnist11
            n_tochnist32=tochnist12
            n_shvydkosrilnist31=shvydkosrilnist11
            n_shvydkosrilnist32=shvydkosrilnist12
            n_shvydkist3=shvydkist1
        if gravetc=="2":
            name3+=" (Зелений)"
            n_tochnist31=tochnist21
            n_tochnist32=tochnist22
            n_shvydkosrilnist31=shvydkosrilnist21
            n_shvydkosrilnist32=shvydkosrilnist22
            n_shvydkist3=shvydkist2
        if gravetc=="3":
            name3+=" (Зелений)"
            n_tochnist31=tochnist31
            n_tochnist32=tochnist32
            n_shvydkosrilnist31=shvydkosrilnist31
            n_shvydkosrilnist32=shvydkosrilnist32
            n_shvydkist3=shvydkist3
        if gravetc=="4":
            name3+=" (Зелений)"
            n_tochnist31=tochnist41
            n_tochnist32=tochnist42
            n_shvydkosrilnist31=shvydkosrilnist41
            n_shvydkosrilnist32=shvydkosrilnist42
            n_shvydkist3=shvydkist4
        if gravetc=="5":
            name3+=" (Зелений)"
            n_tochnist31=tochnist51
            n_tochnist32=tochnist52
            n_shvydkosrilnist31=shvydkosrilnist51
            n_shvydkosrilnist32=shvydkosrilnist52
            n_shvydkist3=shvydkist5
        if gravetc=="6":
            name3+=" (Зелений)"
            n_tochnist31=tochnist61
            n_tochnist32=tochnist62
            n_shvydkosrilnist31=shvydkosrilnist61
            n_shvydkosrilnist32=shvydkosrilnist62
            n_shvydkist3=shvydkist6
        if gravetc=="7":
            name3+=" (Зелений)"
            n_tochnist31=tochnist71
            n_tochnist32=tochnist72
            n_shvydkosrilnist31=shvydkosrilnist71
            n_shvydkosrilnist32=shvydkosrilnist72
            n_shvydkist3=shvydkist7
        if gravetc=="8":
            name3+=" (Зелений)"
            n_tochnist31=tochnist81
            n_tochnist32=tochnist82
            n_shvydkosrilnist31=shvydkosrilnist81
            n_shvydkosrilnist32=shvydkosrilnist82
            n_shvydkist3=shvydkist8
        if gravetc=="9":
            name3+=" (Зелений)"
            n_tochnist31=tochnist91
            n_tochnist32=tochnist92
            n_shvydkosrilnist31=shvydkosrilnist91
            n_shvydkosrilnist32=shvydkosrilnist92
            n_shvydkist3=shvydkist9
        if gravetc=="10":
            name3+=" (Зелений)"
            n_tochnist31=tochnist101
            n_tochnist32=tochnist102
            n_shvydkosrilnist31=shvydkosrilnist101
            n_shvydkosrilnist32=shvydkosrilnist102
            n_shvydkist3=shvydkist10
        if gravetc=="11":
            name3+=" (Зелений)"
            n_tochnist31=tochnist111
            n_tochnist32=tochnist112
            n_shvydkosrilnist31=shvydkosrilnist111
            n_shvydkosrilnist32=shvydkosrilnist112
            n_shvydkist3=shvydkist11
        if gravetc=="12":
            name3+=" (Зелений)"
            n_tochnist31=tochnist121
            n_tochnist32=tochnist122
            n_shvydkosrilnist32=shvydkosrilnist121
            n_shvydkosrilnist32=shvydkosrilnist122
            n_shvydkist3=shvydkist12



    if nomer1_4==4:
        if gravetc=="1":
            # str(name1)
            name4+=" (Синій)"
            n_tochnist41=tochnist11
            n_tochnist42=tochnist12
            n_shvydkosrilnist41=shvydkosrilnist11
            n_shvydkosrilnist42=shvydkosrilnist12
            n_shvydkist4=shvydkist1
        if gravetc=="2":
            name4+=" (Синій)"
            n_tochnist41=tochnist21
            n_tochnist42=tochnist22
            n_shvydkosrilnist41=shvydkosrilnist21
            n_shvydkosrilnist42=shvydkosrilnist22
            n_shvydkist4=shvydkist2
        if gravetc=="3":
            name4+=" (Синій)"
            n_tochnist41=tochnist31
            n_tochnist42=tochnist32
            n_shvydkosrilnist41=shvydkosrilnist31
            n_shvydkosrilnist42=shvydkosrilnist32
            n_shvydkist4=shvydkist3
        if gravetc=="4":
            name4+=" (Синій)"
            n_tochnist41=tochnist41
            n_tochnist42=tochnist42
            n_shvydkosrilnist41=shvydkosrilnist41
            n_shvydkosrilnist42=shvydkosrilnist42
            n_shvydkist4=shvydkist4
        if gravetc=="5":
            name4+=" (Синій)"
            n_tochnist41=tochnist51
            n_tochnist42=tochnist52
            n_shvydkosrilnist41=shvydkosrilnist51
            n_shvydkosrilnist42=shvydkosrilnist52
            n_shvydkist4=shvydkist5
        if gravetc=="6":
            name4+=" (Синій)"
            n_tochnist41=tochnist61
            n_tochnist42=tochnist62
            n_shvydkosrilnist41=shvydkosrilnist61
            n_shvydkosrilnist42=shvydkosrilnist62
            n_shvydkist4=shvydkist6
        if gravetc=="7":
            name4+=" (Синій)"
            n_tochnist41=tochnist71
            n_tochnist42=tochnist72
            n_shvydkosrilnist41=shvydkosrilnist71
            n_shvydkosrilnist42=shvydkosrilnist72
            n_shvydkist4=shvydkist7
        if gravetc=="8":
            name4+=" (Синій)"
            n_tochnist41=tochnist81
            n_tochnist42=tochnist82
            n_shvydkosrilnist41=shvydkosrilnist81
            n_shvydkosrilnist42=shvydkosrilnist82
            n_shvydkist4=shvydkist8
        if gravetc=="9":
            name4+=" (Синій)"
            n_tochnist41=tochnist91
            n_tochnist42=tochnist92
            n_shvydkosrilnist41=shvydkosrilnist91
            n_shvydkosrilnist42=shvydkosrilnist92
            n_shvydkist4=shvydkist9
        if gravetc=="10":
            name4+=" (Синій)"
            n_tochnist41=tochnist101
            n_tochnist42=tochnist102
            n_shvydkosrilnist41=shvydkosrilnist101
            n_shvydkosrilnist42=shvydkosrilnist102
            n_shvydkist4=shvydkist10
        if gravetc=="11":
            name4+=" (Синій)"
            n_tochnist41=tochnist111
            n_tochnist42=tochnist112
            n_shvydkosrilnist41=shvydkosrilnist111
            n_shvydkosrilnist42=shvydkosrilnist112
            n_shvydkist4=shvydkist11
        if gravetc=="12":
            name4+=" (Синій)"
            n_tochnist41=tochnist121
            n_tochnist42=tochnist122
            n_shvydkosrilnist42=shvydkosrilnist121
            n_shvydkosrilnist42=shvydkosrilnist122
            n_shvydkist4=shvydkist12
















#main

@app.route('/', methods=['GET', 'POST'])
# def home():
def home():
    return render_template('number_players.html')
    # твоя логіка
    # return render_template('index.html')
    # return "Головна сторінка працює!"
@app.route('/index', methods=['GET', 'POST'])
def index():
    # print("wkfofas")
    global num_players, prh, vsi_promahy1, vsi_promahy2, vsi_promahy3, vsi_promahy4, promahy1, promahy2 ,promahy3 ,promahy4
    prh = ""
    vsi_promahy1 = ""
    vsi_promahy2 = ""
    vsi_promahy3 = ""
    vsi_promahy4 = ""
    promahy1 = 0
    promahy2 = 0
    promahy3 = 0
    promahy4 = 0
    if request.method == "POST":
        num_players = request.form.get('players')
        # print(num_players)
        return redirect(f'/players/{num_players}')
    return render_template("number_players.html")


@app.route('/players/<num_players>', methods=['GET', 'POST'])
def players(num_players):
    global name1, name2, name3, name4, gravetc1, gravetc2, gravetc3, gravetc4
    name1 = name2 = name3 = name4 = ""
    if request.method == "POST":
        if num_players == "1":
            gravetc1 = request.form.get('gravetc1')
            name1 = request.form.get('login1')
            name2 = request.form.get('login2')
            name3 = request.form.get('login3')
            name4 = request.form.get('login4')
            perevirka(gravetc1, 1)
            # print(n_shvydkist1)
            # print(name1)
        if num_players == "2":
            gravetc1 = request.form.get('gravetc1')
            gravetc2 = request.form.get('gravetc2')
            name1 = request.form.get('login1')
            name2 = request.form.get('login2')
            name3 = request.form.get('login3')
            name4 = request.form.get('login4')
            perevirka(gravetc1, 1)
            perevirka(gravetc2, 2)
        if num_players == "3":
            gravetc1 = request.form.get('gravetc1')
            gravetc2 = request.form.get('gravetc2')
            gravetc3 = request.form.get('gravetc3')
            name1 = request.form.get('login1')
            name2 = request.form.get('login2')
            name3 = request.form.get('login3')
            name4 = request.form.get('login4')
            perevirka(gravetc1, 1)
            perevirka(gravetc2, 2)
            perevirka(gravetc3, 3)
        if num_players == "4":
            gravetc1 = request.form.get('gravetc1')
            gravetc2 = request.form.get('gravetc2')
            gravetc3 = request.form.get('gravetc3')
            gravetc4 = request.form.get('gravetc4')
            name1 = request.form.get('login1')
            name2 = request.form.get('login2')
            name3 = request.form.get('login3')
            name4 = request.form.get('login4')
            perevirka(gravetc1, 1)
            perevirka(gravetc2, 2)
            perevirka(gravetc3, 3)
            perevirka(gravetc4, 4)




        session['name1'] = name1
        session['name2'] = name2
        session['name3'] = name3
        session['name4'] = name4
        session['num_players'] = int(num_players)




        return render_template("menu.html",
                               name1=name1,
                               name2=name2,
                               name3=name3,
                               name4=name4,
                               num_players=int(num_players))
    return render_template('player_names.html', num_players=num_players)


# @app.route("/hid")
# def hid():
#     return render_template("hid.html")

# @app.route("/kinec")
# def kinec():
#     return render_template("kinec.html")

# @app.route("/str_st")
# def str_st():
#     return render_template("str_st.html")

# @app.route("/str_leg")
# def str_leg():
#     return render_template("str_leg.html")

# @app.route("/res_str_leg/<int:button_number>")
# def res_str_leg(button_number):
#     return render_template("str_leg_res.html", button_number=button_number)

# @app.route('/shooting/<code>')
# def shooting(code):
#     player_number = code[0]
#     shooting_type = 'лежка' if code[-1] == '1' else 'стійка'
#     return render_template('shooting.html', code=code,
#                            vybir=vybir)
# @app.route('/shooting/<code>')
# def shooting(code):
#     vybir = code  # ✅ створюємо змінну
#     player_number = code[0]
#     shooting_type = 'лежка' if code[-1] == '1' else 'стійка'
#     return render_template('shooting.html',
#                            code=code,
#                            vybir=vybir)

# @app.route("/result/<vybir>")
# def result(vybir):
#     return render_template("result.html", vybir=vybir)

# def result(code):
#     player_number = int(code[0])
#     middle_digit = code[1]
#     shooting_type = 'лежка' if code[-1] == '1' else 'стійка'

#     # логіка формування vybir
#     if middle_digit == '0':
#         new_player = player_number - 1
#         vybir = str(new_player) + middle_digit + code[2:]
#     else:
#         vybir = code

#     return render_template('result.html',
#                            code=code,
#                            vybir=vybir,
#                            player=player_number,
#                            shooting=shooting_type)


# Підтримка route з і без параметра code
# @app.route("/result/", defaults={"code": ""})
# @app.route("/result/<code>")
# def result(code):
#     if code == "к":
#         vybir = "к"
#         return render_template("result.html", vybir=vybir)

#     if code == "":
#         vybir = ""
#         return render_template("result.html", vybir=vybir)

#     player_number = int(code[0])
#     middle_digit = code[1]
#     shooting_type = 'лежка' if code[-1] == '1' else 'стійка'

    # логіка формування vybir
    # if middle_digit == '0':
    #     new_player = player_number - 1
    #     vybir = str(new_player) + middle_digit + code[2:]
    # else:
    #     vybir = code

    # return render_template("result.html",vybir=vybir)




@app.route("/result/", defaults={"code": ""})
@app.route("/result/<code>")
def result(code):
    global vybir, prh, vsi_promahy1, vsi_promahy2, vsi_promahy3, vsi_promahy4, promahy1, promahy2, promahy3, promahy4
    if code == "к":
        vybir = "к"
    elif code == "":
        vybir = ""
    else:
        vybir = code  # Просто передаємо code як vybir


    if vybir == "к":
        # prh+="Гонка завершилась."
        prh+="<br>"+"Кількість промахів якиі допустив перший гравець("+name1+"): " + vsi_promahy1 + " = " + str(promahy1)
        prh+="<br>"+"Кількість промахів якиі допустив другий гравець("+name2+"): " + vsi_promahy2 + " = " + str(promahy2)
        prh+="<br>"+"Кількість промахів якиі допустив третій гравець("+name3+"): " + vsi_promahy3 + " = " + str(promahy3)
        prh+="<br>"+"Кількість промахів якиі допустив четвертий гравець("+name4+"): " + vsi_promahy4 + " = " + str(promahy4)

    else:
        if num_players=="1":
            if vybir == "11":
                prh+="<br>"+"Стрільба лежачи "+name1+":"
                strilba(n_tochnist11, n_shvydkosrilnist11)
                promahy1+=promahy
                if vsi_promahy1 != "":
                    vsi_promahy1+=" + "+str(promahy)
                else:
                    vsi_promahy1+=str(promahy)
            if vybir == "12":
                prh+="<br>"+"Стрільба стоячи "+name1+":"
                strilba(n_tochnist12, n_shvydkosrilnist12)
                promahy1+=promahy
                if vsi_promahy1 != "":
                    vsi_promahy1+=" + "+str(promahy)
                else:
                    vsi_promahy1+=str(promahy)
            # if vybir == "101":
            #     nasha_strilba(gravetc2)
            #     promahy2+=promahy
            #     if vsi_promahy2 != "":
            #         vsi_promahy2+=" + "+str(promahy)
            #     else:
            #         vsi_promahy2+=str(promahy)
            # if vybir == "102":
            #     nasha_strilba(gravetc3)
            #     promahy3+=promahy
            #     if vsi_promahy3 != "":
            #         vsi_promahy3+=" + "+str(promahy)
            #     else:
            #         vsi_promahy3+=str(promahy)
            # if vybir == "103":
            #     nasha_strilba(gravetc4)
            #     promahy4+=promahy
            #     if vsi_promahy4 != "":
            #         vsi_promahy4+=" + "+str(promahy)
            #     else:
            #         vsi_promahy4+=str(promahy)
            if vybir=="":
                hid(n_shvydkist1, name1)








        if num_players=="2":
            if vybir == "11":
                prh+="<br>"+"Стрільба лежачи "+name1+":"
                strilba(n_tochnist11, n_shvydkosrilnist11)
                promahy1+=promahy
                if vsi_promahy1 != "":
                    vsi_promahy1+=" + "+str(promahy)
                else:
                    vsi_promahy1+=str(promahy)
            if vybir == "12":
                prh+="<br>"+"Стрільба стоячи "+name1+":"
                strilba(n_tochnist12, n_shvydkosrilnist12)
                promahy1+=promahy
                if vsi_promahy1 != "":
                    vsi_promahy1+=" + "+str(promahy)
                else:
                    vsi_promahy1+=str(promahy)
            if vybir == "21":
                prh+="<br>"+"Стрільба лежачи "+name2+":"
                strilba(n_tochnist21, n_shvydkosrilnist21)
                promahy2+=promahy
                if vsi_promahy2 != "":
                    vsi_promahy2+=" + "+str(promahy)
                else:
                    vsi_promahy2+=str(promahy)
            if vybir == "22":
                prh+="<br>"+"Стрільба стоячи "+name2+":"
                strilba(n_tochnist22, n_shvydkosrilnist22)
                promahy2+=promahy
                if vsi_promahy2 != "":
                    vsi_promahy2+=" + "+str(promahy)
                else:
                    vsi_promahy2+=str(promahy)
            # if vybir == "101":
            #     nasha_strilba(gravetc3)
            #     promahy3+=promahy
            #     if vsi_promahy3 != "":
            #         vsi_promahy3+=" + "+str(promahy)
            #     else:
            #         vsi_promahy3+=str(promahy)
            # if vybir == "102":
            #     nasha_strilba(gravetc4)
            #     promahy4+=promahy
            #     if vsi_promahy4 != "":
            #         vsi_promahy4+=" + "+str(promahy)
            #     else:
            #         vsi_promahy4+=str(promahy)
            if vybir=="":
                hid(n_shvydkist1, name1)
                hid(n_shvydkist2, name2)


        if num_players=="3":
            if vybir == "11":
                prh+="<br>"+"Стрільба лежачи "+name1+":"
                strilba(n_tochnist11, n_shvydkosrilnist11)
                promahy1+=promahy
                if vsi_promahy1 != "":
                    vsi_promahy1+=" + "+str(promahy)
                else:
                    vsi_promahy1+=str(promahy)
            if vybir == "12":
                prh+="<br>"+"Стрільба стоячи "+name1+":"
                strilba(n_tochnist12, n_shvydkosrilnist12)
                promahy1+=promahy
                if vsi_promahy1 != "":
                    vsi_promahy1+=" + "+str(promahy)
                else:
                    vsi_promahy1+=str(promahy)
            if vybir == "21":
                prh+="<br>"+"Стрільба лежачи "+name2+":"
                strilba(n_tochnist21, n_shvydkosrilnist21)
                promahy2+=promahy
                if vsi_promahy2 != "":
                    vsi_promahy2+=" + "+str(promahy)
                else:
                    vsi_promahy2+=str(promahy)
            if vybir == "22":
                prh+="<br>"+"Стрільба стоячи "+name2+":"
                strilba(n_tochnist22, n_shvydkosrilnist22)
                promahy2+=promahy
                if vsi_promahy2 != "":
                    vsi_promahy2+=" + "+str(promahy)
                else:
                    vsi_promahy2+=str(promahy)
            if vybir == "31":
                prh+="<br>"+"Стрільба лежачи "+name3+":"
                strilba(n_tochnist31, n_shvydkosrilnist31)
                promahy3+=promahy
                if vsi_promahy3 != "":
                    vsi_promahy3+=" + "+str(promahy)
                else:
                    vsi_promahy3+=str(promahy)
            if vybir == "32":
                prh+="<br>"+"Стрільба стоячи "+name3+":"
                strilba(n_tochnist32, n_shvydkosrilnist32)
                promahy3+=promahy
                if vsi_promahy3 != "":
                    vsi_promahy3+=" + "+str(promahy)
                else:
                    vsi_promahy3+=str(promahy)
            # if vybir == "101":
            #     nasha_strilba(gravetc4)
            #     promahy4+=promahy
            #     if vsi_promahy4 != "":
            #         vsi_promahy4+=" + "+str(promahy)
            #     else:
            #         vsi_promahy4+=str(promahy)
            if vybir=="":
                hid(n_shvydkist1, name1)
                hid(n_shvydkist2, name2)
                hid(n_shvydkist3, name3)



        if num_players=="4":
            if vybir == "11":
                prh+="<br>"+"Стрільба лежачи "+name1+":"
                strilba(n_tochnist11, n_shvydkosrilnist11)
                promahy1+=promahy
                if vsi_promahy1 != "":
                    vsi_promahy1+=" + "+str(promahy)
                else:
                    vsi_promahy1+=str(promahy)
            if vybir == "12":
                prh+="<br>"+"Стрільба стоячи "+name1+":"
                strilba(n_tochnist12, n_shvydkosrilnist12)
                promahy1+=promahy
                if vsi_promahy1 != "":
                    vsi_promahy1+=" + "+str(promahy)
                else:
                    vsi_promahy1+=str(promahy)
            if vybir == "21":
                prh+="<br>"+"Стрільба лежачи "+name2+":"
                strilba(n_tochnist21, n_shvydkosrilnist21)
                promahy2+=promahy
                if vsi_promahy2 != "":
                    vsi_promahy2+=" + "+str(promahy)
                else:
                    vsi_promahy2+=str(promahy)
            if vybir == "22":
                prh+="<br>"+"Стрільба стоячи "+name2+":"
                strilba(n_tochnist22, n_shvydkosrilnist22)
                promahy2+=promahy
                if vsi_promahy2 != "":
                    vsi_promahy2+=" + "+str(promahy)
                else:
                    vsi_promahy2+=str(promahy)
            if vybir == "31":
                prh+="<br>"+"Стрільба лежачи "+name3+":"
                strilba(n_tochnist31, n_shvydkosrilnist31)
                promahy3+=promahy
                if vsi_promahy3 != "":
                    vsi_promahy3+=" + "+str(promahy)
                else:
                    vsi_promahy3+=str(promahy)


            if vybir == "32":
                prh+="<br>"+"Стрільба стоячи "+name3+":"
                strilba(n_tochnist32, n_shvydkosrilnist32)
                promahy3+=promahy
                if vsi_promahy3 != "":
                    vsi_promahy3+=" + "+str(promahy)
                else:
                    vsi_promahy3+=str(promahy)


            if vybir == "41":
                prh+="<br>"+"Стрільба лежачи "+name4+":"
                strilba(n_tochnist41, n_shvydkosrilnist41)
                promahy4+=promahy
                if vsi_promahy4 != "":
                    vsi_promahy4+=" + "+str(promahy)
                else:
                    vsi_promahy4+=str(promahy)
            if vybir == "42":
                prh+="<br>"+"Стрільба стоячи "+name4+":"
                strilba(n_tochnist42, n_shvydkosrilnist42)
                promahy4+=promahy
                if vsi_promahy4 != "":
                    vsi_promahy4+=" + "+str(promahy)
                else:
                    vsi_promahy4+=str(promahy)
            if vybir=="":
                hid(n_shvydkist1, name1)
                hid(n_shvydkist2, name2)
                hid(n_shvydkist3, name3)
                hid(n_shvydkist4, name4)           
    print(prh)


    # return_to = request.referrer or "/"
    return render_template("result.html", vybir=vybir, prh=prh)

# @app.route("/menu")
# def menu():
#     global prh
#     prh = ""  # очищуємо змінну prh при заході в меню
#     # Тут можна передати потрібні змінні, якщо треба
#     return render_template("menu.html")


# @app.route("/clear", methods=["POST"])
# def clear():
#     global prh
#     prh = ""
#     return_to = request.form.get("return_to", "/")  # звідки повернутись
#     return redirect(return_to)
# @app.route("/clear", methods=["POST"])
# def clear():
#     global prh
#     prh = ""  # Очищаємо змінну
    # if num_players=="1":
    #     return redirect("/players/1")
      # або повернення до потрібної сторінки

@app.route('/menu')
def menu():
    global prh
    prh = ""  # або prh = None
    return render_template('menu.html', num_players=session.get('num_players'), 
                           name1=session.get('name1'), 
                           name2=session.get('name2'),
                           name3=session.get('name3'),
                           name4=session.get('name4'))





# @app.route("/save_time", methods=["POST"])
# def save_time():
#     global elapsed_time
#     data = request.get_json()
#     elapsed_time = data.get("elapsed_time", 0)
#     print("Отриманий час:", elapsed_time)
#     return jsonify({"status": "ok", "elapsed_time": elapsed_time})


elapsed_time = 0.0  # тип float

# @app.route("/save_time", methods=["POST"])
# def save_time():
#     global elapsed_time
#     data = request.get_json()
#     elapsed_time = float(data.get("elapsed_time", 0.0))
#     print("Отриманий час:", elapsed_time, "сек (з сотими)")
#     return jsonify({"status": "ok", "elapsed_time": elapsed_time})

@app.route("/save_time", methods=["POST"])
def save_time():
    global elapsed_time
    data = request.get_json()
    
    original = float(data.get("elapsed_time", 0.0))
    rounded = round(original)

    print("Неокруглений час:", original, "секунд")
    print("Округлений час:", rounded, "секунд")

    elapsed_time = rounded
    return jsonify({"status": "ok", "rounded_elapsed_time": elapsed_time})






@app.route("/get_elapsed_time", methods=["GET"])
def get_elapsed_time():
    return jsonify({"elapsed_time": elapsed_time})





@app.route("/save_button", methods=["POST"])
def save_button():
    global promahy, promahy2, promahy3, promahy4, vsi_promahy1, vsi_promahy2, vsi_promahy3, vsi_promahy4
    data = request.get_json()
    button_number = data.get("button")

    if button_number is not None:
        promahy = int(button_number)
        print(f"Натиснута кнопка: {promahy}")  # вивід у термінал
        print(num_players)





        if num_players=="1":
            print(vybir)
            if vybir == "101" or vybir == "102":
                nasha_strilba(name2)
                print(prh)
                promahy2+=promahy
                if vsi_promahy2 != "":
                    vsi_promahy2+=" + "+str(promahy)
                else:
                    vsi_promahy2+=str(promahy)
            if vybir == "201" or vybir == "202":
                print(prh)
                nasha_strilba(name3)
                promahy3+=promahy
                if vsi_promahy3 != "":
                    vsi_promahy3+=" + "+str(promahy)
                else:
                    vsi_promahy3+=str(promahy)
            if vybir == "301" or vybir == "302":
                nasha_strilba(name4)
                print(prh)
                promahy4+=promahy
                if vsi_promahy4 != "":
                    vsi_promahy4+=" + "+str(promahy)
                else:
                    vsi_promahy4+=str(promahy)



        if num_players=="2":
        
            if vybir == "101" or vybir == "102":
                nasha_strilba(name3)
                print(prh)
                promahy3+=promahy
                if vsi_promahy3 != "":
                    vsi_promahy3+=" + "+str(promahy)
                else:
                    vsi_promahy3+=str(promahy)
            if vybir == "201" or vybir == "202":
                nasha_strilba(name4)
                print(prh)
                promahy4+=promahy
                if vsi_promahy4 != "":
                    vsi_promahy4+=" + "+str(promahy)
                else:
                    vsi_promahy4+=str(promahy)



        if num_players=="3":
            print(vybir)
            if vybir == "101" or vybir == "102":
                nasha_strilba(name4)
                print(prh)
                promahy4+=promahy
                if vsi_promahy4 != "":
                    vsi_promahy4+=" + "+str(promahy)
                else:
                    vsi_promahy4+=str(promahy)


    return jsonify({
        "status": "ok",
        "prh": prh  # повертаємо prh у відповідь
    })











if __name__ == "__main__":
    app.run(debug=True)
