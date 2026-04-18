// ===== NODE UNIQUENESS CONSTRAINTS =====
// Users
CREATE CONSTRAINT user_id_unique IF NOT EXISTS FOR (u:User) REQUIRE u.userId IS UNIQUE;
CREATE CONSTRAINT household_user_subtype IF NOT EXISTS FOR (u:Household) REQUIRE u.userId IS UNIQUE;
CREATE CONSTRAINT business_user_subtype IF NOT EXISTS FOR (u:Business) REQUIRE u.userId IS UNIQUE;

// Other Entities
CREATE CONSTRAINT profile_id_unique IF NOT EXISTS FOR (p:EnergyProfile) REQUIRE p.profileId IS UNIQUE;
CREATE CONSTRAINT region_id_unique IF NOT EXISTS FOR (r:Region) REQUIRE r.regionId IS UNIQUE;
CREATE CONSTRAINT employee_id_unique IF NOT EXISTS FOR (e:Employee) REQUIRE e.employeeId IS UNIQUE;
CREATE CONSTRAINT transaction_id_unique IF NOT EXISTS FOR (t:EnergyTransaction) REQUIRE t.transactionId IS UNIQUE;
CREATE CONSTRAINT payment_id_unique IF NOT EXISTS FOR (p:Payment) REQUIRE p.paymentId IS UNIQUE;
CREATE CONSTRAINT complaint_id_unique IF NOT EXISTS FOR (c:Complaint) REQUIRE c.complaintId IS UNIQUE;
CREATE CONSTRAINT grid_id_unique IF NOT EXISTS FOR (g:Grid) REQUIRE g.connectionId IS UNIQUE;

// ===== RELATIONSHIP CONSTRAINTS =====
// Ensure 1:1 relationships
CREATE CONSTRAINT user_has_one_profile IF NOT EXISTS
FOR (u:User)-[r:HAS_PROFILE]->(p:EnergyProfile)
REQUIRE r IS UNIQUE;

// ===== EXISTENCE CONSTRAINTS (Optional) =====
// For required properties
CREATE CONSTRAINT user_email_exists IF NOT EXISTS
FOR (u:User) REQUIRE u.email IS NOT NULL;

CREATE CONSTRAINT transaction_amount_exists IF NOT EXISTS
FOR (t:EnergyTransaction) REQUIRE t.energyAmount IS NOT NULL;