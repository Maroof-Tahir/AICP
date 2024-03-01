class Item:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.highest_bid = 0
        self.num_bids = 0

    def place_bid(self, bid_amount):
        if bid_amount > self.highest_bid:
            self.highest_bid = bid_amount
            self.num_bids += 1
            print("Bid placed successfully.")
        else:
            print("Bid amount must be higher than the current highest bid.")

    def __str__(self):
        return f"Item Number: {self.item_number}\nDescription: {self.description}\nHighest Bid: {self.highest_bid}\n"


class Auction:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        for item in self.items:
            print(item)

    def end_auction(self):
        total_fee = 0
        items_sold = 0
        items_not_meeting_reserve = 0
        items_with_no_bids = 0

        print("\nAuction Results:")

        for item in self.items:
            if item.highest_bid >= item.reserve_price:
                items_sold += 1
                total_fee += 0.1 * item.highest_bid
                print(f"Item {item.item_number} sold for {item.highest_bid}.")
            else:
                items_not_meeting_reserve += 1
                print(f"Item {item.item_number} did not meet reserve price.")

            if item.num_bids == 0:
                items_with_no_bids += 1
                print(f"Item {item.item_number} received no bids.")

        print(f"\nTotal fee for sold items: {total_fee}")
        print(f"Items sold: {items_sold}")
        print(f"Items not meeting reserve price: {items_not_meeting_reserve}")
        print(f"Items with no bids: {items_with_no_bids}")


def main():
    auction = Auction()

    # Task 1 - Auction set up
    print("Task 1 - Auction set up")
    num_items = int(input("Enter the number of items in the auction (must be at least 10): "))
    if num_items < 10:
        print("Error: The number of items must be at least 10.")
        return

    for i in range(1, num_items + 1):
        item_number = input(f"Enter item {i} number: ")
        description = input(f"Enter item {i} description: ")
        reserve_price = float(input(f"Enter reserve price for item {i}: "))
        item = Item(item_number, description, reserve_price)
        auction.add_item(item)

    # Task 2 - Buyer bids
    print("\nTask 2 - Buyer bids")
    while True:
        try:
            item_number = input("Enter the item number you want to bid on (or 'quit' to end): ")
            if item_number.lower() == 'quit':
                break

            found = False
            for item in auction.items:
                if item.item_number == item_number:
                    found = True
                    print(item)
                    bid_amount = float(input("Enter your bid amount: "))
                    item.place_bid(bid_amount)
                    break

            if not found:
                print("Item not found.")
        except ValueError:
            print("Invalid input. Please enter a valid bid amount.")

    # Task 3 - At the end of the auction
    print("\nTask 3 - At the end of the auction")
    auction.end_auction()


if __name__ == "__main__":
    main()
