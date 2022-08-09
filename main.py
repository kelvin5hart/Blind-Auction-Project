from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

bid = True
bidders = {}
print(art.logo)
print("Welcome to secret auction program")
while bid:
  name = input("What is your name? ")
  money = int(input("What's your bid? $"))
  bidders[name] = money
  game = input("Are there any other bidders? Type 'yes' or 'no': ")
  if game == "no":
    bid = False
  clear()
    

highest_bid = 0
highest_bidder = ""
for bid in bidders:
  if bidders[bid] > highest_bid:
    highest_bid = bidders[bid]
    highest_bidder = bid

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
 
