# import mysql.connector
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from mysql.connector import Error

# # Database Configuration
# DB_CONFIG = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'Ketaki@19',
#     'database': 'solshare'
# }

# # --------------------------
# # Core Connection Functions
# # --------------------------
# def create_connection():
#     """Create database connection"""
#     try:
#         conn = mysql.connector.connect(**DB_CONFIG)
#         print("✅ Connected to MySQL!")
#         return conn
#     except Error as e:
#         print(f"❌ Connection error: {e}")
#         return None

# def close_connection(conn):
#     """Close database connection"""
#     if conn.is_connected():
#         conn.close()
#         print("🔌 Connection closed.")

# # --------------------------
# # CRUD Operations with Integrity Checks
# # --------------------------
# def create_user(conn, user_type, user_data):
#     """
#     Create user (Household/Business) with automatic profile creation
#     user_data format: (name, email, phone, consumption_rate, address, renewable_capacity)
#     """
#     try:
#         cursor = conn.cursor()
        
#         # Insert into appropriate user table
#         if user_type == "household":
#             query = """
#                 INSERT INTO Household_User 
#                 (Name, Email, Phone, Consumption_Rate, Address, Renewable_Capacity)
#                 VALUES (%s, %s, %s, %s, %s, %s)
#             """
#         elif user_type == "business":
#             query = """
#                 INSERT INTO Business_User 
#                 (Name, Email, Phone, Consumption_Rate, Address, Renewable_Capacity)
#                 VALUES (%s, %s, %s, %s, %s, %s)
#             """
#         else:
#             raise ValueError("Invalid user type")
            
#         cursor.execute(query, user_data)
#         user_id = cursor.lastrowid
        
#         # Create energy profile
#         profile_query = """
#             INSERT INTO Energy_Profile 
#             (UserID, Energy_Produced, Energy_Consumed, Surplus_Energy)
#             VALUES (%s, 0, 0, 0)
#         """
#         cursor.execute(profile_query, (user_id,))
        
#         conn.commit()
#         print(f"➡️ Created {user_type} user {user_id} with energy profile")
#         return user_id
        
#     except Error as e:
#         conn.rollback()
#         print(f"❌ Creation error: {e}")
#         return None

# def update_user(conn, user_type, user_id, update_data):
#     """
#     Update user details
#     update_data format: {"field": value} dictionary
#     """
#     try:
#         cursor = conn.cursor()
#         set_clause = ", ".join([f"{k} = %s" for k in update_data])
#         values = list(update_data.values())
        
#         if user_type == "household":
#             query = f"""
#                 UPDATE Household_User 
#                 SET {set_clause}
#                 WHERE UserID = %s
#             """
#         elif user_type == "business":
#             query = f"""
#                 UPDATE Business_User 
#                 SET {set_clause}
#                 WHERE UserID = %s
#             """
#         else:
#             raise ValueError("Invalid user type")
            
#         values.append(user_id)
#         cursor.execute(query, values)
        
#         if cursor.rowcount == 0:
#             print(f"⚠️ No user found with ID {user_id}")
#             return False
            
#         conn.commit()
#         print(f"🔄 Updated {user_type} user {user_id}")
#         return True
        
#     except Error as e:
#         conn.rollback()
#         print(f"❌ Update error: {e}")
#         return False

# def delete_user(conn, user_type, user_id):
#     """
#     Delete user and associated profile with integrity checks
#     """
#     try:
#         cursor = conn.cursor()
        
#         # Verify user exists
#         if user_type == "household":
#             exists_query = "SELECT UserID FROM Household_User WHERE UserID = %s"
#         elif user_type == "business":
#             exists_query = "SELECT UserID FROM Business_User WHERE UserID = %s"
#         else:
#             raise ValueError("Invalid user type")
            
#         cursor.execute(exists_query, (user_id,))
#         if not cursor.fetchone():
#             print(f"⚠️ No {user_type} user found with ID {user_id}")
#             return False
            
#         # Delete profile first
#         cursor.execute("DELETE FROM Energy_Profile WHERE UserID = %s", (user_id,))
        
#         # Delete user
#         if user_type == "household":
#             delete_query = "DELETE FROM Household_User WHERE UserID = %s"
#         else:
#             delete_query = "DELETE FROM Business_User WHERE UserID = %s"
            
#         cursor.execute(delete_query, (user_id,))
#         conn.commit()
#         print(f"🗑️ Deleted {user_type} user {user_id} and profile")
#         return True
        
#     except Error as e:
#         conn.rollback()
#         print(f"❌ Deletion error: {e}")
#         return False

# # --------------------------
# # Enhanced Analytics (Your Custom Visualizations)
# # --------------------------
# def plot_energy_surplus_trend(conn):
#     """Line Chart: Monthly Energy Surplus Trends"""
#     query = """
#         SELECT 
#             DATE_FORMAT(et.Transaction_Date, '%Y-%m') AS month,
#             AVG(ep.Surplus_Energy) AS avg_surplus,
#             SUM(ep.Surplus_Energy) AS total_surplus
#         FROM Energy_Profile ep
#         JOIN Energy_Transaction et ON ep.UserID = et.SellerID
#         GROUP BY month
#         ORDER BY month
#     """
#     df = pd.read_sql(query, conn)
#     fig, ax1 = plt.subplots(figsize=(12,6))
#     # Plot average surplus
#     ax1.plot(df['month'], df['avg_surplus'], color='#e74c3c', marker='o', label='Average Surplus')
#     ax1.set_xlabel('Month')
#     ax1.set_ylabel('Average Surplus (kWh)')
#     ax1.tick_params(axis='y')
#     plt.xticks(rotation=45)
    
