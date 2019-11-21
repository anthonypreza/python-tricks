def discount(product, discount):
    price = int(product["price"]) * (1.0 - discount)
    assert 0 <= price <= product["price"]
    return price


shoes = {"name": "Fancy shoes", "price": 14900}

if __name__ == "__main__":
    print(f"25% discount on shoes: {discount(shoes, 0.25)}")
    print(f"200% discount on shoes {discount(shoes, 2.0)}")
"""
NOTES
- debugging aid, internal self-check in program
- only to help identify bugs, not for handling run-time errors
- globally disabled with -o apparently, so assertions can be skipped
- do not use for data validation
- assertion of a tuple will always evaluate to True
"""
