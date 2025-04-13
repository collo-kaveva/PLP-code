def calculate_discount(price, discount_percent):
    """Calculate discounted price if discount is 20% or more"""
    if discount_percent >= 20:
        return price * (1 - discount_percent/100)
    return price

def main():
    print("Discount Calculator")
    print("-------------------")
    
    try:
        price = float(input("Enter item price ($): "))
        discount = float(input("Enter discount (%): "))
        
        if price < 0 or discount < 0:
            print("Error: Values cannot be negative")
            return
            
        final_price = calculate_discount(price, discount)
        
        if final_price < price:
            print(f"Discounted price: ${final_price:.2f}")
        else:
            print(f"No discount applied. Price: ${price:.2f}")
            
    except ValueError:
        print("Error: Please enter numbers only")

if __name__ == "__main__":
    main()