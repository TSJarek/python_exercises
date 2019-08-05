class Traktory(object):               
    def __init__(self, model, kolor, producent, udźwig):  
        self.kolor = kolor
        self.producent = producent
        self.udźwig = udźwig
        self.model = model

    def start(self):
        print("Jedzie")

    def stop(self):
        print("Staje")

    def przyspieszenie(self):
        print("przyspieszenie...")
        "Przyśpieszenie działa"

    def skrzynia_biegów(self, Typ_skrzyni='aaaaa'):
        print("Praca_biegów"+Typ_skrzyni)
" Skrzynia biegów działa"

# Wprowadzona nowa instancja w klasie Traktory. Traktor1 ma 4 argumenty.Te argumenty idą do __init__ aby zainicjować obiekt.
Traktor1 = Traktory("Ursus C-152","Ursus", 'Czerwony', '487kNT' )

# Sprawdzenie stanu
#print(Traktor1)
print(Traktor1.stop()) #<-- funkja stop działa
Traktor1.stop()
#print(Traktor1.udźwig) #<-- Atrybut __init__ działa
#Traktor1.przyspieszenie()
#Traktor1.skrzynia_biegów()