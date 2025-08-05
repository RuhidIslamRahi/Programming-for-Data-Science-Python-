products = [
{"id": 1, "name": "Laptop", "price": 1200, "category": "Electronics"},
{"id": 2, "name": "Smartphone", "price": 800, "category": "Electronics"},
{"id": 3, "name": "Headphones", "price": 150, "category": "Electronics"},
{"id": 4, "name": "Sofa", "price": 700, "category": "Furniture"},
{"id": 5, "name": "Table", "price": 300, "category": "Furniture"}
]

def findExpensiveProducts(products, threshold):
    expensive_products = []
    for product in products:
        if product["price"] >= threshold:
            expensive_products.append(product["name"])
    return expensive_products

def getAveragePrice(products):
    total = 0
    count = 0
    for product in products:
        total += product["price"]
        count += 1
    return total / count

def groupProductsByCategory(products):
    categories = {}
    for product in products:
        category = product["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(product["name"])
    return categories

def getUniquePrices(products):
    unique_prices = set()
    for product in products:
        unique_prices.add(product["price"])
    return unique_prices



threshold = 500
print("Expensive Products:", findExpensiveProducts(products, threshold))
print("Average Price:", getAveragePrice(products))
print("Products Grouped by Category:", groupProductsByCategory(products))
print("Unique Prices:", getUniquePrices(products))