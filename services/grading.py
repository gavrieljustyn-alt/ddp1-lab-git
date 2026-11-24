from models.matkul import MataKuliah, Komponen
from services.skala import batas_bawah

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

def nilai_minimal(matkul, target_huruf):
    target = batas_bawah(target_huruf)
    selisih = target - nilai_sementara(matkul)
    
    if selisih <= 0:
        return 0
    
    sisa_bobot = 0
    for k in matkul.komponen:
        if k.nilai == None:                     
            sisa_bobot += k.bobot
    
    if sisa_bobot == 0:
        return None
    
    dibutuhkan = selisih / (sisa_bobot / 100)
    if dibutuhkan > 100:
        return None
    return dibutuhkan