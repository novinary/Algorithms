#!/usr/bin/python
# Iterative solution
import sys

def rock_paper_scissors(number):
  rps = [['rock'],['paper'],['scissors']]
  if number == 0:
    return [[]]
  elif number == 1:
    return rps
  else:
    count = 2
    plays={0:[[]],1:rps}
    while count<=number:
      last_play = plays[list(plays.keys())[-1]]
      plays[count] = []
      for i in range(len(last_play)):
        last_play_item=last_play[i][0:]
        last_play_item.append('rock')
        plays[count].append(last_play_item)
        last_play_item=last_play_item[0:-1]
        last_play_item.append('paper')
        plays[count].append(last_play_item)
        last_play_item=last_play_item[0:-1]
        last_play_item.append('scissors')
        plays[count].append(last_play_item)
      count+=1
  return plays[number]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')