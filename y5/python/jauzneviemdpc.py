# Funkce pro ověření propojení zařízení
def can_connect_devices(room):
    connectors = {}
    
    for i in range(room['n']):
        y, x, c = room['devices'][i]
        
        if (y, x) not in connectors:
            connectors[(y, x)] = c
        elif connectors[(y, x)] != c:
            return "ajajaj"
    
    return "pujde to"

# Načtení vstupních dat ze souboru
with open("y5/python/input.txt", "r") as file:
    t = int(file.readline().strip())
    results = []

    for _ in range(t):
        h, w, n = map(int, file.readline().split())
        devices = []

        for _ in range(n):
            y, x, c = file.readline().split()
            devices.append((int(y), int(x), c))

        room = {'h': h, 'w': w, 'n': n, 'devices': devices}
        result = can_connect_devices(room)
        results.append(result)

# Uložení výstupu do souboru
with open("gptoutput.txt", "w") as output_file:
    for result in results:
        output_file.write(result + "\n")
