import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

password = quote_plus(os.getenv('MYSQL_PASSWORD', ''))
engine = create_engine(
    f"mysql+mysqlconnector://{os.getenv('MYSQL_USER', 'root')}:{password}"
    f"@{os.getenv('MYSQL_HOST', 'localhost')}/{os.getenv('MYSQL_DATABASE', 'solshare')}"
)

def generate_payments():
    with engine.connect() as conn:
        # Fix PaymentID to auto increment
        conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
        conn.execute(text("ALTER TABLE payment MODIFY PaymentID INT NOT NULL AUTO_INCREMENT"))
        conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))
        conn.commit()

        # Get all transactions that don't have a payment yet
        result = conn.execute(text("""
            SELECT et.Transaction_ID, et.Price, et.Transaction_Date
            FROM energy_transaction et
            LEFT JOIN payment p ON et.Transaction_ID = p.TransactionID
            WHERE p.TransactionID IS NULL
        """))
        transactions = result.fetchall()
        print(f"Found {len(transactions):,} transactions without payments")

        # Insert payments in batches
        batch_size = 1000
        payments = []
        for txn in transactions:
            from datetime import timedelta
            pay_date = txn[2] + timedelta(days=1)
            payments.append({
                'transaction_id': txn[0],
                'amount_paid':    float(txn[1]),
                'payment_date':   pay_date,
                'status':         'Completed'
            })

        print(f"Inserting {len(payments):,} payments in batches of {batch_size}...")
        for i in range(0, len(payments), batch_size):
            batch = payments[i:i + batch_size]
            conn.execute(text("""
                INSERT INTO payment (TransactionID, Amount_Paid, Payment_Date, Payment_Status)
                VALUES (:transaction_id, :amount_paid, :payment_date, :status)
            """), batch)
            conn.commit()
            print(f"  Inserted {min(i + batch_size, len(payments)):,} / {len(payments):,}")

        total = conn.execute(text("SELECT COUNT(*) FROM payment")).scalar()
        print(f"\nTotal payments in database: {total:,}")

if __name__ == "__main__":
    generate_payments()
