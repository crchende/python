# Clasa eroare derivata din clasa standard: Exception
class EroareTelefon(Exception):
    def __init__(self, msg):
        self.errmsg = msg + "--NOUA CLS ERR--"
        #self.errno = errno
        self.args = (self.errmsg,)

class TastaturaTelefon:
    def __init__(self):
        pass
        
    def formeaza_numar(self, numar):
        return(f"NUMAR FORMAT: {numar}")
    

class Telefon:
    def __init__(self, cul):
        self.culoare = cul # var publica
        self.__suna = "NU" # var privata
        self._in_apel = 0  # var protejata
        self.tastatura = TastaturaTelefon()

    def primeste_apel(self):
        self.__suna = "SUNA, primesc apel!"
        print(self.__suna)
        
    def raspunde_apel(self):
        self._in_apel = 1
        self.__suna = "NU"
        print("RASPUND LA APEL")

    def inchide_apel(self):
        self.in_apel = 0
        self.__suna = "NU"
        print("INCHID APEL")
        
    def apeleaza(self, numar):
        info_tastat = self.tastatura.formeaza_numar(numar)
        lst1 = info_tastat.split(':')
        nr = lst1[-1].strip()
        print(f"APELEZ NUMARUL: {nr}")
        
        
class AplicatieTelefon(Telefon):
    def __init__(self, prod):
        self.producator = prod
        self.sunet_apel = "melodie1"
        self.agenda = {}
        super().__init__('NA')
        
    def primeste_apel(self):
        super().primeste_apel()
        print(self.sunet_apel)
        
    def adauga_in_agenda(self, nume, numar):
        self.agenda[nume] = numar
        
    def cauta_nr_in_agenda(self, nume):
        return(self.agenda.get(nume))
        

class AparatTelefonMobil:
    def __init__(self, prod, model):
        self.producator = prod
        self.model = model
        self.aplicatii_incluse = set()
        self.aplicatii_instalate = set()
        
        self.app_telefon = \
            AplicatieTelefon("android")
        
        self.aplicatii_incluse.add(self.app_telefon)

        self.aplicatii = \
           self.aplicatii_incluse.union(\
           self.aplicatii_instalate)  

    def instaleaza_app(self, app):
        if app in self.aplicatii:
            # Utilizare clasa eroare derivata
            raise(EroareTelefon(f"{app}, este deja instalata!"))
        self.aplicatii_instalate.add(app)
        self.aplicatii.add(app)
        
class AppWhatsApp:
    pass

print('\n----- telefon fix -----')
telefon_fix1 = Telefon("crem")
telefon_fix1.apeleaza("4567")
telefon_fix1.primeste_apel()

print('\n----- telefon mobil -----')
mobil1 = AparatTelefonMobil("Samsung", "S23")
mobil1.app_telefon.apeleaza("123")
mobil1.app_telefon.primeste_apel()
print("Aplicatii instalate:", mobil1.aplicatii)

whatsapp = AppWhatsApp()
mobil1.instaleaza_app(whatsapp)
print("Aplicatii instalate:", mobil1.aplicatii)

# mai incercam sa instalam aplicatia - ne asteptam sa vedem o eroare
try:
    mobil1.instaleaza_app(whatsapp)
except Exception as e:
    print("Eroare la instalare:", e)

print("Aplicatii instalate:", mobil1.aplicatii)

print()
print("* acces vaiabila publica:", \
	telefon_fix1.culoare)
print("* acces vaiabila protejata:", \
	telefon_fix1._in_apel)
print('* acces variabila privata, folosind numele extins: _<Clasa>__<var>:', \
	mobil1.app_telefon._Telefon__suna)

# Variabila privata nu poate fi accesata direct. Se genereaza eroare:
try:	
    print('* acces variabila privata:', \
	    mobil1.app_telefon.__suna)
except Exception as e:
    print("EROARE:", e.__class__.__name__, e)