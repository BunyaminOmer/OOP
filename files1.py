class HepsiburadaKullaniciBilgisi:

    def __init__(self, name, surname, age, money):
        self.name = name
        self.surname = surname
        self.age = age
        self.money = money

    def __str__(self):
        return f"Ad : {self.name} Soyad : {self.surname} Yaş : {self.age} Hepsibay Bakiye : {self.money}"

kullanici = HepsiburadaKullaniciBilgisi("Yunus Emre","Karakuş",23,1000.46)
print(kullanici)