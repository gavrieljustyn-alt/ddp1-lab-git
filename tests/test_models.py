from models.matkul import MataKuliah, Komponen
import pytest

def test_bobot_negatif():
    with pytest.raises(ValueError):
        Komponen("UTS", -5, 70)

def test_bobot_lebih_dari_100():
    with pytest.raises(ValueError):
        Komponen("UTS", 150, 70)

def test_nilai_lebih_dari_100():
    with pytest.raises(ValueError):
        Komponen("UTS", 30, 150)

def test_nilai_negatif():
    with pytest.raises(ValueError):
        Komponen("UTS", 30, -1)
        
def test_sks_nol():
    with pytest.raises(ValueError):
        MataKuliah("DDP1", 0)

def test_nilai_batas_sah():
    Komponen("UTS", 30, 0)
    Komponen("UTS", 30, 100)

def test_nilai_none_sah():
    k = Komponen("UAS", 40)
    assert k.nilai is None