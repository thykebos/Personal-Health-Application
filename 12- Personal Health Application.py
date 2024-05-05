import tkinter as tk
from tkinter import ttk
from ttkthemes import *
from tkmacosx import *
from PIL import Image, ImageTk
import json
import random


root = tk.Tk()
root.geometry('1400x700')
root.title('Health Analyst')
def kisi_bilgi():
    global kullanici_vki
    kullanici_ad=ad.get().strip().title()
    kullanici_yas=float(yas.get())
    kullanici_kan=kan
    kullanici_boy=float(boy.get())
    kullanici_kilo=float(kilo.get())
    kullanici_vki=(kullanici_kilo/(kullanici_boy*kullanici_boy))


    if not kullanici_ad or not kullanici_kan:     
        vki_yazi.config(text='Tüm Kısımların Girilmesi\nZorunludur') , 
        vki_yazi.place(x=50)
    elif ad and yas and kan and boy and kilo:

        vki_yazi.place(x=80,y=530)
        if kullanici_vki < 0.00185 :
            vki_yazi.config(text=f'Vücut Kitle Endeksiniz\n {kullanici_vki:,.5f} ideal kilo altı')
        if 0.00249 > kullanici_vki > 0.00185 :
            vki_yazi.config(text=f'Vücut Kitle Endeksiniz\n {kullanici_vki:,.5f} ideal kilo')
        if 0.00299 > kullanici_vki > 0.0025 :
            vki_yazi.config(text=f'Vücut Kitle Endeksiniz\n {kullanici_vki:,.5f} ideal kilo üstü')
        if 0.00399 > kullanici_vki > 0.0030 :
            vki_yazi.config(text=f'Vücut Kitle Endeksiniz\n {kullanici_vki:,.5f} obez')
        if kullanici_vki > 0.0040 :
            vki_yazi.config(text=f'Vücut Kitle Endeksiniz\n {kullanici_vki:,.5f} morbid obez')
        
        list2=[ad,yas,boy,kilo,kaydet_buton]
        for i in list2:
            i.config(state='disabled')

    kisi_bilgileri= {
        "ad": kullanici_ad,
        "yas": kullanici_yas,
        "kan": kullanici_kan,
        "boy": kullanici_boy,
        "kilo": kullanici_kilo,
        "vki": kullanici_vki      
    }
    veri_tabani= json.dumps(kisi_bilgileri,ensure_ascii=False,indent=12)
    with open("kullanici_veri.json","a", encoding='utf-8') as file:
        file.write('\n'+veri_tabani+'\n')
kan=[]
def kan_grubu():
    liste=[aarti,aeksi,barti,beksi,abarti,abeksi,sifirarti,sifireksi]
    if a_arti.get():
        kan.append("A+")
        for i in liste:
            i.config(state='disabled')
            pass
    if a_eksi.get():
        kan.append("A-")
        for i in liste:
            i.config(state='disabled')
            pass
    if b_arti.get():
        kan.append("B+")
        for i in liste:
            i.config(state='disabled')
            pass
    if b_eksi.get():
        kan.append("B-")
        for i in liste:
            i.config(state='disabled')
            pass
    if ab_arti.get():
        kan.append("AB+")
        for i in liste:
            i.config(state='disabled')
            pass
    if ab_eksi.get():
        kan.append("AB-")
        for i in liste:
            i.config(state='disabled')
            pass
    if sifir_arti.get():
        kan.append("0+")
        for i in liste:
            i.config(state='disabled')
            pass
    if sifir_eksi.get():
        kan.append("0-")
        for i in liste:
            i.config(state='disabled')
            pass
            

style = ThemedStyle(root)
style.theme_use('yaru')

canvas = tk.Canvas(root, width=1400, height=700)     #ekrandaki kare oluşturdum ve tema gibi gözükmesini sağladım
canvas.place(x=-25,y=-25)
canvas.create_rectangle(1400, 50, 50, 700, outline="black", width=2,fill='#63BDB7')

