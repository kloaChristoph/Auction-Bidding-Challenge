def auction(initial_price: str, bids: list):
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

        to_add = f",{highest_bidder},{price}"
        if last_added_history != to_add:
            history = history + to_add

        last_added_history = f",{highest_bidder},{price}"

    print(history)
 

if __name__ == "__main__":
    auction_input = [1,"A",5,"B",10,"A",8,"A",14,"A",17,"B",17]
    auction_input = [100,"A",100,"A",115,"A",119,"A",144,"A",145,"A",157,"A",158,"A",171,"A",179,"A",194,"A",206,"A",207,"A",227,"A",229,"A",231,"A",234]
    auction_input = [100,"C",100,"C",115,"C",119,"C",121,"C",144,"C",154,"C",157,"G",158,"C",171,"C",179,"C",194,"C",206,"C",214,"C",227,"C",229,"C",231,"C",298]
    auction_input = [1,"nepper",15,"hamster",24,"philipp",30,"mmautne",31,"hamster",49,"hamster",55,"thebenil",57,"fliegimandi",59,"ev",61,"philipp",64,"philipp",65,"ev",74,"philipp",69,"philipp",71,"fliegimandi",78,"hamster",78,"mio",95,"hamster",103,"macquereauxpl",135]
    auction_input = [15,"urtyp",15]
    auction_input = [1,"rx",50,"aa",2000,"de",3558,"einseins",3999,"ek",4999,"yd",8332,"lb",5000,"lb",6000,"lb",7000,"lb",8000,"lb",8999,"yd",9999,"zn",11000,"ir",11110,"nr",12999,"kt",12567,"kt",12667,"kt",13000,"go",14000,"ym",14999,"hm",15400,"nr",15690,"nr",17000,"td",18500,"kt",18750,"uy",18850,"hr",18999,"td",19049,"st",19200]

    auction(auction_input[0], auction_input[1:])
