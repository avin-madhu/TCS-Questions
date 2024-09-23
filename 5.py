# total cost of joining arrays
wires = [4,3,2,6,7]
total_cost = 0

while len(wires)!=1:
    min_sum = float('inf')
    for i in range(len(wires)-1):
        if wires[i]+wires[i+1] <  min_sum:
            pos = i
            min_sum = wires[i] + wires[i+1]
    wires[pos] = wires[pos] + wires[pos+1]
    total_cost += wires[pos]
    wires = wires[:pos+1] + wires[pos+2:]
    wires.sort()

print(total_cost)
    