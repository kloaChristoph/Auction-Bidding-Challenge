def auction(initial_price: str, bids: list):
    bieter: str = ""
    bid: int = 0
    price: int = 0 
    highest_bidder: str = ""
    
    bid = initial_price
    highest_bidder = bids[0]

    while bids:
        bieter = bids[0]

        if bids[1] > bid:
            highest_bidder = bieter

            price = bid + 1

            bid = bids[1]
            
        elif bids[1] < bid:
            price = bids[1] + 1 
             
        elif bids[1] == bid:
            price = bid
        
        bids.pop(0)
        bids.pop(0)

    print(f"{highest_bidder},{price}")
 

if __name__ == "__main__":
    #auction_input = [1,"A",5,"B",10,"A",8,"A",17,"B",17]
    #auction_input = [1,"nepper",15,"hamster",24,"philipp",30,"mmautne",31,"hamster",49,"thebenil",57,"fliegimandi",59,"ev",61,"philipp",64,"ev",74,"philipp",69,"philipp",71,"fliegimandi",78,"hamster",78,"mio",95,"hamster",103,"macquereauxpl",135]
    #auction_input = [1,"cable",5,"ente",10,"karl",19,"moehe",14,"moehe",23,"michbex",24,"melloy",25,"achi",26]
    #auction_input = [1,"cable",5,"ente",10,"karl",19,"moehe",23,"michbex",24,"melloy",29,"achi",26]
    #auction_input = [15,"urtyp",17,"neuli",16,"schlurchi",25,"tokay",75,"horni",35,"sue",60,"sue",70]
    auction_input = [15,"urtyp",15]

    auction(auction_input[0], auction_input[1:])
