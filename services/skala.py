SKALA_UI = [
    (85, "A", 4.0),
    (80, "A-", 3.7),
    (75, "B+", 3.3),
    (70, "B", 3.0),
    (65, "B-", 2.7),
    (60, "C+", 2.3),
    (55, "C", 2.0),
    (40, "D", 1.0),
    (0, "E", 0.0)
]

def nilai_ke_huruf(nilai):
    """Huruf mutu untuk nilai angka. ValueError jika nilai di bawah 0."""
    for batas, huruf, bobot in SKALA_UI:
        if nilai >= batas:
            return huruf
    raise ValueError("Nilai tidak valid")

def huruf_ke_bobot(huruf_dicari):
    """Bobot IPK (misalnya 3.7 untuk "A-"). ValueError jika huruf tidak dikenal."""
    for batas, huruf, bobot in SKALA_UI:
        if huruf_dicari == huruf:
            return bobot
    raise ValueError("Huruf tidak valid")

def batas_bawah(huruf_dicari):
    """Nilai angka minimal untuk mendapat huruf tertentu. ValueError jika huruf tidak dikenal."""
    for batas, huruf, bobot in SKALA_UI:
        if huruf_dicari == huruf:
            return batas
    raise ValueError("Huruf tidak valid")