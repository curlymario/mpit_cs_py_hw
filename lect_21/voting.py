votes = {}
N = int(input)
for i in range(N):
    name = input()
    if name in votes:           # код-гольф, в одну строчку, без if|else но хуже асимптотика (+ действие на удаление):
        votes[name] += 1        # D[name] = D.pop(name, 0) + 1
    else:
        votes[name] = 1

A = list(votes.items())

