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
        self.name=input('vards: ')
        self.text=input('veltijuma teksts: ')
        self.platums=int(input('platums: '))
        self.garums=int(input('garums: '))
        self.augstums=int(input('augstums: '))
        self.materiala_cena=float(input('materiala cena: '))
        self.izdrukat()


    """def aprekins(self, produkta_cena):  
        self.darba_samaksa=15
        self.pvn=21
        self.produkta_cena=12
        print('Pārbaude')
        self.produkta_cena=(len(self.text))*1.2+(self.platums/100*self.garums/100*self.augstums/100)/3*self.materiala_cena
        #pvn_summa=(produkta_cena+darba_samaksa)*(pvn/100)
        #rekina_summa=(produkta_cena+darba_samaksa)*pvn_summa"""
        
        

    def izdrukat(self):
        self.produkta_cena=(len(self.text))*1.2+(self.platums/100*self.garums/100*self.augstums/100)/3*self.materiala_cena
        self.pvn_summa=(self.produkta_cena+15)*(21/100)
        self.rekina_summa=(self.produkta_cena+15)*self.pvn_summa
        print (f'vārds: {self.name}\nteksts: {self.text}\nplatums,garums,augstums: {self.platums},{self.garums},{self.augstums}')
        print(f'materiala cena eur/m2: {self.materiala_cena}\nrekina summa: {round(self.rekina_summa,2)}')
        self.saglabat()

    def saglabat(self):
        file=open(self.name+"_rekins.txt", "w")
        file.write(f"Klients {self.name}\n teksts {self.text}\nizmers {self.augstums}x{self.platums}x{self.garums}mm\n cena {round(self.rekina_summa,2)}\n{dt_string}" )



print("laiks=", dt_string)	

person1=Rekins()