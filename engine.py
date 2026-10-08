# =========================================================
# ENGINE LOGIKA (engine.py)
# =========================================================

DIK_CF_USER = {
    "Tidak": 0.0,
    "Sedikit Yakin": 0.2,
    "Cukup Yakin": 0.4,
    "Yakin": 0.8,
    "Sangat Yakin": 1.0
}

def cf_and(*values):
    """Mencari nilai minimum untuk kondisi AND (Sesuai rumus gambar)"""
    return min(values)

def proses_forward_chaining_cf(g1, g2, g3, g4, g5, g6, g7, g8):
    input_gejala = {
        "G1": g1, "G2": g2, "G3": g3, "G4": g4,
        "G5": g5, "G6": g6, "G7": g7, "G8": g8
    }
    
    G = {kode: DIK_CF_USER.get(jawaban, 0.0) for kode, jawaban in input_gejala.items()}
    
    log = []
    log.append("=== LOG PENALARAN FORWARD CHAINING ===")
    
    F1, F2, F3, F4, F5 = 0.0, 0.0, 0.0, 0.0, 0.0
    P1, P2, P3 = 0.0, 0.0, 0.0
    
    # --- R1 - R3 ---
    if G["G1"] > 0 and G["G5"] > 0:
        F1 = cf_and(G["G1"], G["G5"]) * 0.90
        log.append(f"[✓] R1 Terpemicu: G1({G['G1']}) AND G5({G['G5']}) -> F1 = {F1:.4f}")
    else:
        log.append("[X] R1 Tidak Aktif (Syarat G1 AND G5 tidak terpenuhi)")
        
    if G["G3"] > 0 and G["G4"] > 0:
        F2 = cf_and(G["G3"], G["G4"]) * 0.85
        log.append(f"[✓] R2 Terpemicu: G3({G['G3']}) AND G4({G['G4']}) -> F2 = {F2:.4f}")
    else:
        log.append("[X] R2 Tidak Aktif (Syarat G3 AND G4 tidak terpenuhi)")
        
    if G["G7"] > 0 and G["G8"] > 0:
        F3 = cf_and(G["G7"], G["G8"]) * 0.90
        log.append(f"[✓] R3 Terpemicu: G7({G['G7']}) AND G8({G['G8']}) -> F3 = {F3:.4f}")
    else:
        log.append("[X] R3 Tidak Aktif (Syarat G7 AND G8 tidak terpenuhi)")

    # --- R4 ---
    if F1 > 0 and F2 > 0:
        F4 = cf_and(F1, F2) * 0.90
        log.append(f"[✓] R4 Terpemicu: F1({F1:.4f}) AND F2({F2:.4f}) -> F4 = {F4:.4f}")
    else:
        log.append("[X] R4 Tidak Aktif (Syarat F1 AND F2 tidak terpenuhi)")

    # --- R5 - R8 ---
    if F4 > 0 and G["G6"] > 0:
        P1 = cf_and(F4, G["G6"]) * 0.85
        log.append(f"[✓] R5 Terpemicu: F4({F4:.4f}) AND G6({G['G6']}) -> P1 = {P1:.4f}")
    else:
        log.append("[X] R5 Tidak Aktif (Syarat F4 AND G6 tidak terpenuhi)")

    if P1 > 0 and F3 > 0:
        F5 = cf_and(P1, F3) * 0.90
        log.append(f"[✓] R6 Terpemicu: P1({P1:.4f}) AND F3({F3:.4f}) -> F5 = {F5:.4f}")
    else:
        log.append("[X] R6 Tidak Aktif (Syarat P1 AND F3 tidak terpenuhi)")

    if F5 > 0 and G["G2"] > 0:
        P2 = cf_and(F5, G["G2"]) * 0.95
        log.append(f"[✓] R7 Terpemicu: F5({F5:.4f}) AND G2({G['G2']}) -> P2 = {P2:.4f}")
    else:
        log.append("[X] R7 Tidak Aktif (Syarat F5 AND G2 tidak terpenuhi)")

    if P2 > 0 and G["G6"] > 0:
        P3 = cf_and(P2, G["G6"]) * 0.95
        log.append(f"[✓] R8 Terpemicu: P2({P2:.4f}) AND G6({G['G6']}) -> P3 = {P3:.4f}")
    else:
        log.append("[X] R8 Tidak Aktif (Syarat P2 AND G6 tidak terpenuhi)")

    # --- HIARARKI GOAL ---
    if P3 > 0:
        kategori = "Burnout Berat"
        cf_final = P3
    elif P2 > 0:
        kategori = "Burnout Sedang"
        cf_final = P2
    elif P1 > 0:
        kategori = "Burnout Ringan"
        cf_final = P1
    else:
        kategori = "Tidak Terdeteksi Burnout"
        cf_final = 0.0

    persentase = cf_final * 100
    return kategori, persentase, log, G