import math

# Rumus delta_x
def ketidakpastian_absolut (data):
    #Jumlah data N
    N = len(data)

    #xi data ke-i, i adalah 1 sampai N: data[i]
    #xi2 data ke-i dikuadratkan, data[i]**2 

    #Penjumlahan dari data atau xi
    sum_x = sum(data)

    #Penjumlahan dari data dikuadratkan atau xi2
    sum_x2 = sum(x**2 for x in data)

    # Rumusnya berjalan seperti ini:
    pembilang = N * sum_x2 - (sum_x)**2
    penyebut = N - 1
    hasil = 1 / math.sqrt(N) * math.sqrt(pembilang / penyebut)
    return hasil

def ketidakpastian_relatif(data):
    N = len(data)

    # Rata-rata data
    rerata_x = sum(data) / N

    # Ketidakpastian absolut
    delta_x = ketidakpastian_absolut(data)

    # delta_x dibagi dengan rata-rata data untuk mendapatakan ketidakpastian_relatif
    ketidakpastian_rel = delta_x / rerata_x

    return delta_x, rerata_x, ketidakpastian_rel

def main() :
    data = [2, 4, 6, 8, 10]
    abs_u, mean, rel_u = ketidakpastian_relatif(data)
    print(f"Δx (absolut) = {abs_u}")
    print(f"Rata-rata = {mean}")
    print(f"Δx_rel (relatif) = {rel_u}")

if __name__ == "__main__":
    main()