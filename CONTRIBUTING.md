# Panduan Kontribusi untuk Rum-us

Pertama-tama, terima kasih telah meluangkan waktu untuk berkontribusi! 🎉

Semua jenis kontribusi diterima, mulai dari melaporkan bug, mengusulkan fitur baru, hingga menambahkan implementasi rumus baru.

## Daftar Isi

- [Kode Etik](#kode-etik)
- [Bagaimana Saya Bisa Berkontribusi?](#bagaimana-saya-bisa-berkontribusi)
  - [Melaporkan Bug](#melaporkan-bug)
  - [Mengusulkan Fitur Baru](#mengusulkan-fitur-baru)
  - [Menambahkan Rumus Baru (Pull Request)](#menambahkan-rumus-baru-pull-request)
- [Panduan Gaya Kode](#panduan-gaya-kode)
  - [Struktur Direktori](#struktur-direktori)
  - [Konvensi Penamaan](#konvensi-penamaan)
  - [Docstrings dan Type Hinting](#docstrings-dan-type-hinting)
  - [Contoh Penggunaan](#contoh-penggunaan)

## Kode Etik

Proyek ini dan semua orang yang berpartisipasi di dalamnya diharapkan untuk mengikuti [Kode Etik](CODE_OF_CONDUCT.md) kami. Dengan berpartisipasi, Anda setuju untuk mematuhi aturan ini.

## Bagaimana Saya Bisa Berkontribusi?

### Melaporkan Bug

Jika Anda menemukan bug, silakan buka _issue_ baru di repositori kami. Pastikan untuk menyertakan informasi selengkapnya, seperti:

- Versi Python yang digunakan.
- Langkah-langkah untuk mereproduksi bug.
- Hasil yang diharapkan vs. hasil yang sebenarnya terjadi.

Gunakan template [Laporan Bug](https://github.com/agwaingit/rum-us/issues/new?assignees=&labels=bug&template=bug_report.md&title=) untuk memudahkan.

### Mengusulkan Fitur Baru

Jika Anda memiliki ide untuk fitur baru atau penambahan rumus yang belum ada, kami sangat senang mendengarnya! Buka _issue_ baru dan jelaskan ide Anda. Gunakan template [Permintaan Fitur](https://github.com/agwaingit/rum-us/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=).

### Menambahkan Rumus Baru (Pull Request)

Ini adalah cara terbaik untuk menambahkan rumus baru ke dalam koleksi.

1.  **Fork** repositori `agwaingit/rum-us`.
2.  **Clone** fork Anda ke mesin lokal.
3.  Buat **branch baru** untuk pekerjaan Anda (`git checkout -b fitur/rumus-pythagoras`). Nama branch harus deskriptif.
4.  Tambahkan atau ubah kode sesuai dengan Panduan Gaya Kode.
5.  **Commit** perubahan Anda dengan pesan yang jelas (`git commit -m 'feat: Menambahkan implementasi rumus Pythagoras'`).
6.  **Push** ke branch Anda (`git push origin fitur/rumus-pythagoras`).
7.  Buka **Pull Request** ke branch `main` dari repositori `agwaingit/rum-us`.

## Panduan Gaya Kode

Untuk menjaga konsistensi dan keterbacaan kode, mohon ikuti panduan berikut.

### Struktur Direktori

Letakkan file Python Anda di direktori yang sesuai:

- `matematika/` untuk semua rumus yang berhubungan dengan matematika.
- `fisika/` untuk semua rumus yang berhubungan dengan fisika.

### Konvensi Penamaan

- **Nama File**: Gunakan `snake_case` (huruf kecil dengan garis bawah). Contoh: `luas_lingkaran.py`, `hukum_ohm.py`.
- **Nama Fungsi**: Gunakan `snake_case`. Contoh: `hitung_luas_lingkaran`, `cari_tegangan`.

### Docstrings dan Type Hinting

Setiap fungsi **wajib** memiliki _docstring_ dan _type hinting_. Docstring harus menjelaskan:

1.  Tujuan fungsi.
2.  Penjelasan singkat tentang rumus yang digunakan.
3.  Deskripsi setiap parameter (`Args`).
4.  Deskripsi nilai yang dikembalikan (`Returns`).

**Contoh Template:**

```python
def hitung_luas_persegi(sisi: float) -> float:
    """Menghitung luas dari sebuah persegi.

    Rumus: Luas = sisi * sisi

    Args:
        sisi (float): Panjang sisi persegi.

    Returns:
        float: Luas dari persegi tersebut.
    """
    return sisi * sisi

```

### Contoh Penggunaan

Sertakan blok `if __name__ == "__main__":` di akhir setiap file untuk menunjukkan contoh cara menggunakan fungsi tersebut. Ini sangat membantu untuk pengujian cepat dan sebagai dokumentasi.

**Contoh:**

```python
# ... (kode fungsi di atas)

if __name__ == "__main__":
    panjang_sisi = 10.0
    luas = hitung_luas_persegi(panjang_sisi)
    print(f"Persegi dengan sisi {panjang_sisi} memiliki luas {luas}")

```

Terima kasih sekali lagi atas kontribusi Anda!