#     # Create second y-axis for total surplus
#     ax2 = ax1.twinx()
#     ax2.bar(df['month'], df['total_surplus'], alpha=0.3, color='#3498db', label='Total Surplus')
#     ax2.set_ylabel('Total Surplus (kWh)')
    
#     plt.title('Monthly Energy Surplus Trends')
#     fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))
#     plt.show()

# def plot_user_adoption_timeline(conn):
#     """Line Chart: Cumulative User Growth Over Time"""
#     query = """
#         SELECT 
#             DATE(et.Transaction_Date) AS signup_date,
#             COUNT(DISTINCT 
#                 CASE WHEN hu.UserID IS NOT NULL THEN hu.UserID 
#                 ELSE bu.UserID END
#             ) AS new_users
#         FROM Energy_Transaction et
#         LEFT JOIN Household_User hu ON et.SellerID = hu.UserID
#         LEFT JOIN Business_User bu ON et.SellerID = bu.UserID
#         GROUP BY signup_date
#         ORDER BY signup_date
#     """
#     df = pd.read_sql(query, conn)
#     df['cumulative_users'] = df['new_users'].cumsum()
    
#     plt.figure(figsize=(12,6))
#     plt.plot(df['signup_date'], df['cumulative_users'], marker='o', color='#2ecc71')
#     plt.title('Platform Adoption Timeline')
#     plt.xlabel('Date')
#     plt.ylabel('Total Registered Users')
#     plt.grid(True)
#     plt.xticks(rotation=45)
#     plt.show()

# # def plot_surplus_vs_traded(conn):
# #     """Scatter Plot: Surplus Energy Generated vs Energy Traded"""
# #     try:
# #         # Improved query with NULL handling
# #         query = """
# #             SELECT 
# #                 ep.Surplus_Energy,
# #                 COALESCE(SUM(et.Energy_Amount), 0) AS total_traded
# #             FROM Energy_Profile ep
# #             LEFT JOIN Energy_Transaction et 
# #                 ON ep.UserID = et.SellerID
# #             GROUP BY ep.UserID
# #         """
# #         df = pd.read_sql(query, conn)
        
# #         if df.empty:
# #             print("⚠️ No energy profile data found")
# #             return
            
# #         # Clean data: Remove negative surplus values
# #         df = df[df['Surplus_Energy'] >= 0]
        
# #         plt.figure(figsize=(12,6))
# #         plt.scatter(df['Surplus_Energy'], df['total_traded'], 
# #                     alpha=0.6, c='#e67e22', edgecolors='w', s=100)
        
# #         # Add trendline
# #         z = np.polyfit(df['Surplus_Energy'], df['total_traded'], 1)
# #         p = np.poly1d(z)
# #         plt.plot(df['Surplus_Energy'], p(df['Surplus_Energy']), 
# #                 "r--", linewidth=2, label='Trendline')
        
# #         # Add annotations
# #         plt.title('Surplus Energy Utilization Efficiency\n(0 = No Trading Activity)', fontsize=14)
# #         plt.xlabel('Surplus Energy Generated (kWh)', fontsize=12)
# #         plt.ylabel('Energy Actually Traded (kWh)', fontsize=12)
# #         plt.grid(True, alpha=0.3)
# #         plt.legend()
        
# #         # Force display if running in non-interactive mode
# #         plt.show()

# #     except Error as e:
# #         print(f"❌ Database error: {e}")
# #     except Exception as e:
# #         print(f"❌ Plotting error: {str(e)}")

# def plot_user_type_distribution(conn):
#     """Pie Chart: Distribution of Users by Energy Surplus Category"""
#     try:
#         query = """
#             SELECT 
#                 CASE 
#                     WHEN Surplus_Energy > 100 THEN 'High Surplus (>100 kWh)'
#                     WHEN Surplus_Energy > 10 THEN 'Medium Surplus (10-100 kWh)'
#                     WHEN Surplus_Energy > 0 THEN 'Low Surplus (0-10 kWh)'
#                     ELSE 'No Surplus (≤0 kWh)'
#                 END AS surplus_category,
#                 COUNT(*) AS count
#             FROM Energy_Profile
#             GROUP BY surplus_category
#         """
#         df = pd.read_sql(query, conn)
        
#         if df.empty or df['count'].sum() == 0:
#             print("⚠️ No energy profiles found in database")
#             return
            
#         # Create pie chart
#         plt.figure(figsize=(8,8))
#         plt.pie(df['count'], labels=df['surplus_category'], 
#                 autopct='%1.1f%%', startangle=140,
#                 colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'],
#                 explode=(0.05, 0.05, 0.05, 0.05))
#         plt.title('User Distribution by Energy Surplus Category', pad=20)
#         plt.savefig('user_surplus_distribution.png')
        
#     except Error as e:
#         print(f"❌ Database error: {e}")
        
