

symbols = []
descriptions = []
output = []
stock_pick = "Stock_Pick"

f = open("NYSE.txt", "r")
wf = open("NYSE_imports.txt", "w")

for line in f:
    line = line.partition("\t")

    symbols.append(str(line[0]))
    descriptions.append(str(line[2]))
f.close()

for idx, (x, y) in enumerate(zip(symbols, descriptions)):
    symbol = symbols[idx].strip()
    description = descriptions[idx].strip()

    wf.write(
        f'{stock_pick}(symbol = {symbol}, description = {description}).save()\n')


wf.close
