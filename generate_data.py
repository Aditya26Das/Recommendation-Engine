import random
import pandas as pd

# Sample tags and categories
tags_pool = ["floral", "summer", "pastel", "denim", "casual", "boho", "formal", "classic", 
             "sports", "shoes", "comfort", "leather", "bag", "tank", "winter", "wool", 
             "warm", "jeans", "crop", "maxi"]

categories = ["dresses", "jackets", "skirts", "tops", "footwear", "accessories", "bottoms"]

# Function to generate a random product row
def generate_product(product_id):
    title = f"Product {product_id}"
    tags = ",".join(random.sample(tags_pool, k=random.randint(2, 4)))
    category = random.choice(categories)
    popularity_score = random.randint(50, 100)
    return {
        "product_id": product_id,
        "title": title,
        "tags": tags,
        "category": category,
        "popularity_score": popularity_score
    }

# Generate 1100 product entries
products = [generate_product(pid) for pid in range(1, 1101)]
products = sorted(products, key=lambda x: x['popularity_score'], reverse=True)
products_df = pd.DataFrame(products)

# Show a sample of the data
print(products_df)
products_df.to_csv("products.csv",index=False)


# Generate 200 rows of user interaction data
user_ids = [random.randint(1, 10) for _ in range(200)]  # Simulate 10 users
product_ids = [random.randint(1, 1100) for _ in range(200)]  # Products from 1 to 1100

user_interactions = pd.DataFrame({
    "user_id": user_ids,
    "product_id": product_ids
})

# Show a sample
print(user_interactions)
user_interactions.to_csv("users.csv",index=False)