from dataclasses import dataclass, field

@dataclass
class Komponen:
    nama: str
    bobot: float
    nilai: float | None = None
    
@dataclass
class MataKuliah:
    nama: str
    sks: int
    komponen: list[Komponen] = field(default_factory=list)
    
m = MataKuliah("DDP1", 4, [
    Komponen("Tugas", 30, 80),
    Komponen("UTS", 30, 70),
    Komponen("UAS", 40),
])
print(m.nama, m.sks, len(m.komponen))
print(m.komponen[2])