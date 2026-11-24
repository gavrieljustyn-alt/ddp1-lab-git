from dataclasses import dataclass, field

@dataclass
class Komponen:
    """Satu komponen penilaian. nilai=None berarti belum dinilai."""
    nama: str
    bobot: float
    nilai: float | None = None
    
    def __post_init__(self):
        if not (0 < self.bobot <= 100):
            raise ValueError("Bobot harus lebih dari 0 dan maksimal 100")
        if self.nilai is not None and not (0 <= self.nilai <= 100):  
            raise ValueError("Nilai harus 0 sampai 100")
    
@dataclass
class MataKuliah:
    """Satu mata kuliah beserta SKS dan daftar komponen penilaiannya."""
    nama: str
    sks: int
    komponen: list[Komponen] = field(default_factory=list)
    
    def __post_init__(self):
        if self.sks <= 0:
            raise ValueError('SKS harus lebih dari 0!')
    