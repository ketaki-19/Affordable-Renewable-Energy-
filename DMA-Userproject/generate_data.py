import os
import random
from datetime import date, timedelta
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

password = quote_plus(os.getenv('MYSQL_PASSWORD', ''))
engine = create_engine(
    f"mysql+mysqlconnector://{os.getenv('MYSQL_USER', 'root')}:{password}"
    f"@{os.getenv('MYSQL_HOST', 'localhost')}/{os.getenv('MYSQL_DATABASE', 'solshare')}"
)

# 6 Trade Scenarios with different pricing dynamics
TRADE_SCENARIOS = {
    1: {"name": "Peak Solar",         "price_multiplier": 1.2,  "energy_range": (50, 200)},
    2: {"name": "Off-Peak",           "price_multiplier": 0.8,  "energy_range": (20, 100)},
    3: {"name": "Storm Surplus",      "price_multiplier": 0.6,  "energy_range": (100, 300)},
    4: {"name": "High Demand",        "price_multiplier": 1.5,  "energy_range": (50, 150)},
    5: {"name": "Business Bulk",      "price_multiplier": 1.1,  "energy_range": (200, 500)},
    6: {"name": "Residential Micro",  "price_multiplier": 0.9,  "energy_range": (10, 60)},
}

BASE_PRICE_PER_KWH = 2.0
START_DATE = date(2023, 1, 1)
END_DATE   = date(2025, 10, 13)
TOTAL_DAYS = (END_DATE - START_DATE).days

HOUSEHOLD_IDS = list(range(54321, 54341))
BUSINESS_IDS  = list(range(54341, 54361))
ALL_USER_IDS  = HOUSEHOLD_IDS + BUSINESS_IDS

def generate_transactions(n=50000):
    transactions = []
    for i in range(n):
        scenario_id = random.randint(1, 6)
        scenario    = TRADE_SCENARIOS[scenario_id]

        seller_id = random.choice(ALL_USER_IDS)
        buyer_id  = random.choice([u for u in ALL_USER_IDS if u != seller_id])

        energy_min, energy_max = scenario["energy_range"]
        energy_amount = round(random.uniform(energy_min, energy_max), 2)
        price = round(energy_amount * BASE_PRICE_PER_KWH * scenario["price_multiplier"], 2)

        txn_date = START_DATE + timedelta(days=random.randint(0, TOTAL_DAYS))

        transactions.append({
            "seller_id":     seller_id,
            "buyer_id":      buyer_id,
            "energy_amount": energy_amount,
            "price":         price,
            "txn_date":      txn_date,
            "scenario_id":   scenario_id,
            "scenario_name": scenario["name"],
        })
    return transactions

def insert_transactions(transactions, batch_size=1000):
    with engine.connect() as conn:
        # Add scenario columns if not exist
        existing = [r[0] for r in conn.execute(text("SHOW COLUMNS FROM energy_transaction")).fetchall()]
        if 'Scenario_ID' not in existing:
            conn.execute(text("ALTER TABLE energy_transaction ADD COLUMN Scenario_ID INT DEFAULT NULL"))
        if 'Scenario_Name' not in existing:
            conn.execute(text("ALTER TABLE energy_transaction ADD COLUMN Scenario_Name VARCHAR(50) DEFAULT NULL"))
        conn.commit()

        print(f"Inserting {len(transactions):,} transactions in batches of {batch_size}...")
        for i in range(0, len(transactions), batch_size):
            batch = transactions[i:i + batch_size]
            conn.execute(text("""
                INSERT INTO energy_transaction
                    (SellerID, BuyerID, Energy_Amount, Price, Transaction_Date, Scenario_ID, Scenario_Name)
                VALUES
                    (:seller_id, :buyer_id, :energy_amount, :price, :txn_date, :scenario_id, :scenario_name)
            """), batch)
            conn.commit()
            print(f"  Inserted {min(i + batch_size, len(transactions)):,} / {len(transactions):,}")

        total = conn.execute(text("SELECT COUNT(*) FROM energy_transaction")).scalar()
        print(f"\nTotal transactions in database: {total:,}")

if __name__ == "__main__":
    print("Generating 50,000 synthetic transactions across 6 trade scenarios...")
    transactions = generate_transactions(50000)
    insert_transactions(transactions)
    print("Done!")
