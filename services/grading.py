from models.matkul import MataKuliah, Komponen
from services.skala import batas_bawah, huruf_ke_bobot

def total_bobot(matkul):
    """Jumlah bobot (persen) semua komponen matkul."""
    total = 0
    for k in matkul.komponen:
        total += k.bobot
    return total
        
def nilai_sementara(matkul):
    """Poin (skala 0-100) yang sudah terkumpul dari komponen yang sudah dinilai.
    Komponen dengan nilai None diabaikan."""
    total_nilai = 0
    for k in matkul.komponen:
        if k.nilai is not None:
            total_nilai += k.nilai * k.bobot / 100
    return total_nilai

def hitung_nilai_akhir(matkul):
    """Nilai akhir (skala 0-100) dari matkul yang semua komponennya sudah dinilai.

    Raises:
        ValueError: jika total bobot bukan 100 atau ada komponen yang belum dinilai.
    """
    if total_bobot(matkul) != 100:
        raise ValueError("Total bobot harus 100")
    for k in matkul.komponen:
        if k.nilai is None:
            raise ValueError("Masih ada komponen yang belum dinilai")
    return nilai_sementara(matkul)

def nilai_minimal(matkul, target_huruf):
    """Nilai minimal yang harus diraih di komponen yang belum dinilai
    agar nilai akhir mencapai target_huruf (misalnya "A", "B+").

    Returns:
        0 jika target sudah pasti tercapai.
        float (0-100) berupa nilai minimal yang dibutuhkan.
        None jika mustahil (butuh > 100) atau tidak ada komponen tersisa.

    Raises:
        ValueError: jika target_huruf tidak dikenal.
    """
    target = batas_bawah(target_huruf)
    selisih = target - nilai_sementara(matkul)
    
    if selisih <= 0:
        return 0
    
    sisa_bobot = 0
    for k in matkul.komponen:
        if k.nilai is None:                     
            sisa_bobot += k.bobot
    
    if sisa_bobot == 0:
        return None
    
    dibutuhkan = selisih / (sisa_bobot / 100)
    if dibutuhkan > 100:
        return None
    return dibutuhkan

def hitung_ipk(riwayat):
    """Hitung IPK sebagai rata-rata tertimbang SKS.

    Args:
        riwayat: list tuple (sks, huruf), contoh [(4, "A"), (3, "B")].

    Returns:
        IPK (float), atau 0.0 jika riwayat kosong.

    Raises:
        ValueError: jika sks <= 0 atau huruf tidak dikenal.
    """
    if not riwayat:
        return 0.0

    total_poin = 0
    total_sks = 0
    for sks, huruf in riwayat:
        if sks <= 0:
            raise ValueError('SKS harus lebih dari 0')
        total_poin += sks * huruf_ke_bobot(huruf)
        total_sks += sks
    return total_poin / total_sks