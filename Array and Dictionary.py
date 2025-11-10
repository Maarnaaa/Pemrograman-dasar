print("=== DATA MAHASISWA (ARRAY) ===")

# Array berisi nama mahasiswa
mahasiswa = ["Marna", "Indriani", "Maya"]
print("Data awal:", mahasiswa)

# Mengakses data
print("Mahasiswa urutan pertama:", mahasiswa[0])

# Menambah data baru
mahasiswa.append("Salsa")
print("Setelah penambahan:", mahasiswa)

# Menghapus salah satu data
mahasiswa.remove("Indriani")
print("Setelah penghapusan:", mahasiswa)


print("\n=== DATA BUKU PERPUSTAKAAN (DICTIONARY) ===")

# Dictionary berisi data buku: harga & stok
buku_perpus = {
    "Dasar Pemrograman": {"harga": 70000, "stok": 10},
    "Matematika Diskrit": {"harga": 85000, "stok": 6},
    "Jaringan Komputer": {"harga": 92000, "stok": 4}
}

# Mengakses data tertentu
print("Harga buku 'Dasar Pemrograman': Rp", buku_perpus["Dasar Pemrograman"]["harga"])
print("Stok buku 'Matematika Diskrit':", buku_perpus["Matematika Diskrit"]["stok"])

# Menampilkan seluruh data buku
print("\nDaftar Buku:")
for judul, info in buku_perpus.items():
    print(f"{judul} - Harga: Rp{info['harga']} | Stok: {info['stok']} buah")
