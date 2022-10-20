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
    #rekina_summa=None

    def __init__(self, name=None, text=None, platums=None, garums=None, augstums=None, materiala_cena=None):
        self.name=input('vards')
        self.text=input('veltijuma teksts')
        self.platums=int(input('platums'))
        self.garums=int(input('garums'))
        self.augstums=int(input('augstums'))
        self.materiala_cena=float(input('materiala cena'))
        self.izdrukat()


    def aprekins(self):
        self.darba_samaksa=15
        self.pvn=21
        self.produkta_cena=(len(self.text))*1.2+((self.platums/100)*(self.garums/100)*(self.augstums/100))/3*self.materiala_cena
        #self.pvn_summa=(self.produkta_cena+self.darba_samaksa)*(self.pvn/100)
        #self.rekina_summa=(self.produkta_cena+self.darba_samaksa)*self.pvn_summa
        
        

    def izdrukat(self):
        #self.produkta_cena=(len(self.text))*1.2+(self.platums/100*self.garums/100*self.augstums/100)/3*self.materiala_cena
        print (f'vārds: {self.name}\nteksts: {self.text}\nplatums,garums,augstums: {self.platums},{self.garums},{self.augstums}\nmateriala cena eur/m2: {self.materiala_cena}\nprodukta cena: {self.produkta.cena}')

print("laiks=", dt_string)	

person1=Rekins()