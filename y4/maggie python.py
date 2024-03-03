def zisti(zoznam):
    ulozim= zoznam
    slovo_s_najmensou_hodnotou =''
    for i in range((zoznam.count(', ')+1)):
        if ', ' in zoznam:
            terajsie_slovo = zoznam[:zoznam.find(', ')]
        else:
            terajsie_slovo = zoznam
        if i == 0:
            slovo_s_najmensou_hodnotou= terajsie_slovo
        elif sucet(terajsie_slovo) < sucet(slovo_s_najmensou_hodnotou):
            slovo_s_najmensou_hodnotou= terajsie_slovo
        zoznam = zoznam[zoznam.find(', ')+2:]
    print(f'{slovo_s_najmensou_hodnotou}-{sucet(slovo_s_najmensou_hodnotou)}')

def sucet(slovo):
    celkovy_sucet = 0
    slovo = slovo.lower()
    for i in range(len(slovo)-1):
        prve = slovo[i]
        druhe = slovo[i+1] 
        celkovy_sucet += abs(ord(druhe)-ord(prve))-1
    return celkovy_sucet

zisti("Adolf, Gregor, Filip, Natalia")
zisti("jednotka, Prepadnem, string, GBAS, abeceda")
