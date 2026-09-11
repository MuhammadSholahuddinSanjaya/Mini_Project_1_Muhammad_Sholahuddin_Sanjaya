Jadwal_Pertandingan = []

while True :
    print("Sistem Pendataan Jadwal Pertandingan Sepakbola")
    print("1. Tambahkan jadwal pertandingan sepakbola dengan format: Nama Pertandingan, Nama Liga, Waktu Pertandingan (dd/mm/yyyy hh:mm)")
    print("2. Tampilkan daftar jadwal pertandingan sepakbola yang telah dimasukkan")
    print("3. Ubah jadwal pertandingan sepakbola yang salah diinputkan")
    print("4. Hapus jadwal pertandingan sepakbola yang salah diinputkan")
    print("5. Ketik 'Selesai' untuk mengakhiri input jadwal pertandingan sepakbola")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        print("Tambah Jadwal Pertandingan")
        pertandingan = input("Nama Pertandingan: ")
        liga = input("Nama Liga: ")
        waktu = input("Waktu Pertandingan dengan format (dd/mm/yyyy hh:mm) : ")

        data_baru = (pertandingan, liga, waktu)
        Jadwal_Pertandingan.append(data_baru)
        print("Jadwal pertandingan berhasil ditambahkan")

    elif pilihan == "2":
        print("Daftar Jadwal Pertandingan Sepakbola")
        if not Jadwal_Pertandingan:
            print("Belum ada data jadwal pertandingan yang tersimpan.")
        else:
            nomor = 1
            for item in Jadwal_Pertandingan:
                print(f"{nomor}  {item[0]}  {item[1]} {item[2]}")
                nomor += 1

    elif pilihan == "3":
        print("Ubah Jadwal Pertandingan")
        if not Jadwal_Pertandingan:
            print("Tidak ada data jadwal yang dapat diubah.")
        else:
            print("Daftar Jadwal Pertandingan Sepakbola")
            nomor = 1
            for item in Jadwal_Pertandingan:
                print(f"{nomor}  {item[0]}  {item[1]} {item[2]}")
                nomor += 1

            idx_input = input("Masukkan nomor data yang ingin diubah: ")
            idx = int(idx_input) - 1

            pertandingan_baru = input("Masukkan Nama Pertandingan Baru: ")
            liga_baru = input("Masukkan Nama Liga Baru: ")
            waktu_baru = input("Masukkan Waktu Pertandingan Baru: ")

            Jadwal_Pertandingan[idx] = (pertandingan_baru, liga_baru, waktu_baru)
            print("Data jadwal pertandingan berhasil diubah.")

    elif pilihan == "4":
        print("Hapus Jadwal Pertandingan")
        if not Jadwal_Pertandingan:
            print("Tidak ada data jadwal yang dapat dihapus.")
        else:
            print("Daftar Jadwal Pertandingan Sepakbola")
            nomor = 1
            for item in Jadwal_Pertandingan:
                print(f"{nomor}  {item[0]}  {item[1]} {item[2]}")
                nomor += 1

            idx_input = input("Masukkan nomor data yang ingin dihapus: ")
            del Jadwal_Pertandingan[int(idx_input) - 1]
            print("Data jadwal pertandingan berhasil dihapus.")

    elif pilihan == "5":
        print("Input Jadwal Pertandingan Sepakbola Selesai")
        break

    else :
        print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")
        