from models.matkul import MataKuliah, Komponen

def total_bobot(matkul):
    total = 0
    for k in matkul.komponen:
        total += k.bobot
    return total
        
def nilai_sementara(matkul):
    total_nilai = 0
    for k in matkul.komponen:
        if k.nilai is not None:
            total_nilai += k.nilai * k.bobot / 100
    return total_nilai

def hitung_nilai_akhir(matkul):
    if total_bobot(matkul) != 100:
        raise ValueError("Total bobot harus 100")
    for k in matkul.komponen:
        if k.nilai == None:
            raise ValueError("Masih ada komponen yang belum dinilai")
    return nilai_sementara(matkul)

m = MataKuliah("DDP1", 4, [
    Komponen("Tugas", 30, 80),
    Komponen("UTS", 30, 70),
    Komponen("UAS", 40),
])