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
    produkta_cena=None

    def __init__(self, name=None, text=None, platums=None, garums=None, augstums=None, materiala_cena=None):
        self.name=input('vards')
        self.text=input('veltijuma teksts')
        self.platums=int(input('platums'))
        self.garums=int(input('garums'))
        self.augstums=int(input('augstums'))
        self.materiala_cena=float(input('materiala cena'))
        self.izdrukat()


    def aprekins(self, produkta_cena=None):
        #darba_samaksa=15
        #pvn=21
        produkta_cena=(len(self.text))*1.2+(self.platums/100*self.garums/100*self.augstums/100)/3*self.materiala_cena
        #pvn_summa=(produkta_cena+darba_samaksa)*(pvn/100)
        #rekina_summa=(produkta_cena+darba_samaksa)*pvn_summa
        
        

    def izdrukat(self):
        print (f'vārds: {self.name}\nteksts: {self.text}\nplatums,garums,augstums: {self.platums},{self.garums},{self.augstums}\nmateriala cena eur/m2: {self.materiala_cena}\nprodukta cena: {self.produkta_cena}')

print("laiks=", dt_string)	

person1=Rekins()