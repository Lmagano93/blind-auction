from replit import clear
from art import logo

print(logo)


bidding_finished = False
bids = {}

# def find_higher_bid(bidding_record):
#    #bidding_record is a um funcao local, só está despinivel dentro da função, bem como bidder, ou seja são criados para o for loop. 
#   highest_bid = 0
#   winner = ""
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder] #buscar valores de todos os bids
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")




while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your Bid?"))
    bids[name] = price

    choice = input("Do you want to continue biding? Type yes or no\n")
    if choice == "no":
      bidding_finished = True
      find_highest_bidder(bids)
      
      
    elif choice =="yes":
     clear()

    else:
      biding = False
      print("game over")





