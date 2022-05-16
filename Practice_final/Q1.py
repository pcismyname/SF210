def main():
  election("Votes1.txt")
  election("Votes2.txt")
  election("Votes3.txt")
  # read file
  # loop through each line
  #     compute winner and votes recieve for each line
  #     compute numbers of candidates from the first line
  # compare votes to find overall winner


def election(filename):
  with open(filename) as input:
    votes = getvotes(input.readlines())
    findwinner(votes)

def getvotes(lines):
  num_candidates = len(lines[0].split()) - 2
  votes = [0] * num_candidates
  for line in lines:
    data = line.split()
    winner = getwinner(data[1:-1])
    votes[winner] += int(data[-1])
  return votes


def getwinner(votes):
  votes = [int(x) for x in votes]
  return votes.index(max(votes))

def findwinner(votes):
  winner = getwinner(votes)
  for i in range(len(votes)):
    print(f"Candidate {i+1}: {votes[i]} votes")

  print(f"The winner is candidate {winner+1}")

main()