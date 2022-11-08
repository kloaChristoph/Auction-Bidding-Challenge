def auction(initial_price: str, buy_now:int, bids: list):
    bidder: str = ""
    bid: int = 0
    price: int = 1
    highest_bidder: str = ""
    history: str = f"-,{initial_price}"
    last_added_history: str = ""
    
    bid = initial_price
    highest_bidder = bids[0]

    while bids:
        bidder = bids[0]
        new_bid = bids[1]

        if new_bid > bid and bidder == highest_bidder:
            bid = new_bid
        
        elif new_bid > bid:
            highest_bidder = bidder
            price = bid + 1
            bid = new_bid
            
        elif new_bid < bid:
            price = new_bid + 1 
            
        elif new_bid == bid:    
            price = bid
            
        bids.pop(0)
        bids.pop(0)

        if price >= buy_now and buy_now != 0:
            price = buy_now
            to_add = f",{highest_bidder},{price}"
            history = history + to_add
            break
        
        to_add = f",{highest_bidder},{price}"
        if last_added_history != to_add:
            history = history + to_add

        last_added_history = f",{highest_bidder},{price}"
        
    print(history)

if __name__ == "__main__":
    auction_input = [1,15,"A",5,"B",10,"A",8,"A",17,"B",17]
    auction_input = [100,0,"C",100,"C",115,"C",119,"C",121,"C",144,"C",154,"C",157,"G",158,"C",171,"C",179,"C",194,"C",206,"C",214,"C",227,"C",229,"C",231,"C",298]
    auction_input = [100,325,"C",100,"C",115,"C",119,"C",121,"C",144,"C",154,"C",157,"G",158,"C",171,"C",179,"C",194,"C",206,"C",214,"C",227,"C",229,"C",231,"C",298]
    auction_input = [100,160,"C",100,"C",115,"C",119,"C",121,"C",144,"C",154,"C",157,"G",158,"C",171,"C",179,"C",194,"C",206,"C",214,"C",227,"C",229,"C",231,"C",298]
    auction_input = [1,0,"nepper",15,"hamster",24,"philipp",30,"mmautne",31,"hamster",49,"hamster",55,"thebenil",57,"fliegimandi",59,"ev",61,"philipp",64,"philipp",65,"ev",74,"philipp",69,"philipp",71,"fliegimandi",78,"hamster",78,"mio",95,"hamster",103,"macquereauxpl",135]
    auction_input = [1,120,"6a",17,"kl",5,"kl",10,"kl",15,"cs",28,"kl",20,"kl",25,"hr",35,"hr",40,"hr",41,"hl",42,"hr",43,"hr",44,"hl",44,"hl",49,"hr",47]
    auction_input = [1,47,"6a",17,"kl",5,"kl",10,"kl",15,"cs",28,"kl",20,"kl",25,"hr",35,"hr",40,"hr",41,"hl",42,"hr",43,"hr",44,"hl",44,"hl",49,"hr",47]

    auction(auction_input[0], auction_input[1], auction_input[2:])
