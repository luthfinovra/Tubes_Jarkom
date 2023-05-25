package main

import "fmt"

func luaslingkaran(r float64) float64 {
	return (22 * r * r) / 7
}
func kelilinglingkaran(r float64) float64 {
	return (22 * r) / 7
}
func volumebola(r float64) float64 {
	return (4 * 22 * r * r * r) / 21
}
func main() {
	var r float64
	var a, b int
	for a != 4 {
		fmt.Println()
		fmt.Println("Pilihlah Operasi Yang Ingin Anda Lakukan")
		fmt.Println("1. Operasi mencari luas lingkaran")
		fmt.Println("2. Operasi mencari keliling lingkaran")
		fmt.Println("3. Operasi mencari volume bola")
		fmt.Println("4. Exit")
		fmt.Print("Pilih Operasi nomor berapa yang ingin anda lakukan: ")
		fmt.Scanln(&a)
		if a == 1 {
			fmt.Print("Inputkan Jari-Jari: ")
			fmt.Scanln(&r)
			fmt.Println("luas lingkaran =", luaslingkaran(r))
		} else if a == 2 {
			fmt.Print("Inputkan Jari-Jari: ")
			fmt.Scanln(&r)
			fmt.Println("keliling lingkaran =", kelilinglingkaran(r))
		} else if a == 3 {
			fmt.Print("Inputkan Jari-Jari: ")
			fmt.Scanln(&r)
			fmt.Println("volume bola =", volumebola(r))
		} else if a == 4 {
			fmt.Println("keluar dari program")
			break
		} else {
			fmt.Println("input tidak valid")
		}
		fmt.Println()
		fmt.Println("Kembali ke menu utama?")
		fmt.Println("1. Ya")
		fmt.Println("2. Tidak")
		fmt.Scanln(&b)
		if b == 2 {
			break
		} else {
			continue
		}
	}
}
