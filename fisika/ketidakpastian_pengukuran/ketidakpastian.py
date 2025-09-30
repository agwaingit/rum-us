import math
import statistics


def hitung_ketidakpastian(data: list[float]) -> tuple[float, float, float]:
    """
    Menghitung ketidakpastian absolut, rata-rata, dan ketidakpastian relatif
    dari serangkaian data pengukuran.

    Args:
        data: Sebuah list berisi angka (float atau int) dari data pengukuran.

    Returns:
        Sebuah tuple berisi:
        - Ketidakpastian absolut (standar deviasi dari rata-rata).
        - Rata-rata dari data.
        - Ketidakpastian relatif.
    """
    N = len(data)
    if N < 2:
        raise ValueError("Perhitungan ketidakpastian memerlukan setidaknya dua data poin.")

    # Menghitung rata-rata (mean) dari data.
    rata_rata = statistics.mean(data)

    # Menghitung standar deviasi sampel (s).
    # ddof=1 digunakan untuk standar deviasi sampel (pembagi N-1).
    standar_deviasi = statistics.stdev(data)

    # Menghitung ketidakpastian absolut (Δx), yaitu standar deviasi dari rata-rata.
    # Rumus: Δx = s / sqrt(N)
    ketidakpastian_absolut = standar_deviasi / math.sqrt(N)

    # Menghitung ketidakpastian relatif.
    # Hindari pembagian dengan nol jika rata-rata adalah 0.
    ketidakpastian_relatif = (
        ketidakpastian_absolut / rata_rata if rata_rata != 0 else float("inf")
    )

    return ketidakpastian_absolut, rata_rata, ketidakpastian_relatif


def main() :
    data = [2, 4, 6, 8, 10]
    delta_x, rata_rata, delta_x_rel = hitung_ketidakpastian(data)
    print(f"Data: {data}")
    print(f"Ketidakpastian Absolut (Δx) = {delta_x:.4f}")
    print(f"Rata-rata (x̄) = {rata_rata:.4f}")
    print(f"Ketidakpastian Relatif = {delta_x_rel:.4f} atau {delta_x_rel:.2%}")

if __name__ == "__main__":
    main()