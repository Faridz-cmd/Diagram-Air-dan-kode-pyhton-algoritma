def is_prime(n):
    if n <= 1:
        return False  # Bukan bilangan prima
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Ditemukan pembagi selain 1 dan n
    return True  # Tidak ada pembagi selain 1 dan n

# Contoh penggunaan
angka = int(input("Masukkan angka: "))
if is_prime(angka):
    print(f"{angka} adalah bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")
