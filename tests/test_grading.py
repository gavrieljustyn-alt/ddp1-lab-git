from models.matkul import MataKuliah, Komponen
from services.grading import hitung_nilai_akhir, nilai_minimal
import pytest

def test_nilai_akhir_lengkap():
    m = MataKuliah("DDP1", 4, [
        Komponen("Tugas", 30, 80),
        Komponen("UTS", 30, 70),
        Komponen("UAS", 40, 90),
    ])
    assert hitung_nilai_akhir(m) == 81
    
def test_nilai_akhir_belum_lengkap():
    m = MataKuliah("DDP1", 4, [
        Komponen("Tugas", 30, 80),
        Komponen("UTS", 30, 70),
        Komponen("UAS", 40), 
    ])
    with pytest.raises(ValueError):
        hitung_nilai_akhir(m)
    
def test_nilai_akhir_bobot_salah():
    m = MataKuliah("DDP1", 4, [
        Komponen("Tugas", 30, 80),
        Komponen("UTS", 30, 70),
        Komponen("UAS", 30, 90),
    ])
    with pytest.raises(ValueError):
            hitung_nilai_akhir(m)
            
def test_nilai_minimal_a():
    m = MataKuliah("DDP1", 4, [
            Komponen("Tugas", 30, 80),
            Komponen("UTS", 30, 70),
            Komponen("UAS", 40), 
    ])
    assert nilai_minimal(m, "A") == 100
                
def test_nilai_minimal_a_minus():
    m = MataKuliah("DDP1", 4, [
            Komponen("Tugas", 30, 80),
            Komponen("UTS", 30, 70),
            Komponen("UAS", 40), 
    ])
    assert nilai_minimal(m, "A-") == 87.5
            
def test_nilai_minimal_sudah_aman():
    m = MataKuliah("DDP1", 4, [
            Komponen("Tugas", 30, 80),
            Komponen("UTS", 30, 70),
            Komponen("UAS", 40), 
    ])
    assert nilai_minimal(m, "E") == 0
            
def test_nilai_minimal_mustahil():
    m = MataKuliah("DDP1", 4, [
            Komponen("Tugas", 30, 50),
            Komponen("UTS", 30, 50),
            Komponen("UAS", 40), 
    ])
    assert nilai_minimal(m, 'A') is None
            
def test_nilai_minimal_tanpa_sisa():
    m = MataKuliah("DDP1", 4, [
            Komponen("Tugas", 30, 80),
            Komponen("UTS", 30, 70),
            Komponen("UAS", 40, 60), 
    ])
    assert nilai_minimal(m, 'A') is None