


class Agama:
    def __init__(self, nama, agama):
        self.agama = agama
        self.nama = nama

    def mengenalkandiri(self):
        print(self.nama, "Beragama", self.agama)

class Islam(Agama):
    def __init__(self, nama, agama, ibadah1):
        Agama.__init__(self, nama, agama)
        self.ibadah1 = ibadah1

class Buddha(Agama):
    def __init__(self, nama, agama, ibadah2):
        Agama.__init__(self, nama, agama)
        self.ibadah2 = ibadah2 


Dava = Islam('Dava', 'Islam', 'Sholat')
Dava.mengenalkandiri()
print("Saya beribadah dengan melakukan", Dava.ibadah1, "\n")

Bongchin = Buddha('Bongchin', 'Buddha', 'Sembahyang')
Bongchin.mengenalkandiri()
print("Saya beribadah dengan melakukan", Bongchin.ibadah2, "\n")