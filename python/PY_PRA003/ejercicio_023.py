def domino():
    ficha_max = 6
    ficha_min = 0
    while ficha_min <= 6:
        for ficha in range(ficha_max+1):
            print(f"[{ficha_max} | {ficha_min}",  end='] ')
            
            if ficha_max == ficha_min:
                break
            ficha_max-=1
        print("")
        ficha_max = 6
        ficha_min += 1
        

domino()