## program to take input from users and add it into Dicttionary

Bid_Dict =  {}
flag = True

while flag:
    Name_person =  input("Name of the bidder -  " )
    amount = int(input("Amount to bid $ "))
    Bid_Dict [Name_person] =  amount
    continue_flag = input("Do you want to continue 'Yes' or No")
    if continue_flag == 'No':
        flag =  False
    print(Bid_Dict)

    ## Bid winner
Winner_name = ""
max_amount = 0
for name in Bid_Dict:
    if   Bid_Dict[name] > max_amount:
        max_amount = Bid_Dict[name]
        Winner_name=name
print(f"So the winner is - {Winner_name}  has bid with amount - {max_amount}")