#     # --------------------------
# # Main Execution with Example Workflow
# # --------------------------
# if __name__ == "__main__":
#     conn = create_connection()
#     if conn:
#         try:
#             # ===== DEMO CRUD OPERATIONS =====
#             print("\n=== USER MANAGEMENT DEMO ===")
#             # Create test users
#             household_data = (
#                 "Eco Family", 
#                 "eco@example.com", 
#                 "555-1234", 
#                 20.5, 
#                 "123 Green St", 
#                 30.0
#             )
#             h_user_id = create_user(conn, "household", household_data)
            
#             business_data = (
#                 "Solar Solutions", 
#                 "sales@solarsolutions.com", 
#                 "555-5678", 
#                 150.0, 
#                 "456 Renewable Ave", 
#                 300.0
#             )
#             b_user_id = create_user(conn, "business", business_data)

#             # Update user
#             print("\n=== UPDATE OPERATION ===")
#             update_success = update_user(conn, "household", h_user_id, 
#                 {"Consumption_Rate": 25.0, "Renewable_Capacity": 35.0})

#             # # ===== DATA ANALYTICS =====
#             # print("\n=== GENERATING ANALYTICS ===")
#             # plot_energy_surplus_trend(conn)
#             # plot_user_adoption_timeline(conn)
#             # # plot_surplus_vs_traded(conn)
#             # plot_user_type_distribution(conn)
#             # plot_energy_amount_distribution(conn)

#              # ===== DATA ANALYTICS =====
#             print("\n=== GENERATING ANALYTICS ===")
#             plot_energy_surplus_trend(conn)
#             plot_user_adoption_timeline(conn)
#             plot_user_type_distribution(conn)
#             # plot_energy_amount_distribution(conn)
#             # plot_transaction_distribution_by_user_type(conn)

#             # ===== CLEANUP DEMO =====
#             print("\n=== CLEANUP OPERATION ===")
#             delete_success = delete_user(conn, "household", h_user_id)
            
#         except Exception as e:
#             print(f"⚠️ Unexpected error: {str(e)}")
#         finally:
#             close_connection(conn)
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from sqlalchemy import create_engine, text

# # Database Configuration
# DB_CONFIG = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'Ketaki@19',
#     'database': 'solshare'
# }

# # --------------------------
# # Core Connection Functions
# # --------------------------
# def create_connection():
#     """Create database connection using SQLAlchemy"""
#     try:
#         connection_string = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
#         engine = create_engine(connection_string)
#         print("✅ Connected to MySQL via SQLAlchemy!")
#         return engine
#     except Exception as e:
#         print(f"❌ Connection error: {e}")
#         return None

# def close_connection(engine):
#     """Close database connection"""
#     if engine:
#         engine.dispose()
#         print("🔌 Connection closed.")

# # --------------------------
# # CRUD Operations with Integrity Checks
# # --------------------------
# def create_user(conn, user_type, user_data):
#     """
#     Create user (Household/Business) with automatic profile creation
#     user_data format: (name, email, phone, consumption_rate, address, renewable_capacity)
#     """
#     try:
#         if user_type == "household":
#             query = text("""
#                 INSERT INTO Household_User 
#                 (Name, Email, Phone, Consumption_Rate, Address, Renewable_Capacity)
#                 VALUES (:name, :email, :phone, :consumption_rate, :address, :renewable_capacity)
#             """)
#         elif user_type == "business":
#             query = text("""
#                 INSERT INTO Business_User 
#                 (Name, Email, Phone, Consumption_Rate, Address, Renewable_Capacity)
#                 VALUES (:name, :email, :phone, :consumption_rate, :address, :renewable_capacity)
#             """)
#         else:
#             raise ValueError("Invalid user type")
            
#         with conn.connect() as mysql_conn:
#             # Execute user insertion
#             result = mysql_conn.execute(query, {
#                 'name': user_data[0],
#                 'email': user_data[1],
#                 'phone': user_data[2],
#                 'consumption_rate': user_data[3],
#                 'address': user_data[4],
#                 'renewable_capacity': user_data[5]
#             })
#             user_id = result.lastrowid
            
#             # Create energy profile
#             profile_query = text("""
#                 INSERT INTO Energy_Profile 
#                 (UserID, Energy_Produced, Energy_Consumed, Surplus_Energy)
#                 VALUES (:user_id, :energy_produced, :energy_consumed, :surplus_energy)
#             """)
#             mysql_conn.execute(profile_query, {
#                 'user_id': user_id,
#                 'energy_produced': 0,
#                 'energy_consumed': 0,
#                 'surplus_energy': 0
#             })
            
#             mysql_conn.commit()
#             print(f"➡️ Created {user_type} user {user_id} with energy profile")
#             return user_id
        
#     except Exception as e:
#         print(f"❌ Creation error: {e}")
#         return None

# def update_user(conn, user_type, user_id, update_data):
#     """
#     Update user details
#     update_data format: {"field": value} dictionary
#     """
#     if user_id is None:
#         print("⚠️ Cannot update user: User ID is None")
#         return False
        
#     try:
#         set_clause = ", ".join([f"{k} = :{k}" for k in update_data])
#         params = update_data.copy()
#         params['user_id'] = user_id
        