def fitness():  
    randevu_alan = ttk.Label(root, text=f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ", background='#63BDB7', font=('Times New Roman', 14), width=105)
    randevu_alan.place(x=390, y=255)
    
    if kullanici_vki < 0.00185:
        zayif_adam = Image.open('5.png')
        resim_boyut2 = zayif_adam.resize((150, 250))
        zayif_adam = ImageTk.PhotoImage(resim_boyut2)
        zayif_label = tk.Label(root, image=zayif_adam, bg='#63BDB7')
        zayif_label.image = zayif_adam  # Resim nesnesine referansı tutun
        zayif_label.place(x=400, y=280)

        yazi1=('(kiloya göre)Haftada 3-4 Gün Widerstand Antrenmanı:\n\nSquat: 3 set x 12 tekrar\n'
               'Lunges: 3 set x 12 tekrar (her bacak için)\n'
               'Dumbbell Bench Press: 3 set x 12 tekrar\n'
               'Bent Over Rows: 3 set x 12 tekrar\nShoulder Press: 3 set x 12 tekrar\nPlank: 3 set x 30 saniye')
        zayif_yazi= ttk.Label(root,text=yazi1,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi.place(x=580,y=280)

        yazi11=('Bir Günlük Beslenme Planı:\n\n(sabah) Yulaf ezmesi üzerine dilimlenmiş muz ve bir avuç ceviz içi\n'
               '1 bardak yarım yağlı süt veya badem sütü\n'
               '(ara öğün) 1 adet orta boy elma veya bir avuç badem\n'
               '(öğle) Izgara tavuk göğsü salata (marul, domates, salatalık ile)\n(ara öğün)1 su bardağı yoğurt veya 1 küçük kutu light yoğurt\n'
               '(akşam) Izgara balık -somon veya alabalık- sebzeli bulgur pilavı')
        zayif_yazi1= ttk.Label(root,text=yazi11,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi1.place(x=580,y=480)

    if 0.00249 > kullanici_vki > 0.00185:
        normal_adam = Image.open('4.png')
        resim_boyut3 = normal_adam.resize((150, 250))
        normal_adam = ImageTk.PhotoImage(resim_boyut3)
        normal_label = tk.Label(root, image=normal_adam, bg='#63BDB7')
        normal_label.image = normal_adam      
        normal_label.place(x=400, y=280)

        yazi2=('(kiloya göre)Haftada 3-4 Gün Widerstand Antrenmanı:\n\nSquat: 3 set x 12 tekrar\n'
               'Push-up: 3 set x 12 tekrar (her bacak için)\n'
               'Dumbbell Bench Press: 3 set x 12 tekrar\n'
               'Bent Over Rows: 3 set x 12 tekrar\nShoulder Press: 3 set x 12 tekrar\nDeadlift: 3 set x 30 saniye')
        zayif_yazi2= ttk.Label(root,text=yazi2,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi2.place(x=580,y=280)

        yazi22=('Bir Günlük Beslenme Planı:\n\n(sabah) Yulaf ezmesi, meyve ve ceviz içeren bir kase.\n'
               'Bir dilim kepekli ekmek üzerine peynir ve domates.\n'
               '(ara öğün) Yoğurt veya meyve.\n'
               '(öğle) Izgara tavuk göğsü, esmer pirinç ve sebzelerden oluşan bir tabak.\nSalata (zeytinyağı ve limon sosuyla)\n'
               '(akşam) Balık, kızarmış veya fırınlanmış sebzeler ve bulgur pilavı.')
        zayif_yazi22= ttk.Label(root,text=yazi22,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi22.place(x=580,y=480)

    if 0.00299 > kullanici_vki > 0.0025:
        kilolu_adam = Image.open('3.png')
        resim_boyut4 = kilolu_adam.resize((150, 250))
        kilolu_adam = ImageTk.PhotoImage(resim_boyut4)
        kilolu_label = tk.Label(root, image=kilolu_adam, bg='#63BDB7')
        kilolu_label.image = kilolu_adam      
        kilolu_label.place(x=400, y=280)

        yazi3=('(kiloya göre)Haftada 3-4 Gün Widerstand Antrenmanı:\n\nSquat: 3 set x 12 tekrar\n'
               'Lunge: 3 set x 12 tekrar (her bacak için)\n'
               'Dumbbell Bench Press: 3 set x 12 tekrar\n'
               'Bent Over Rows: 3 set x 12 tekrar\nKardiyo: 20 Dakika')
        zayif_yazi3= ttk.Label(root,text=yazi3,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi3.place(x=580,y=280)

        yazi33=('Bir Günlük Beslenme Planı:\n\n(sabah) Yulaf ezmesi, süt veya yoğurt ile.\n'
               'Bir dilim kepekli ekmek üzerine az yağlı peynir veya yumurta.\n'
               '(ara öğün) Bir avuç kadar badem veya ceviz.\n'
               '(öğle) Izgara tavuk veya balık.\nBol yeşillikli salata (az yağlı sosla) ve az miktarda esmer pirinç veya bulgur pilavı.\n'
               '(akşam) Sebzelerle hazırlanmış bir çorba veya sebze yemeği.')
        zayif_yazi33= ttk.Label(root,text=yazi33,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi33.place(x=580,y=480)
    if 0.00399 > kullanici_vki > 0.0030:
        obez_adam = Image.open('2.png')
        resim_boyut5 = obez_adam.resize((150, 250))
        obez_adam = ImageTk.PhotoImage(resim_boyut5)
        obez_label = tk.Label(root, image=obez_adam, bg='#63BDB7')
        obez_label.image = obez_adam      
        obez_label.place(x=400, y=280)

        yazi4=('(kiloya göre)Haftada 3-4 Gün Widerstand Antrenmanı:\n\nDuvara Dayalı Squat: 3 set, 8-10 tekrar.\n'
               'Diz Üstü Push-up: 3 set, 8-10 tekrar.\n'
               'Duvara Dayalı Lunges: Her bacak için 3 set, 8-10 tekrar.\n'
               'Plank (Mekik): 3 set, 20-30 saniye.\nKardiyo: 25 Dakika')
        zayif_yazi4= ttk.Label(root,text=yazi4,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi4.place(x=580,y=280)

        yazi44=('Bir Günlük Beslenme Planı:\n\n(sabah) Yulaf ezmesi, süt veya yoğurt ile.\n'
               'Bir dilim kepekli ekmek üzerine az yağlı peynir veya yumurta.\n'
               '(ara öğün) Bir avuç kadar badem veya ceviz.\n'
               '(öğle) Izgara tavuk veya balık.\nBol yeşillikli salata (az yağlı sosla) ve az miktarda esmer pirinç veya bulgur pilavı.\n'
               '(akşam) Sebzelerle hazırlanmış bir çorba veya sebze yemeği.')
        zayif_yazi44= ttk.Label(root,text=yazi44,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi44.place(x=580,y=480)
    if kullanici_vki > 0.0040:
        orbid_adam = Image.open('1.png')
        resim_boyut6 = orbid_adam.resize((150, 250))
        orbid_adam = ImageTk.PhotoImage(resim_boyut6)
        orbid_label = tk.Label(root, image=orbid_adam, bg='#63BDB7')
        orbid_label.image = orbid_adam      
        orbid_label.place(x=400, y=280)

        yazi5=('(kiloya göre)Haftada 3-4 Gün Widerstand Antrenmanı:\n\nDuvara Dayalı Squat: 3 set, 8-10 tekrar.\n'
               'Diz Üstü Push-up: 3 set, 8-10 tekrar.\n'
               'Duvara Dayalı Lunges: Her bacak için 3 set, 8-10 tekrar.\n'
               'Sandalye Üzerinde Oturarak Kalkma (Chair Stand): 2 set, 6-8 tekrar.\nKardiyo: 30 Dakika')
        zayif_yazi5= ttk.Label(root,text=yazi5,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi5.place(x=580,y=280)

        yazi55=('Bir Günlük Beslenme Planı:\n\n(sabah) Yulaf ezmesi, süt veya yoğurt\n'
               ' Bir dilim kepekli ekmek üzerine az yağlı peynir veya yumurta.\n'
               '(ara öğün)  Biraz meyve veya yoğurt.\n'
               '(öğle) Bol yeşillikli salata (az yağlı sosla)\n'
               '(akşam) Sebzelerle hazırlanmış bir çorba veya sebze yemeği.')
        zayif_yazi55= ttk.Label(root,text=yazi55,background='#63BDB7',font=('Times New Roman',14))
        zayif_yazi55.place(x=580,y=480)

    else:
        print("KULLANICI HATASI:")

def randevu_al():
    randevu_alan = ttk.Label(root, text=f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ", background='#63BDB7', font=('Times New Roman', 14), width=105)
    randevu_alan.place(x=390, y=255)

    secilen_hastane = tk.StringVar()
    hastaneler = ['HASTANE SEÇİNİZ','IBIS HASTANE', 'PROGRAMCILIK HASTANE']
    hastane_secenek = ttk.OptionMenu(root,secilen_hastane, hastaneler[0], *hastaneler)
    hastane_secenek.place(x=450,y=270)

    secilen_bolum = tk.StringVar()
    bolumler = ['BÖLÜM SEÇİNİZ','KULAK-BURUN-BOĞAZ', 'ENDOSKOPİ', 'DİĞER']
    bolum_secenek = ttk.OptionMenu(root,secilen_bolum, bolumler[0], *bolumler)
    bolum_secenek.place(x=650,y=270)

    secilen_doktor = tk.StringVar()
    doktorlar = ['DOKTOR SEÇİNİZ','ÇAĞRI İBİŞ', 'FERİDUN KUNAK']
    doktor_secenek = ttk.OptionMenu(root,secilen_doktor, doktorlar[0], *doktorlar)
    doktor_secenek.place(x=850,y=270)

    def randevu_kaydet():
        if ad.get():
                if secilen_hastane.get() != hastaneler[0] and secilen_bolum.get() != bolumler[0] and secilen_doktor.get() != doktorlar[0]:               
                    randevu_buton.config(text=' \n\n\nRANDEVU ALINDI \n\n\n\n ',state='disabled')
                    kontrol_buton.config(state='disabled')
                    hastane_secenek.config(state='disabled')               
                    bolum_secenek.config(state='disabled')               
                    doktor_secenek.config(state='disabled')
                    
                    saatler=['10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00']
                    saatler_yazi=(f'Muayene Saatiniz: \n {random.choice(saatler)}\nDoktorunuz: \n {secilen_doktor.get()}')
                    rapor_yazi= ttk.Label(root,text=saatler_yazi,background='#63BDB7',font=('Times New Roman',14))
                    rapor_yazi.place(x=1050,y=70)
        else:
            print("KULLANICI HATASI: doldurulmamış kısımlar var")

    kontrol_buton = ttk.Button(root, text=" Tamam", command=randevu_kaydet,width=17)
    kontrol_buton.place(x=670,y=340)

ad = tk.Entry(root,width=15, font=('Times New Roman',12),relief='groove',state='normal')
ad.place(x=100,y=215)
yas = tk.Entry(root,width=10, font=('Times New Roman',12),relief='groove',state='normal')
yas.place(x=50,y=300)
boy = tk.Entry(root,width=10, font=('Times New Roman',12),relief='groove',state='normal')
boy.place(x=50,y=420)
kilo = tk.Entry(root,width=10, font=('Times New Roman',12),relief='groove',state='normal')
kilo.place(x=185,y=420)
vki_yazi= ttk.Label(root,text='Vücut Kitle Endeksiniz\n',background='#63BDB7',font=('Times New Roman',14))
vki_yazi.place(x=80,y=530)
ad_yazi= ttk.Label(root,text='    Ad Soyad',background='#63BDB7',font=('Times New Roman',14))
ad_yazi.place(x=100,y=187)
yas_yazi= ttk.Label(root,text='    Yaş',background='#63BDB7',font=('Times New Roman',14))
yas_yazi.place(x=50,y=270)
boy_yazi= ttk.Label(root,text='  Boy (cm)',background='#63BDB7',font=('Times New Roman',14))
boy_yazi.place(x=50,y=390)
kilo_yazi= ttk.Label(root,text='    Kilo',background='#63BDB7',font=('Times New Roman',14))
kilo_yazi.place(x=185,y=390)
kaydet_buton= ttk.Button(root,text=' KAYDET ',command=kisi_bilgi)
kaydet_buton.place(x=110,y=600)
fitness_buton = ttk.Button(root,text=f' \n\n\nFITNESS PROGRAM \n\n\n\n ',width=35,command=fitness)
fitness_buton.place(x=390,y=50)
randevu_buton = ttk.Button(root,text=f' \n\n\nRANDEVU AL \n\n\n\n ',width=35,command=randevu_al)
randevu_buton.place(x=740,y=50)
#########################################
a_arti= tk.BooleanVar()
a_eksi= tk.BooleanVar()
b_arti= tk.BooleanVar()
b_eksi= tk.BooleanVar()
ab_arti= tk.BooleanVar()
ab_eksi= tk.BooleanVar()
sifir_arti= tk.BooleanVar()
sifir_eksi= tk.BooleanVar()

aarti = ttk.Checkbutton(root, text=" A+  ", variable=a_arti,command=kan_grubu, )
aarti.place(x=170,y=265)
aeksi = ttk.Checkbutton(root, text=" A-  ", variable=a_eksi,command=kan_grubu )
aeksi.place(x=210,y=265)
barti = ttk.Checkbutton(root, text=" B+  ", variable=b_arti,command=kan_grubu )
barti.place(x=170,y=285)
beksi = ttk.Checkbutton(root, text=" B-  ", variable=b_eksi,command=kan_grubu )
beksi.place(x=210,y=285)
abarti = ttk.Checkbutton(root, text=" AB+  ", variable=ab_arti,command=kan_grubu )
abarti.place(x=170,y=305)
abeksi = ttk.Checkbutton(root, text=" AB-  ", variable=ab_eksi,command=kan_grubu )
abeksi.place(x=210,y=305)
sifirarti = ttk.Checkbutton(root, text=" 0+  ", variable=sifir_arti,command=kan_grubu )
sifirarti.place(x=170,y=325)
sifireksi = ttk.Checkbutton(root, text=" 0-  ", variable=sifir_eksi,command=kan_grubu )
sifireksi.place(x=210,y=325)
#########################################

resim = Image.open('health2.png')  #PIL kütüphanesi kullanarak panele resim ekledik
resim_boyut= resim.resize((120,120))
resim = ImageTk.PhotoImage(resim_boyut)
resim_label = tk.Label(root, image=resim,bg='#63BDB7')
resim_label.place(x=100,y=50)


stil = ttk.Style()
stil.configure("Horizontal.TSeparator", background="#7CB7BB")
cizgi = ttk.Separator(root, orient='horizontal', style="Horizontal.TSeparator")
cizgi.place(x=40, y=250, width=250)
cizgi2 = ttk.Separator(root, orient='vertical',style="Horizontal.TSeparator")
cizgi2.place(x=160, y=260, height=100)
cizgi3 = ttk.Separator(root, orient='horizontal',style="Horizontal.TSeparator")
cizgi3.place(x=40, y=370, width=250)
cizgi4 = ttk.Separator(root, orient='vertical',style="Horizontal.TSeparator")
cizgi4.place(x=160, y=380, height=100)
cizgi5 = ttk.Separator(root, orient='horizontal',style="Horizontal.TSeparator")
cizgi5.place(x=40, y=490, width=250)
cizgi6 = ttk.Separator(root, orient='vertical',style="Horizontal.TSeparator")
cizgi6.place(x=310, y=50, height=600)
cizgi7 = ttk.Separator(root, orient='horizontal',style="Horizontal.TSeparator")
cizgi7.place(x=390, y=210, width=900)







root.mainloop()