#%%
class Szopa:
    def __init__(self,bok_a,bok_b,wys_h):
        self.podstawa_a=bok_a
        self_podstawa_b=bok_b
        self_podstawa_h=wys_h

    def Pomaluj(self):
        return 2*(self.podstawa_a + self.podstawa_b)*self.wysokosc_h

szopa1=Szopa(2,3,5)
print(szopa1.Pomaluj())
szopa2=Szopa(5,1,2)
print(szopa2.Pomaluj())


#%%
class KOT: 
    def __init__ (self): 
        self.name = name = ''
        self.kolor_oczu = ''
        self.ogon = ''
        



        def talk (self): pass class Dog (Animal): 
            def talk (self): print ('Hau') class Cat (Animal): 
                def talk ( self): print ('MEOW!')