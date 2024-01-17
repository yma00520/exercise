flower_bulb_prices = {
    "daffodil": 0.35,
    "tulip": 0.33,
    "hyacinth": 0.75,
    "crocus": 0.25,
    "bluebell": 0.50,
}

mary_purchase_order = {"daffodil": 50, "tulip": 100}

def print_purchase_order(purchase_order):
    print("You have purchased the following bulbs:")
    total_quantity = 0
    total = 0
    for bulb_name, bulb_quantity in sorted(purchase_order.items()):
        bulb_code = bulb_name[:3].upper()
        bulb_price = flower_bulb_prices[bulb_name]
        subtotal = round(bulb_price * bulb_quantity, 2)

        total_quantity += bulb_quantity
        total += subtotal
        print(f"{bulb_code:<5} *{bulb_quantity:>4} = ${subtotal:>6.2f}")
    print(
        f"\nThank you for purchasing {total_quantity} bulbs from Bluebell Greenhouses.\nYour total comes to ${total:>6.2f}."
    )


def main():
    flower_bulb_prices["tulip"] = round(flower_bulb_prices["tulip"] * (1 + 0.25), 2)

    mary_purchase_order["hyacinth"] = 30

    print_purchase_order(mary_purchase_order)

if __name__ == "__main__":
    main()
