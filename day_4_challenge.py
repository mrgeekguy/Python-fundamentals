# Fix the code


def calculate_savings(prev_price, current_price, amount, tax):
    """
    Function's purpose is to calculate and report savings on a purchase

    prev_price      (float number describing the price before savings)
    current_price   (float number describing the price at purchasing)
    amount          (int number denoting how many were purchased)
    tax             (float number describing the state's tax percentage)

    This function should return a float number describing how much was saved
    or a string stating "no savings occured"
    """
    tax_percentage = 1 + tax

    previous_total = (prev_price * amount) * tax_percentage
    current_total = (current_price) * amount * tax_percentage

    savings = previous_total - current_total

    return savings if savings > 0 else "No savings occured"

print(calculate_savings(30, 50, 2, -0.08))

# ----------------------------------------------------------

contracted_items = [
   {
      "id": "A001",
      "name": "Daisy Paper Plates",
      "price": 3.99
   },
   {
      "id": "A002",
      "name": "Solo Red Cups",
      "price": 2.00
   },
   {
      "id": "A199",
      "name": "Dixie Paper Towels",
      "price": 4.50
   }
]


purchased_items = [
   {
      "id": "A088",
      "count": 32,
      "price": 4.88
   },
   {
      "id": "A002",
      "count": 29,
      "price": 3.40
   },
   {
      "id": "A199",
      "count": 2,
      "price": 8.90
   },
   {
      "id": "A332",
      "count": 78,
      "price": 22.78
   },
   {
      "id": "A001",
      "count": 10,
      "price": 3.99
   }
]

