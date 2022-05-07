rest_days = int(input())

year_norma = 30000
work_days = 365 - rest_days
norma_real = (rest_days * 127) + (work_days * 63)


if norma_real > 30000 :
    H = round(-(year_norma - norma_real) // 60, 0)
    M = abs((year_norma - norma_real) + (H * 60))
    print("Tom will run away")
    print(f"{H} hours and {M} minutes more for play")
else:
    H = round((year_norma - norma_real) // 60, 0)
    M = ((year_norma - norma_real) - (H * 60))
    print("Tom sleeps well")
    print(f"{H} hours and {M} minutes less for play")