#         if user_type == "household":
#             query = text(f"""
#                 UPDATE Household_User 
#                 SET {set_clause}
#                 WHERE UserID = :user_id
#             """)
#         elif user_type == "business":
#             query = text(f"""
#                 UPDATE Business_User 
#                 SET {set_clause}
#                 WHERE UserID = :user_id
#             """)
#         else:
#             raise ValueError("Invalid user type")
            
#         with conn.connect() as mysql_conn:
#             result = mysql_conn.execute(query, params)
            
#             if result.rowcount == 0:
#                 print(f"⚠️ No user found with ID {user_id}")
#                 return False
                
#             mysql_conn.commit()
#             print(f"🔄 Updated {user_type} user {user_id}")
#             return True
        
#     except Exception as e:
#         print(f"❌ Update error: {e}")
#         return False

# def delete_user(conn, user_type, user_id):
#     """
#     Delete user and associated profile with integrity checks
#     """
#     if user_id is None:
#         print("⚠️ Cannot delete user: User ID is None")
#         return False
        
#     try:
#         if user_type == "household":
#             exists_query = text("SELECT UserID FROM Household_User WHERE UserID = :user_id")
#         elif user_type == "business":
#             exists_query = text("SELECT UserID FROM Business_User WHERE UserID = :user_id")
#         else:
#             raise ValueError("Invalid user type")
            
#         with conn.connect() as mysql_conn:
#             result = mysql_conn.execute(exists_query, {'user_id': user_id})
#             if not result.fetchone():
#                 print(f"⚠️ No {user_type} user found with ID {user_id}")
#                 return False
                
#             # Delete profile first
#             mysql_conn.execute(text("DELETE FROM Energy_Profile WHERE UserID = :user_id"), {'user_id': user_id})
            
#             # Delete user
#             if user_type == "household":
#                 delete_query = text("DELETE FROM Household_User WHERE UserID = :user_id")
#             else:
#                 delete_query = text("DELETE FROM Business_User WHERE UserID = :user_id")
                
#             mysql_conn.execute(delete_query, {'user_id': user_id})
#             mysql_conn.commit()
#             print(f"🗑️ Deleted {user_type} user {user_id} and profile")
#             return True
        
#     except Exception as e:
#         print(f"❌ Deletion error: {e}")
#         return False

# # --------------------------
# # Enhanced Analytics
# # --------------------------
# def plot_energy_surplus_trend(conn):
#     """Line Chart: Monthly Energy Surplus Trends"""
#     try:
#         query = """
#             SELECT 
#                 DATE_FORMAT(et.Transaction_Date, '%Y-%m') AS month,
#                 AVG(ep.Surplus_Energy) AS avg_surplus,
#                 SUM(ep.Surplus_Energy) AS total_surplus
#             FROM Energy_Profile ep
#             JOIN Energy_Transaction et ON ep.UserID = et.SellerID
#             GROUP BY month
#             ORDER BY month
#         """
#         df = pd.read_sql(query, conn)
#         if df.empty:
#             print("⚠️ No data for energy surplus trend")
#             return
            
#         fig, ax1 = plt.subplots(figsize=(12,6))
#         ax1.plot(df['month'], df['avg_surplus'], color='#e74c3c', marker='o', label='Average Surplus')
#         ax1.set_xlabel('Month')
#         ax1.set_ylabel('Average Surplus (kWh)')
#         ax1.tick_params(axis='y')
#         plt.xticks(rotation=45)
        
#         ax2 = ax1.twinx()
#         ax2.bar(df['month'], df['total_surplus'], alpha=0.3, color='#3498db', label='Total Surplus')
#         ax2.set_ylabel('Total Surplus (kWh)')
        
#         plt.title('Monthly Energy Surplus Trends')
#         fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))
#         plt.savefig('energy_surplus_trend.png')
#         plt.close()
        
#     except Exception as e:
#         print(f"❌ Plotting error: {e}")

# def plot_user_adoption_timeline(conn):
#     """Line Chart: Cumulative User Growth Over Time"""
#     try:
#         query = """
#             SELECT 
#                 DATE(et.Transaction_Date) AS signup_date,
#                 COUNT(DISTINCT 
#                     CASE WHEN hu.UserID IS NOT NULL THEN hu.UserID 
#                     ELSE bu.UserID END
#                 ) AS new_users
#             FROM Energy_Transaction et
#             LEFT JOIN Household_User hu ON et.SellerID = hu.UserID
#             LEFT JOIN Business_User bu ON et.SellerID = bu.UserID
#             GROUP BY signup_date
#             ORDER BY signup_date
#         """
#         df = pd.read_sql(query, conn)
#         if df.empty:
#             print("⚠️ No data for user adoption timeline")
#             return
            
#         df['cumulative_users'] = df['new_users'].cumsum()
        
#         plt.figure(figsize=(12,6))
#         plt.plot(df['signup_date'], df['cumulative_users'], marker='o', color='#2ecc71')
#         plt.title('Platform Adoption Timeline')
#         plt.xlabel('Date')
#         plt.ylabel('Total Registered Users')
#         plt.grid(True)
#         plt.xticks(rotation=45)
#         plt.savefig('user_adoption_timeline.png')
#         plt.close()
        
#     except Exception as e:
#         print(f"❌ Plotting error: {e}")

