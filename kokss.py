from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

class Rekins:
    name=None
    text=None
    platums=None
    garums=None
    augstums=None
    materiala_cena=None

    def __init__(self, name=None, text=None, platums=None, garums=None, augstums=None, materiala_cena=None):
        self.name=name
        self.text=text
        self.platums=platums
        self.garums=garums
        self.augstums=augstums
        self.materiala_cena=materiala_cena
        self.izdrukat()

    def izdrukat(self):
        print (f'vārds: {self.name}\nteksts: {self.text}\nplatums,garums,augstums: {self.platums},{self.garums},{self.augstums}\nmateriala cena eur/m2: {self.materiala_cena}')

    def aprekins(self):
        darba_samaksa=15
        pvn=21
        produkta_cena=(len(text))*1.2+(platums/100*garums/100*augstums/100)/3*materiala_cena
        pvn_summa=(produkta_cena+darba_samaksa)*(pvn/100)
        


print("laiks=", dt_string)	

person1=Rekins("amanda", "kfsfknsfk ",500, 200, 400, 0.3)