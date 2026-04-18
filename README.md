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
- Analytics and visualizations:
  - Monthly energy surplus trends
  - Platform adoption timeline
  - Distribution of energy transaction amounts
  - Transaction amounts by user type
  - Monthly total revenue
  - Top 10 sellers by energy sold

---

## Project Structure

```
├── DMA-Userproject/
│   ├── app.py                  # Main application (MySQL CRUD + analytics)
│   ├── data_load.py            # Neo4j graph database data loader
│   ├── solshareNeo4J_config.py # Neo4j connection configuration
│   ├── analytics.py            # Analytics module
│   ├── database/
│   │   └── constraints.cypher  # Neo4j database constraints
│   └── .env.example            # Environment variable template
│
└── MySQL Data Dump/
    ├── solshare_household_user.sql
    ├── solshare_business_user.sql
    ├── solshare_employee.sql
    ├── solshare_region.sql
    ├── solshare_energy_profile.sql
    ├── solshare_energy_transaction.sql
    ├── solshare_payment.sql
    ├── solshare_complaints.sql
    ├── solshare_grid.sql
    ├── solshare_member_of.sql
    └── solshare_participate.sql
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Relational Database | MySQL 8+ |
| Graph Database | Neo4j |
| Language | Python 3.11 |
| ORM / DB Driver | SQLAlchemy, mysql-connector-python |
| Analytics | pandas, matplotlib |
| Graph Driver | neo4j-python-driver |

---

## Database Schema

### MySQL (Relational)
- `Household_User` — residential users with solar panels
- `Business_User` — commercial users
- `Energy_Profile` — tracks energy produced, consumed, and surplus per user
- `Energy_Transaction` — records of energy bought and sold
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
- MySQL 8+
- Neo4j Desktop (optional, for graph database)

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

### 4. Create the database and import data
```bash
mysql -u root -p -e "CREATE DATABASE solshare;"
```
Then import each SQL file from the `MySQL Data Dump/` folder:
```bash
mysql -u root -p solshare < "MySQL Data Dump/solshare_household_user.sql"
mysql -u root -p solshare < "MySQL Data Dump/solshare_business_user.sql"
# ... repeat for all files
```

### 5. Run the application
```bash
cd DMA-Userproject
python app.py
```

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