# def plot_user_type_distribution(conn):
#     """Pie Chart: Distribution of Users by Energy Surplus Category"""
#     try:
#         query = """
#             SELECT 
#                 CASE 
#                     WHEN Surplus_Energy > 100 THEN 'High Surplus (>100 kWh)'
#                     WHEN Surplus_Energy > 10 THEN 'Medium Surplus (10-100 kWh)'
#                     WHEN Surplus_Energy > 0 THEN 'Low Surplus (0-10 kWh)'
#                     ELSE 'No Surplus (≤0 kWh)'
#                 END AS surplus_category,
#                 COUNT(*) AS count
#             FROM Energy_Profile
#             GROUP BY surplus_category
#         """
#         df = pd.read_sql(query, conn)
        
#         if df.empty or df['count'].sum() == 0:
#             print("⚠️ No energy profiles found in database")
#             return
            
#         print(f"Debug: Surplus categories found: {df['surplus_category'].tolist()}")
#         print(f"Debug: Counts: {df['count'].tolist()}")
        
#         num_categories = len(df)
#         explode = [0.05] * num_categories
        
#         plt.figure(figsize=(8,8))
#         plt.pie(df['count'], labels=df['surplus_category'], 
#                 autopct='%1.1f%%', startangle=140,
#                 colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'][:num_categories],
#                 explode=explode)
#         plt.title('User Distribution by Energy Surplus Category', pad=20)
#         plt.savefig('user_surplus_distribution.png')
#         plt.close()
        
#     except Exception as e:
#         print(f"❌ Plotting error: {e}")

# def plot_energy_amount_distribution(conn):
#     """Histogram: Energy Transaction Amounts"""
#     try:
#         query = "SELECT Energy_Amount FROM Energy_Transaction"
#         df = pd.read_sql(query, conn)
        
#         if df.empty:
#             print("⚠️ No energy transactions found")
#             return
            
#         bin_count = min(20, len(df) // 5) if len(df) > 0 else 10
        
#         plt.figure(figsize=(12,6))
#         plt.hist(df['Energy_Amount'], bins=bin_count, 
#                 color='purple', edgecolor='white',
#                 alpha=0.7)
#         plt.title('Distribution of Energy Transaction Amounts')
#         plt.xlabel('Energy Amount (kWh)')
#         plt.ylabel('Number of Transactions')
#         plt.grid(axis='y', alpha=0.3)
#         plt.savefig('energy_amount_distribution.png')
#         plt.close()
        
#     except Exception as e:
#         print(f"❌ Plotting error: {e}")

# def plot_transaction_distribution_by_user_type(conn):
#     """Box Plot: Energy Transaction Amounts by User Type"""
#     try:
#         query = """
#             SELECT 
#                 CASE 
#                     WHEN hu.UserID IS NOT NULL THEN 'Household'
#                     WHEN bu.UserID IS NOT NULL THEN 'Business'
#                 END AS user_type,
#                 et.Energy_Amount
#             FROM Energy_Transaction et
#             LEFT JOIN Household_User hu ON et.SellerID = hu.UserID
#             LEFT JOIN Business_User bu ON et.SellerID = bu.UserID
#             WHERE hu.UserID IS NOT NULL OR bu.UserID IS NOT NULL
#         """
#         df = pd.read_sql(query, conn)
        
#         if df.empty:
#             print("⚠️ No energy transactions found for users")
#             return
            
#         plt.figure(figsize=(10,6))
#         df.boxplot(column='Energy_Amount', by='user_type', grid=False, patch_artist=True,
#                   boxprops=dict(facecolor='#66b3ff', color='black'),
#                   whiskerprops=dict(color='black'),
#                   capprops=dict(color='black'),
#                   medianprops=dict(color='red'))
#         plt.title('Energy Transaction Amounts by User Type')
#         plt.suptitle('')
#         plt.xlabel('User Type')
#         plt.ylabel('Energy Amount (kWh)')
#         plt.tight_layout()
#         plt.savefig('transaction_distribution_by_user_type.png')
#         plt.close()
        
#     except Exception as e:
#         print(f"❌ Plotting error: {e}")

# # --------------------------
# # Main Execution with Example Workflow
# # --------------------------
# if __name__ == "__main__":
#     conn = create_connection()
#     if conn:
#         try:
#             # ===== DATA ANALYTICS =====
#             print("\n=== GENERATING ANALYTICS ===")
#             plot_energy_surplus_trend(conn)
#             plot_user_adoption_timeline(conn)
#             plot_user_type_distribution(conn)
#             plot_energy_amount_distribution(conn)
#             # plot_transaction_distribution_by_user_type(conn)
            
#         except Exception as e:
#             print(f"⚠️ Unexpected error: {str(e)}")
#         finally:
#             close_connection(conn)





import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

# Database Configuration
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'database': os.getenv('MYSQL_DATABASE', 'solshare')
}

# --------------------------
# Core Connection Functions
# --------------------------
def create_connection():
    """Create database connection using SQLAlchemy"""
    try:
        from urllib.parse import quote_plus
        password = quote_plus(DB_CONFIG['password'])
        connection_string = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{password}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
        engine = create_engine(connection_string)
        print("✅ Connected to MySQL via SQLAlchemy!")
        return engine
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return None

def close_connection(engine):
    """Close database connection"""
    if engine:
        engine.dispose()
        print("🔌 Connection closed.")

