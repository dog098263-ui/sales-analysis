import csv
import random
import os
from datetime import datetime, timedelta

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generate_ecommerce_data():
    random.seed(42)  # For reproducibility
    output_dir = "/Users/meow/.gemini/antigravity/scratch/powerbi_portfolio/data"
    create_directory(output_dir)

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2026, 6, 30)
    delta_days = (end_date - start_date).days

    # --- 1. Products (DimProduct) ---
    # Relational ID, Name, Category, Subcategory, UnitPrice, ProductCost
    product_templates = [
        # Electronics
        ("Prod_E01", "Optima 4K Monitor", "Electronics", "Monitors", 350.00, 210.00),
        ("Prod_E02", "Apex Wireless Mouse", "Electronics", "Accessories", 49.99, 18.00),
        ("Prod_E03", "Apex Mechanical Keyboard", "Electronics", "Accessories", 120.00, 55.00),
        ("Prod_E04", "Quantum Noise Cancelling Headphones", "Electronics", "Audio", 250.00, 110.00),
        ("Prod_E05", "Bolt USB-C Hub", "Electronics", "Accessories", 39.99, 12.00),
        # Apparel
        ("Prod_A01", "Classic Cotton Tee", "Apparel", "Shirts", 25.00, 8.00),
        ("Prod_A02", "Urban Denim Jacket", "Apparel", "Outerwear", 85.00, 32.00),
        ("Prod_A03", "Athletic Fleece Joggers", "Apparel", "Pants", 45.00, 16.00),
        ("Prod_A04", "Wool Knit Beanie", "Apparel", "Accessories", 19.99, 6.00),
        ("Prod_A05", "All-Weather Windbreaker", "Apparel", "Outerwear", 75.00, 28.00),
        # Home & Kitchen
        ("Prod_H01", "Gourmet Drip Coffee Maker", "Home", "Kitchen", 89.99, 38.00),
        ("Prod_H02", "Ergonomic Memory Foam Pillow", "Home", "Bedroom", 59.99, 22.00),
        ("Prod_H03", "Smart LED Desk Lamp", "Home", "Lighting", 45.00, 18.00),
        ("Prod_H04", "Vacuum Insulated Water Bottle", "Home", "Kitchen", 29.99, 9.00),
        # Beauty & Personal Care
        ("Prod_B01", "Hydrating Facial Serum", "Beauty", "Skincare", 35.00, 10.00),
        ("Prod_B02", "Organic Lavender Body Wash", "Beauty", "Bath", 18.50, 5.00),
        ("Prod_B03", "Sonic Electric Toothbrush", "Beauty", "Oral Care", 79.99, 30.00)
    ]

    # Write Products (clean, but will introduce some category casing issues in script to clean in Power BI)
    products_file = os.path.join(output_dir, "products.csv")
    with open(products_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ProductID", "ProductName", "Category", "SubCategory", "UnitPrice", "ProductCost"])
        for pid, name, cat, subcat, price, cost in product_templates:
            # Introduce casing dirty data (e.g. electronics vs Electronics)
            dirty_cat = cat.lower() if random.random() < 0.15 else cat
            writer.writerow([pid, name, dirty_cat, subcat, price, cost])

    # --- 2. Geography (DimGeography) ---
    geo_templates = [
        ("10001", "New York", "NY", "East"),
        ("90001", "Los Angeles", "CA", "West"),
        ("60601", "Chicago", "IL", "Midwest"),
        ("77001", "Houston", "TX", "South"),
        ("33101", "Miami", "FL", "South"),
        ("98101", "Seattle", "WA", "West"),
        ("02101", "Boston", "MA", "East"),
        ("30301", "Atlanta", "GA", "South"),
        ("80201", "Denver", "CO", "West"),
        ("60101", "Minneapolis", "MN", "Midwest")
    ]
    geography_file = os.path.join(output_dir, "geography.csv")
    with open(geography_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["PostalCode", "City", "State", "Region"])
        for post, city, state, reg in geo_templates:
            writer.writerow([post, city, state, reg])

    # --- 3. Customers (DimCustomer) ---
    first_names = ["John", "Mary", "Robert", "Patricia", "Michael", "Jennifer", "David", "Elizabeth", "William", "Linda", 
                   "Richard", "Barbara", "Joseph", "Susan", "Thomas", "Jessica", "Charles", "Sarah", "Christopher", "Karen"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                  "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
    segments = ["Standard", "Premium", "Basic"]

    customers = []
    num_customers = 500
    for i in range(1, num_customers + 1):
        cid = f"CUST_{i:04d}"
        fname = random.choice(first_names)
        lname = random.choice(last_names)
        
        # Introduce dirty data in CustomerName (trailing spaces, lowercase)
        name_type = random.random()
        if name_type < 0.1:
            name = f" {fname} {lname} "
        elif name_type < 0.15:
            name = f"{fname} {lname}".lower()
        else:
            name = f"{fname} {lname}"

        # Segment with typos and spaces
        seg = random.choice(segments)
        if seg == "Premium" and random.random() < 0.2:
            seg = "premiuum"  # Typo
        elif seg == "Standard" and random.random() < 0.2:
            seg = "Standard   "  # Spaces
        elif random.random() < 0.05:
            seg = ""  # Null/Empty

        # Dates: customer signup date between 2024-01-01 and 2025-12-31
        signup_offset = random.randint(0, 730)
        signup_dt = start_date + timedelta(days=signup_offset)
        signup_date_str = signup_dt.strftime("%Y-%m-%d")

        email = f"{fname.lower()}.{lname.lower()}@example.com" if random.random() > 0.05 else ""
        gender = random.choice(["M", "F"])
        postal = random.choice(geo_templates)[0]

        customers.append((cid, name, seg, signup_dt, signup_date_str, email, gender, postal))

    # Write Customers with duplicate rows to clean in Power BI
    customers_file = os.path.join(output_dir, "customers.csv")
    with open(customers_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["CustomerID", "CustomerName", "Segment", "SignupDate", "Email", "Gender", "PostalCode"])
        
        # Write customers, occasionally duplicate records
        for cid, name, seg, _, signup_str, email, gender, postal in customers:
            writer.writerow([cid, name, seg, signup_str, email, gender, postal])
            if cid in ["CUST_0012", "CUST_0045", "CUST_0233"] and random.random() < 0.8:
                # Add duplicate rows
                writer.writerow([cid, name, seg, signup_str, email, gender, postal])

    # --- 4. Orders (FactOrders) & Deliveries (FactDeliveries) ---
    orders = []
    deliveries = []
    order_id_counter = 10001
    
    # Establish a "churn" cohort: Customers with IDs ending in 0 or 5 will stop buying after their signup + 120 days.
    # Customers with premium segments or from NY/CA buy more frequently.
    carriers = ["FedEx", "UPS", "DHL"]

    for cid, name, seg, signup_dt, _, email, gender, postal in customers:
        # Check if customer churns early (stops ordering)
        is_churner = (int(cid.split("_")[1]) % 5 == 0) # 20% of customers are churners

        current_date = signup_dt + timedelta(days=random.randint(1, 10))
        customer_orders_count = 0
        
        while current_date < end_date:
            if is_churner and (current_date - signup_dt).days > 120:
                # Churner stops ordering after 120 days
                break

            # Frequency: regular users order every 30-90 days, churners order less, premium order more
            if seg == "Premium":
                interval = random.randint(15, 45)
            elif is_churner:
                interval = random.randint(45, 120)
            else:
                interval = random.randint(30, 90)

            current_date += timedelta(days=interval)
            if current_date >= end_date:
                break

            # Create an Order
            oid = f"ORD_{order_id_counter}"
            order_id_counter += 1
            customer_orders_count += 1

            # Select 1 to 3 items per order
            items_count = random.randint(1, 3)
            selected_products = random.sample(product_templates, items_count)

            order_date_str = current_date.strftime("%Y-%m-%d")

            for prod in selected_products:
                pid, pname, pcat, psubcat, unit_price, prod_cost = prod
                qty = random.randint(1, 4)
                
                # Apply discount to some orders
                discount = 0.0
                if random.random() < 0.3:
                    discount = round(random.choice([0.05, 0.10, 0.15, 0.20]), 2)

                # Total revenue = qty * unit_price * (1 - discount)
                revenue = round(qty * unit_price * (1 - discount), 2)

                # Introduce dirty data: A small fraction of orders have negative or null quantities to clean
                if random.random() < 0.005:
                    qty = -1  # Return/refund simulation
                    revenue = -round(unit_price * (1 - discount), 2)
                
                orders.append((oid, cid, order_date_str, pid, qty, discount, revenue, postal))

            # Deliveries: created per order ID
            # Let's say shipping carrier performance is tracked here
            ship_days = random.randint(1, 3)
            ship_date = current_date + timedelta(days=ship_days)
            ship_date_str = ship_date.strftime("%Y-%m-%d")

            # Shipping duration: normal is 2-5 days. Let's make carrier DHL have shipping delays in early 2025.
            delivery_status = "Delivered"
            carrier = random.choice(carriers)
            
            # Shipping delay simulation
            delay_prob = random.random()
            if carrier == "DHL" and current_date.year == 2025 and current_date.month in [3, 4, 5]:
                # Shipping logistics issue at DHL
                delivery_days = random.randint(8, 18)
            else:
                delivery_days = random.randint(2, 6)

            delivery_dt = ship_date + timedelta(days=delivery_days)
            
            # Pending/lost shipments: delivery date is blank
            if delay_prob < 0.02:
                delivery_date_str = ""  # Still pending / lost
                delivery_status = "In Transit" if delay_prob < 0.005 else "Lost"
            else:
                delivery_date_str = delivery_dt.strftime("%Y-%m-%d")
                delivery_status = "Delivered"
                
                # Introduce returned items (causes customer dissatisfaction)
                if delay_days > 7 and random.random() < 0.4:
                    delivery_status = "Returned"

            # Carrier spelling errors
            dirty_carrier = carrier
            if carrier == "UPS" and random.random() < 0.15:
                dirty_carrier = " u.p.s. "
            elif carrier == "FedEx" and random.random() < 0.15:
                dirty_carrier = "fedex"

            shipping_cost = round(random.uniform(5.00, 25.00), 2)

            # Introduce another dirty data: Ship date BEFORE order date (impossible)
            if random.random() < 0.005:
                ship_date_str = (current_date - timedelta(days=2)).strftime("%Y-%m-%d")

            deliveries.append((oid, ship_date_str, delivery_date_str, dirty_carrier, delivery_status, shipping_cost))

    # Write Orders
    orders_file = os.path.join(output_dir, "orders.csv")
    with open(orders_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["OrderID", "CustomerID", "OrderDate", "ProductID", "Quantity", "Discount", "SalesAmount", "PostalCode"])
        for row in orders:
            writer.writerow(row)

    # Write Deliveries
    deliveries_file = os.path.join(output_dir, "deliveries.csv")
    with open(deliveries_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["OrderID", "ShipDate", "DeliveryDate", "Carrier", "DeliveryStatus", "ShippingCost"])
        for row in deliveries:
            writer.writerow(row)

    print(f"Data generation complete!")
    print(f"Products written: {len(product_templates)}")
    print(f"Geography written: {len(geo_templates)}")
    print(f"Customers written: {len(customers)}")
    print(f"Order items written: {len(orders)}")
    print(f"Deliveries written: {len(deliveries)}")

if __name__ == "__main__":
    generate_ecommerce_data()
