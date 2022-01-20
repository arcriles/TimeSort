print("gunakan . atau , untuk membedakan menit dan detik")

waktu = []
while True:
    durasi = input()
    if race_time == "DONE":
        break
    waktu.append(float(durasi))
print(min(waktu))