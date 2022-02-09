# Codingame challenge
# INPUT:
# 1st line: number of people and number of following lines
# Next n lines: the person number and the vote

# Did everyone voted for everyone?

# Input:
# 3 6
# 1 2
# 1 3
# 2 3
# 2 1
# 3 1
# 3 2
# Output:
# "Clique"

(n_people, n_lines) = map(int, input().split())

d = dict()

for _ in range(n_lines):
    person, vote = map(int, input().split())
    if person in d.keys():
        d[person].append(vote)
    else:
        d[person] = [vote]
    d[person].append(person)

ok = True
keys = set(d.keys())
for elem in d.keys():
    voted = set(d[elem])
    if voted != keys:
        ok = False
        break

print("CLIQUE" if ok else "NOTHING TO SEE HERE")
