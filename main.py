import random
from game_data import data
from replit import clear
from art import logo, vs
  
def compare(A,B):
  if A["follower_count"] > B["follower_count"]:
    return "A"
  if A["follower_count"] < B["follower_count"]:
    return "B"

def return_account(account, A, B):
  if account == "A":
    return A
  elif account == "B":
    return B

score = 0

def instagram():
  print(logo)
  A = random.choice(data)
  print("Compare A: {}, a {}, from {}".format(A["name"], A["description"], A["country"]))

  continuation = True
  score = 0

  while continuation == True:
    print(vs)
    B = random.choice(data)
    print("Against B: {}, a {}, from {}".format(B["name"], B["description"], B["country"]))
    answer = input("Who has more followers? Type 'A' or 'B': ")
    clear()
    if answer == compare(A,B):
      score += 1
      print("You're right! Current score: {}.".format(score))
      replace = return_account(answer, A, B)
      print("Compare A: {}, a {}, from {}".format(replace["name"], replace["description"], replace["country"]))
    else:
      print("Sorry, that's wrong. Final score: {}".format(score))
      continuation = False
      
instagram()