# --------------------------
# CRUD Operations with Integrity Checks
# --------------------------
def create_user(conn, user_type, user_data):
    """
    Create user (Household/Business) with automatic profile creation
    user_data format: (name, email, phone, consumption_rate, address, renewable_capacity)
    """
    try:
        if user_type == "household":
            query = text("""
                INSERT INTO Household_User 
                (Name, Email, Phone, Consumption_Rate, Address, Renewable_Capacity)
                VALUES (:name, :email, :phone, :consumption_rate, :address, :renewable_capacity)
            """)
        elif user_type == "business":
            query = text("""
                INSERT INTO Business_User 
                (Name, Email, Phone, Consumption_Rate, Address, Renewable_Capacity)
                VALUES (:name, :email, :phone, :consumption_rate, :address, :renewable_capacity)
            """)
        else:
            raise ValueError("Invalid user type")
            
        with conn.connect() as mysql_conn:
            # Execute user insertion
            result = mysql_conn.execute(query, {
                'name': user_data[0],
                'email': user_data[1],
                'phone': user_data[2],
                'consumption_rate': user_data[3],
                'address': user_data[4],
                'renewable_capacity': user_data[5]
            })
            user_id = result.lastrowid
            
            # Create energy profile
            profile_query = text("""
                INSERT INTO Energy_Profile 
                (UserID, Energy_Produced, Energy_Consumed, Surplus_Energy)
                VALUES (:user_id, :energy_produced, :energy_consumed, :surplus_energy)
            """)
            mysql_conn.execute(profile_query, {
                'user_id': user_id,
                'energy_produced': 0,
                'energy_consumed': 0,
                'surplus_energy': 0
            })
            
            mysql_conn.commit()
            print(f"➡️ Created {user_type} user {user_id} with energy profile")
            return user_id
        
    except Exception as e:
        print(f"❌ Creation error: {e}")
        return None

def update_user(conn, user_type, user_id, update_data):
    """
    Update user details
    update_data format: {"field": value} dictionary
    """
    if user_id is None:
        print("⚠️ Cannot update user: User ID is None")
        return False
        
    try:
        set_clause = ", ".join([f"{k} = :{k}" for k in update_data])
        params = update_data.copy()
        params['user_id'] = user_id
        
        if user_type == "household":
            query = text(f"""
                UPDATE Household_User 
                SET {set_clause}
                WHERE UserID = :user_id
            """)
        elif user_type == "business":
            query = text(f"""
                UPDATE Business_User 
                SET {set_clause}
                WHERE UserID = :user_id
            """)
        else:
            raise ValueError("Invalid user type")
            
        with conn.connect() as mysql_conn:
            result = mysql_conn.execute(query, params)
            
            if result.rowcount == 0:
                print(f"⚠️ No user found with ID {user_id}")
                return False
                
            mysql_conn.commit()
            print(f"🔄 Updated {user_type} user {user_id}")
            return True
        
    except Exception as e:
        print(f"❌ Update error: {e}")
        return False

def delete_user(conn, user_type, user_id):
    """
    Delete user and associated profile with integrity checks
    """
    if user_id is None:
        print("⚠️ Cannot delete user: User ID is None")
        return False
        
    try:
        if user_type == "household":
            query = text("SELECT UserID FROM Household_User WHERE UserID = :user_id")
        elif user_type == "business":
            query = text("SELECT UserID FROM Business_User WHERE UserID = :user_id")
        else:
            raise ValueError("Invalid user type")
            
        with conn.connect() as mysql_conn:
            result = mysql_conn.execute(query, {'user_id': user_id})
            if not result.fetchone():
                print(f"⚠️ No {user_type} user found with ID {user_id}")
                return False
                
            # Delete profile first
            mysql_conn.execute(text("DELETE FROM Energy_Profile WHERE UserID = :user_id"), {'user_id': user_id})
            
            # Delete user
            if user_type == "household":
                delete_query = text("DELETE FROM Household_User WHERE UserID = :user_id")
            else:
                delete_query = text("DELETE FROM Business_User WHERE UserID = :user_id")
                
            mysql_conn.execute(delete_query, {'user_id': user_id})
            mysql_conn.commit()
            print(f"🗑️ Deleted {user_type} user {user_id} and profile")
            return True
        
    except Exception as e:
        print(f"❌ Deletion error: {e}")
        return False

# --------------------------
# Enhanced Analytics
# --------------------------
def plot_energy_surplus_trend(conn):
    """Line Chart: Monthly Energy Surplus Trends"""
    try:
        query = """
            SELECT 
                DATE_FORMAT(et.Transaction_Date, '%Y-%m') AS month,
                AVG(ep.Surplus_Energy) AS avg_surplus,
                SUM(ep.Surplus_Energy) AS total_surplus
            FROM Energy_Profile ep
            JOIN Energy_Transaction et ON ep.UserID = et.SellerID
            GROUP BY month
            ORDER BY month
        """
        df = pd.read_sql(query, conn)
        if df.empty:
            print("⚠️ No data for energy surplus trend")
            return
            
        fig, ax1 = plt.subplots(figsize=(12,6))
        ax1.plot(df['month'], df['avg_surplus'], color='#e74c3c', marker='o', label='Average Surplus')
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Average Surplus (kWh)')
        ax1.tick_params(axis='y')
        plt.xticks(rotation=45)
        
        ax2 = ax1.twinx()
        ax2.bar(df['month'], df['total_surplus'], alpha=0.3, color='#3498db', label='Total Surplus')
        ax2.set_ylabel('Total Surplus (kWh)')
        
        plt.title('Monthly Energy Surplus Trends')
        fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))
        plt.savefig('energy_surplus_trend.png')
        plt.close()
        
    except Exception as e:
        print(f"❌ Plotting error: {e}")

