# SolShare — Affordable Renewable Energy Trading Platform

SolShare is a peer-to-peer solar energy trading platform that allows households and businesses to buy and sell surplus solar energy directly with each other — without going through a traditional utility company.

---

## What It Does

Users with solar panels often produce more energy than they consume. SolShare lets them sell that surplus to nearby buyers at fair market prices, making renewable energy more affordable and accessible for everyone.

---

## Features

- Track energy production, consumption, and surplus per user
- Peer-to-peer energy transactions between buyers and sellers
- Payment processing and tracking
- Complaint management handled by employees
- Regional grid-based user grouping
- Python-based ETL pipelines generating 50,000+ synthetic transactions across 6 trade scenarios
- Interactive Power BI dashboard with 7 visualizations
- Automated analytics using pandas and matplotlib

---

## Trade Scenarios

The platform simulates 6 distinct energy trade scenarios:

| Scenario | Price Multiplier | Energy Range (kWh) |
|----------|-----------------|---------------------|
| Peak Solar | 1.2x | 50 - 200 |
| Off-Peak | 0.8x | 20 - 100 |
| Storm Surplus | 0.6x | 100 - 300 |
| High Demand | 1.5x | 50 - 150 |
| Business Bulk | 1.1x | 200 - 500 |
| Residential Micro | 0.9x | 10 - 60 |

---

## Project Structure

```
├── DMA-Userproject/
│   ├── app.py                                      # Main app (MySQL CRUD + analytics)
│   ├── generate_data.py                            # ETL pipeline: 50K synthetic transactions
│   ├── generate_payments.py                        # ETL pipeline: payment records
│   ├── data_load.py                                # Neo4j graph database data loader
│   ├── solshareNeo4J_config.py                     # Neo4j connection configuration
│   ├── analytics.py                                # Analytics module
│   ├── database/
│   │   └── constraints.cypher                      # Neo4j database constraints
│   ├── Affordable Renewable Energy transaction.pbix  # Power BI dashboard
│   └── .env.example                                # Environment variable template
│
├── MySQL Data Dump/
│   ├── solshare_household_user.sql
│   ├── solshare_business_user.sql
│   ├── solshare_employee.sql
│   ├── solshare_region.sql
│   ├── solshare_energy_profile.sql
│   ├── solshare_energy_transaction.sql
│   ├── solshare_payment.sql
│   ├── solshare_complaints.sql
│   ├── solshare_grid.sql
│   ├── solshare_member_of.sql
│   └── solshare_participate.sql
│
├── Conceptual Model.pdf
├── Relational Model.pdf
├── EER Model.png
├── DMA - Project Proposal.pdf
├── impementation in SQL.pdf
└── impementation in NoSQL.pdf
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Relational Database | MySQL 9.6 |
| Graph Database | Neo4j |
| Language | Python 3.11 |
| ORM / DB Driver | SQLAlchemy, mysql-connector-python |
| Analytics | pandas, matplotlib |
| Graph Driver | neo4j-python-driver |
| Dashboards | Power BI |

---

## Database Schema

### MySQL (Relational)
- `Household_User` — residential users with solar panels
- `Business_User` — commercial users
- `Energy_Profile` — tracks energy produced, consumed, and surplus per user
- `Energy_Transaction` — records of energy bought and sold (50,150 records)
- `Payment` — payment records linked to transactions
- `Complaints` — user complaints handled by employees
- `Employee` — platform staff
- `Region` — geographical areas supervised by employees
- `Grid` — local energy networks grouping nearby users
- `Member_Of` — user-to-grid memberships
- `Participate` — user participation in transactions

### Neo4j (Graph)
Models the same entities as nodes with relationships:
`MEMBER_OF`, `HAS_PROFILE`, `BOUGHT_FROM`, `SOLD_TO`, `HAS_PAYMENT`, `SUBMITTED`, `HANDLED`, `REPORTS_TO`, `SUPERVISED_BY`, `LOCATED_IN`, `PARTICIPATES_IN`

---

## Setup & Installation

### Prerequisites
- Python 3.11+
- MySQL 9+
- Neo4j Desktop (optional, for graph database)
- Power BI Desktop (optional, for dashboards)

### 1. Clone the repository
```bash
git clone https://github.com/ketaki-19/Affordable-Renewable-Energy-.git
cd Affordable-Renewable-Energy-
```

### 2. Install dependencies
```bash
pip install pandas matplotlib sqlalchemy mysql-connector-python neo4j python-dotenv
```

### 3. Configure environment variables
```bash
cp DMA-Userproject/.env.example DMA-Userproject/.env
```
Edit `.env` with your MySQL credentials:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password_here
MYSQL_DATABASE=solshare
```

### 4. Create the database and import base data
```bash
mysql -u root -p -e "CREATE DATABASE solshare;"
```
Then import each SQL file from the `MySQL Data Dump/` folder:
```bash
mysql -u root -p solshare < "MySQL Data Dump/solshare_household_user.sql"
mysql -u root -p solshare < "MySQL Data Dump/solshare_business_user.sql"
# ... repeat for all files
```

### 5. Generate 50,000+ synthetic transactions (ETL Pipeline)
```bash
cd DMA-Userproject
python generate_data.py       # Generates 50,000 transactions across 6 scenarios
python generate_payments.py   # Generates matching payment records
```

### 6. Run analytics
```bash
python app.py
```

### 7. Open Power BI Dashboard
Open `DMA-Userproject/Affordable Renewable Energy transaction.pbix` in Power BI Desktop.

---

## ETL Pipeline Details

### generate_data.py
- Generates **50,000 synthetic energy transactions** in batches of 1,000
- Distributes transactions across 6 trade scenarios with distinct pricing dynamics
- Uses SQLAlchemy for efficient bulk inserts
- Transaction dates span from January 2023 to October 2025

### generate_payments.py
- Automatically creates matching payment records for all transactions
- Payment date set one day after transaction date
- Default status: `Completed`

---

## Analytics Output

Running `app.py` generates the following charts:

| Chart | Description |
|-------|-------------|
| `energy_surplus_trend.png` | Monthly average and total energy surplus |
| `user_adoption_timeline.png` | Cumulative user growth over time |
| `energy_amount_distribution.png` | Histogram of transaction energy amounts |
| `transaction_distribution_by_user_type.png` | Box plot of transaction amounts by user type |
| `monthly_revenue.png` | Total revenue generated per month |
| `top_sellers.png` | Top 10 sellers by total energy sold |

---

## Power BI Dashboard

The dashboard (`Affordable Renewable Energy transaction.pbix`) includes 7 visualizations:

1. **Total Revenue by Scenario** — Bar chart showing revenue distribution across 6 trade scenarios
2. **Monthly Revenue Trend** — Line chart of revenue over time
3. **Energy Amount by Scenario** — Column chart comparing energy volume per scenario
4. **Surplus Energy by Region** — Geographic map showing regional energy surplus
5. **Energy Produced vs Consumed by User Type** — Comparison between Household and Business users
6. **Top 10 Sellers by Energy Sold** — Horizontal bar chart of top performers
7. **Total Revenue vs Target** — Gauge chart tracking revenue against financial goals

### Key Insights
- **Business Bulk** scenario generates **~43% of total revenue** ($6.5M of $14.76M)
- Total revenue exceeds $5M target by **195%**
- Business users trade ~28% more energy than household users
- Platform handled 50,150 total transactions across 40 users

---

## Author

**Ketaki** — [GitHub](https://github.com/ketaki-19)
