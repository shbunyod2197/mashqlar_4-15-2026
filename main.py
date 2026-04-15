# 1
class Kitob:
    def __init__(self, n, m):
        self.nomi = n
        self.muallif = m

kitob1 = Kitob("O‘tkan kunlar", "Abdulla Qodiriy")
print(kitob1.nomi, kitob1.muallif)

kitob2 = Kitob("Mehrobdan chayon", "Abdulla Qodiriy")
print(kitob2.nomi, kitob2.muallif)

# 2
class Talaba:
    def __init__(self, i, y):
        self.ism = i
        self.yosh = y

talaba1 = Talaba("Ali", 21)
print(talaba1.ism, talaba1.yosh)

talaba2 = Talaba("Vali", 22)
print(talaba2.ism, talaba2.yosh)

# 3
class Telefon:
    def __init__(self, m, n):
        self.model = m
        self.narx = n

tel1 = Telefon("Apple", 23445)
print(tel1.model, tel1.narx)

tel2 = Telefon("Samsung", 234333)
print(tel2.model, tel2.narx)

# 4
class Shahar:
    def __init__(self, n,a):
        self.nomi = n
        self.aholisi = a

tel1 = Shahar("Xorazim", 2377)
print(tel1.nomi, tel1.aholisi)

tel2 = Shahar("Samsung", 2843)
print(tel2.nomi, tel2.aholisi)

# 5
class Mashina:
    def __init__(self, m, r):
        self.marka = m
        self.rang = r

tel1 = Mashina("Matiz", "oq")
print(tel1.marka, tel1.rang)

tel2 = Mashina("Ekskavator", "qora")
print(tel2.marka, tel2.rang)
