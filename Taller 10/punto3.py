M = int(input().strip())
ticket_counts = {}
winning_numbers = []
prizes = []

while True:
    line = input().strip()
    if line == "end":
        break
    
    parts = line.split()
    action, number = parts[0], int(parts[1])
    
    if action == "sms":
        ticket_counts[number] = ticket_counts.get(number, 0) + 1
    elif action == "winner":
        winning_numbers.append(number)
        
        if number in ticket_counts:
            G = len(winning_numbers)
            C = ticket_counts[number]
            prize = M // (G * C)
            prizes.append((number, prize))

if prizes:
    for number, prize in prizes:
        print(number, prize)
else:
    print(0)
