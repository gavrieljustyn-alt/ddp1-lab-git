from models.matkul import MataKuliah, Komponen
from services.grading import hitung_nilai_akhir
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
            Komponen("UAS", 40), 
    ])
    with pytest.raises(ValueError):
            hitung_nilai_akhir(m)