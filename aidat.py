#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gökyüzü Aidat Hesaplayıcı — Resmi Sürüm 0.0.1"""

import random
import datetime

TARIFE = {
    "acik_hava": 17.5,
    "parcali_bulut": 42.0,
    "kapali": 91.3,
    "yagmur": 128.7,
    "gokkusagi": 3.14,  # indirimli, çünkü estetik katkı
}

VATANDAS_KATSAYISI = 1.08  # enflasyon düzeltmesi değil, “ruh hali” katsayısı

def gokyuzu_durumu_sor():
    print("Bugün gökyüzüne baktınız mı? (cevap vermeseniz de aidat kesilir)")
    durumlar = list(TARIFE.keys())
    durum = random.choice(durumlar)
    print(f"Sistem otomatik tespit etti: {durum.upper()}")
    return durum

def hesapla(durum, bakis_suresi_saniye=8):
    taban = TARIFE[durum]
    sure_carpan = max(1, bakis_suresi_saniye / 10)
    tutar = taban * sure_carpan * VATANDAS_KATSAYISI
    return round(tutar, 2)

def makbuz_bas(tutar, durum):
    print("\n======= GÖKYÜZÜ İŞLETME MÜDÜRLÜĞÜ =======")
    print(f"Tarih     : {datetime.date.today().isoformat()}")
    print(f"Hizmet    : {durum} görüntüleme")
    print(f"Tutar     : {tutar} TL (KDV dahil değil çünkü gökyüzü KDV'siz)")
    print("Ödeme yeri: En yakın rüzgâr.")
    print("==========================================\n")
    print("(Bu makbuz yasal değer taşımaz. Taşısa da kimse okumaz.)")

if __name__ == "__main__":
    d = gokyuzu_durumu_sor()
    t = hesapla(d, bakis_suresi_saniye=random.randint(3, 40))
    makbuz_bas(t, d)