def plot_user_adoption_timeline(conn):
    """Line Chart: Cumulative User Growth Over Time"""
    try:
        query = """
            SELECT 
                DATE(et.Transaction_Date) AS signup_date,
                COUNT(DISTINCT 
                    CASE WHEN hu.UserID IS NOT NULL THEN hu.UserID 
                    ELSE bu.UserID END
                ) AS new_users
            FROM Energy_Transaction et
            LEFT JOIN Household_User hu ON et.SellerID = hu.UserID
            LEFT JOIN Business_User bu ON et.SellerID = bu.UserID
            GROUP BY signup_date
            ORDER BY signup_date
        """
        df = pd.read_sql(query, conn)
        if df.empty:
            print("⚠️ No data for user adoption timeline")
            return
            
        df['cumulative_users'] = df['new_users'].cumsum()
        
        plt.figure(figsize=(12,6))
        plt.plot(df['signup_date'], df['cumulative_users'], marker='o', color='#2ecc71')
        plt.title('Platform Adoption Timeline')
        plt.xlabel('Date')
        plt.ylabel('Total Registered Users')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.savefig('user_adoption_timeline.png')
        plt.close()
        
    except Exception as e:
        print(f"❌ Plotting error: {e}")

def plot_user_type_distribution(conn):
    """Pie Chart: Distribution of Users by Energy Surplus Category"""
    try:
        query = """
            SELECT 
                CASE 
                    WHEN Surplus_Energy > 100 THEN 'High Surplus (>100 kWh)'
                    WHEN Surplus_Energy > 10 THEN 'Medium Surplus (10-100 kWh)'
                    WHEN Surplus_Energy > 0 THEN 'Low Surplus (0-10 kWh)'
                    ELSE 'No Surplus (≤0 kWh)'
                END AS surplus_category,
                COUNT(*) AS count
            FROM Energy_Profile
            GROUP BY surplus_category
        """
        df = pd.read_sql(query, conn)
        
        if df.empty or df['count'].sum() == 0:
            print("⚠️ No energy profiles found in database")
            return
            
        print(f"Debug: Surplus categories found: {df['surplus_category'].tolist()}")
        print(f"Debug: Counts: {df['count'].tolist()}")
        
        num_categories = len(df)
        explode = [0.05] * num_categories
        
        plt.figure(figsize=(8,8))
        plt.pie(df['count'], labels=df['surplus_category'], 
                autopct='%1.1f%%', startangle=140,
                colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'][:num_categories],
                explode=explode)
        plt.title('User Distribution by Energy Surplus Category', pad=20)
        plt.savefig('user_surplus_distribution.png')
        plt.close()
        
    except Exception as e:
        print(f"❌ Plotting error: {e}")

