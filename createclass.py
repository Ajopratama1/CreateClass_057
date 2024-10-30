class PersegiPanjang:
    def __init__(self, panjang, lebar):# untuk menginisialisasi properti P dan L dri objek pp
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):#menyediakan representasi string dri objek pp
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    
    #untuk nguji iwir
pp = PersegiPanjang(3,2 )
print(pp) #ouput p 3, l 2
print("Keliling:", pp.hitung_keliling())
print("Luas:", pp.hitung_luas())
