class BankAccount:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self._saldo = saldo_awal
        
    # Method getter untuk membaca saldo (tanpa bisa diubah langsung)
    def get_saldo(self):
        return self._saldo
    
    # Method setter untuk memperbarui saldo dengan validasi
    def set_saldo(self, jumlah):
        if jumlah < 0:
            print("Jumlah saldo tidak boleh negatif!")
        else:
            self._saldo = jumlah
            print(f"Saldo berhasil diperbarui menjadi: {self._saldo}")
    
    # Metode untuk menambah saldo
    def deposit(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah
            print(f"Saldo bertambah: {jumlah}, Saldo sekarang: {self._saldo}")
        else:
            print("Jumlah deposit harus positif!")
            
    # Metode untuk menarik saldo
    def withdraw(self, jumlah):
        if jumlah > 0 and jumlah <= self._saldo:
            self._saldo -= jumlah
            print(f"Berhasil menarik: {jumlah}, Saldo sekarang: {self._saldo}")
        else:
            print("Penarikan gagal: saldo tidak mencukupi atau jumlah tidak valid")
                
# contoh penggunaan
akun = BankAccount("Martin", 1000)
print(akun.get_saldo())

akun.set_saldo(2000)
akun.deposit(500)
akun.withdraw(1000)