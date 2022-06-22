from fuzzy_1 import (
    down,
    Permintaan,
    Persediaan,
    Produksi,
    up
)

class PermintaanBaru(Permintaan):
    median = 2800

    def turun(self, x):
        if x >= self.median:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.median)
    
    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.median:
            return 0
        else:
            return up(x, self.median, self.maximum)
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.median:
            return up(x, self.minimum, self.median)
        elif self.median < x < self.maximum:
            return down(x, self.median, self.maximum)
        else:
            return 1

class ProduksiBaru(Produksi):

    def _inferensi(self):
        pmt = PermintaanBaru()
        psd = Persediaan()
        data_inferensi = super()._inferensi(pmt=pmt)
        # [R5] JIKA Permintaan TETAP, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERTAMBAH.
        a5 = min(pmt.tetap(self.permintaan), psd.sedikit(self.persediaan))
        z5 = self._bertambah(a5)
        data_inferensi.append((a5, z5))
        # [R6] JIKA Permintaan TETAP, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERKURANG.
        a6 = min(pmt.tetap(self.permintaan), psd.sedikit(self.persediaan))
        z6 = self._berkurang(a6)
        data_inferensi.append((a6, z6))
        return data_inferensi

    def defuzifikasi(self):
        return super().defuzifikasi(self._inferensi())