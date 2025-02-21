votes = {}
invalid_voters = set()
 
while True:
    line = input().strip()
    if line == "0 0":
        break
    
    voter, candidate = map(int, line.split())
    
    if voter in votes:
        invalid_voters.add(voter)
    votes[voter] = candidate
 
valid_votes = {}
for voter, candidate in votes.items():
    if voter not in invalid_voters:
        valid_votes[candidate] = valid_votes.get(candidate, 0) + 1
 
sorted_results = sorted(valid_votes.items(), key=lambda x: (-x[1], -x[0]))
 
for candidate, count in sorted_results:
    print(candidate, count)