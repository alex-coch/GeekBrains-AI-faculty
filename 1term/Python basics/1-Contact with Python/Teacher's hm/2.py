time = int(input("Введите время в секундах - "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")


# time = int(input("Введите время в секундах"))
# hours = time // 3600
# minutes = time / 60
# seconds = minutes / 60
# print(f"{hours:02}:{minutes % 60:02}:{seconds % 60:02}")

