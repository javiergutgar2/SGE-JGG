def romper_h(palabra):
    for letra in palabra:
        if letra == "h":
            print("Lo rompiste")
            break
        else:
            print(f"{letra}")

palabra = input("introduce una palabra sin h porfi: ")
romper_h(palabra)