def plot_energy_amount_distribution(conn):
    """Histogram: Energy Transaction Amounts"""
    try:
        query = "SELECT Energy_Amount FROM Energy_Transaction"
        df = pd.read_sql(query, conn)
        
        if df.empty:
            print("⚠️ No energy transactions found")
            return
            
        bin_count = min(20, len(df) // 5) if len(df) > 0 else 10
        
        plt.figure(figsize=(12,6))
        plt.hist(df['Energy_Amount'], bins=bin_count, 
                color='purple', edgecolor='white',
                alpha=0.7)
        plt.title('Distribution of Energy Transaction Amounts')
        plt.xlabel('Energy Amount (kWh)')
        plt.ylabel('Number of Transactions')
        plt.grid(axis='y', alpha=0.3)
        plt.savefig('energy_amount_distribution.png')
        plt.close()
        
    except Exception as e:
        print(f"❌ Plotting error: {e}")

def plot_transaction_distribution_by_user_type(conn):
    """Box Plot: Energy Transaction Amounts by User Type"""
    try:
        query = """
            SELECT 
                CASE 
                    WHEN hu.UserID IS NOT NULL THEN 'Household'
                    WHEN bu.UserID IS NOT NULL THEN 'Business'
                END AS user_type,
                et.Energy_Amount
            FROM Energy_Transaction et
            LEFT JOIN Household_User hu ON et.SellerID = hu.UserID
            LEFT JOIN Business_User bu ON et.SellerID = bu.UserID
            WHERE hu.UserID IS NOT NULL OR bu.UserID IS NOT NULL
        """
        df = pd.read_sql(query, conn)
        
        if df.empty:
            print("⚠️ No energy transactions found for users")
            return
            
        plt.figure(figsize=(10,6))
        df.boxplot(column='Energy_Amount', by='user_type', grid=False, patch_artist=True,
                  boxprops=dict(facecolor='#66b3ff', color='black'),
                  whiskerprops=dict(color='black'),
                  capprops=dict(color='black'),
                  medianprops=dict(color='red'))
        plt.title('Energy Transaction Amounts by User Type')
        plt.suptitle('')
        plt.xlabel('User Type')
        plt.ylabel('Energy Amount (kWh)')
        plt.tight_layout()
        plt.savefig('transaction_distribution_by_user_type.png')
        plt.close()
        
    except Exception as e:
        print(f"❌ Plotting error: {e}")

def plot_monthly_revenue(conn):
    """Bar Chart: Monthly Total Revenue"""
    try:
        query = """
            SELECT
                DATE_FORMAT(Transaction_Date, '%Y-%m') AS month,
                SUM(Price) AS total_revenue
            FROM Energy_Transaction
            GROUP BY month
            ORDER BY month
        """
        df = pd.read_sql(query, conn)
        if df.empty:
            print("No data for monthly revenue")
            return

        plt.figure(figsize=(12, 6))
        plt.bar(df['month'], df['total_revenue'], color='#e67e22', edgecolor='white')
        plt.title('Monthly Total Revenue')
        plt.xlabel('Month')
        plt.ylabel('Total Revenue ($)')
        plt.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('monthly_revenue.png')
        plt.close()

    except Exception as e:
        print(f"Plotting error: {e}")

def plot_top_sellers(conn):
    """Horizontal Bar Chart: Top 10 Sellers by Total Energy Sold"""
    try:
        query = """
            SELECT SellerID, SUM(Energy_Amount) AS total_energy_sold
            FROM Energy_Transaction
            GROUP BY SellerID
            ORDER BY total_energy_sold DESC
            LIMIT 10
        """
        df = pd.read_sql(query, conn)
        if df.empty:
            print("No data for top sellers")
            return

        df['SellerID'] = df['SellerID'].astype(int).astype(str)

        plt.figure(figsize=(12, 6))
        plt.barh(df['SellerID'], df['total_energy_sold'], color='#2980b9', edgecolor='white')
        plt.title('Top 10 Sellers by Total Energy Sold')
        plt.xlabel('Total Energy Sold (kWh)')
        plt.ylabel('Seller ID')
        plt.gca().invert_yaxis()
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig('top_sellers.png')
        plt.close()

    except Exception as e:
        print(f"Plotting error: {e}")

# --------------------------
# Simple Database Queries
# --------------------------
def run_simple_queries(conn):
    """Execute simple queries to retrieve basic data from the database"""
    try:
        print("\n1. Total Number of Users:")
        query_household = "SELECT COUNT(*) AS household_count FROM Household_User"
        query_business = "SELECT COUNT(*) AS business_count FROM Business_User"
        
        df_household = pd.read_sql(query_household, conn)
        df_business = pd.read_sql(query_business, conn)
        
        household_count = df_household['household_count'].iloc[0]
        business_count = df_business['business_count'].iloc[0]
        print(f"   - Household Users: {household_count}")
        print(f"   - Business Users: {business_count}")
        print(f"   - Total Users: {household_count + business_count}")
        
        print("\n2. Top 5 Users by Surplus Energy:")
        query_top_surplus = """
            SELECT UserID, Surplus_Energy
            FROM Energy_Profile
            ORDER BY Surplus_Energy DESC
            LIMIT 5
        """
        df_top_surplus = pd.read_sql(query_top_surplus, conn)
        if df_top_surplus.empty:
            print("   - No users found in Energy_Profile")
        else:
            for index, row in df_top_surplus.iterrows():
                print(f"   - UserID: {row['UserID']}, Surplus Energy: {row['Surplus_Energy']} kWh")
        
        print("\n3. Total Number of Energy Transactions:")
        query_transaction_count = "SELECT COUNT(*) AS transaction_count FROM Energy_Transaction"
        df_transaction_count = pd.read_sql(query_transaction_count, conn)
        transaction_count = df_transaction_count['transaction_count'].iloc[0]
        print(f"   - Total Transactions: {transaction_count}")
        
        print("\n4. Most Recent 5 Energy Transactions:")
        query_recent_transactions = """
            SELECT Transaction_ID, SellerID, BuyerID, Energy_Amount, Transaction_Date
            FROM Energy_Transaction
            ORDER BY Transaction_Date DESC
            LIMIT 5
        """
        df_recent_transactions = pd.read_sql(query_recent_transactions, conn)
        if df_recent_transactions.empty:
            print("   - No transactions found in Energy_Transaction")
        else:
            for index, row in df_recent_transactions.iterrows():
                print(f"   - Transaction_ID: {row['Transaction_ID']}, SellerID: {row['SellerID']}, "
                      f"BuyerID: {row['BuyerID']}, Energy: {row['Energy_Amount']} kWh, "
                      f"Date: {row['Transaction_Date']}")
        
    except Exception as e:
        print(f"❌ Query error: {e}")

# --------------------------
# Main Execution with Example Workflow
# --------------------------
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        try:
            # ===== SIMPLE DATABASE QUERIES =====
            print("\n=== SIMPLE DATABASE QUERIES ===")
            run_simple_queries(conn)
            
            # ===== DATA ANALYTICS =====
            print("\n=== GENERATING ANALYTICS ===")
            plot_energy_surplus_trend(conn)
            plot_user_adoption_timeline(conn)
            plot_energy_amount_distribution(conn)
            plot_transaction_distribution_by_user_type(conn)
            plot_monthly_revenue(conn)
            plot_top_sellers(conn)
            
        except Exception as e:
            print(f"⚠️ Unexpected error: {str(e)}")
        finally:
            close_connection(conn)