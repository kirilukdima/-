def format_price(price: float) -> str:
    return f"ціна: {price:.2f} грн"


def check_availability(*products) -> dict:

    availability = {
        "хліб": True,
        "молоко": True,
        "сир": False,
        "яблуко": True,
        "шоколад": False,
    }
    return {product: availability.get(product, False) for product in products}


def make_order(order: list, action: str):
    prices = {
        "хліб": 25.5,
        "молоко": 32,
        "сир": 120,
        "яблуко": 15.75,
        "шоколад": 55,
    }

    availability = check_availability(*order)

    if not all(availability.values()):
        print("⚠️ Замовлення неможливе, бо деякі товари відсутні:")
        for product, avail in availability.items():
            if not avail:
                print(f"❌ {product}")
        return

    total = sum(prices[product] for product in order)

    if action == "ціна":
        print("💰 Загальна вартість замовлення:")
        for product in order:
            print(f"{product}: {format_price(prices[product])}")
        print("Разом:", format_price(total))

    elif action == "купити":
        print("✅ Ви успішно придбали товари:")
        for product in order:
            print(f"   - {product}: {format_price(prices[product])}")
        print("Загальна сума:", format_price(total))

    else:
        print("⚠️ Невідома дія! Використовуйте 'ціна' або 'купити'.")


print("🛒 Вітаємо у магазині!")
print("Доступні товари: хліб, молоко, сир, яблуко, шоколад")

while True:
    action = input("\nВведіть дію ('ціна', 'купити' або 'stop'): ").lower()
    if action == "stop":
        print("👋 Дякуємо за відвідування!")
        break

    order = input("Введіть товари через кому: ").lower().split(",")
    order = [item.strip() for item in order]

    make_order(order, action)
