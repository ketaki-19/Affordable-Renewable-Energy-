from solshareNeo4J_config import Neo4jConnector

def load_full_data():
    queries = [
        # Region nodes
        """UNWIND [
            {regionId: 1, geographicalCondition: 'Urban', supervisorId: 1002, regionName: 'Eastern Boston'},
            {regionId: 2, geographicalCondition: 'Suburban', supervisorId: 1003, regionName: 'Western Cambridge'},
            {regionId: 3, geographicalCondition: 'Rural', supervisorId: 1004, regionName: 'Northern Worcester'},
            {regionId: 4, geographicalCondition: 'Coastal', supervisorId: 1005, regionName: 'Southern Salem'},
            {regionId: 5, geographicalCondition: 'Inland', supervisorId: 1006, regionName: 'Central Lowell'},
            {regionId: 6, geographicalCondition: 'Mountain', supervisorId: 1007, regionName: 'Highland Newton'}
        ] AS r
        CREATE (:Region {
            regionId: r.regionId,
            geographicalCondition: r.geographicalCondition,
            supervisorId: r.supervisorId,
            regionName: r.regionName
        })""",

        # Employee nodes
        """UNWIND [
            {employeeId: 1001, name: 'John Manager', email: 'john.manager@example.com', phone: '617-555-1111', managerId: 1001},
            {employeeId: 1002, name: 'Lisa Supervisor', email: 'lisa.supervisor@example.com', phone: '617-555-2222', managerId: 1001},
            {employeeId: 1003, name: 'Mark Coordinator', email: 'mark.coordinator@example.com', phone: '617-555-3333', managerId: 1001},
            {employeeId: 1004, name: 'Nina Analyst', email: 'nina.analyst@example.com', phone: '617-555-4444', managerId: 1001},
            {employeeId: 1005, name: 'Oscar Operator', email: 'oscar.operator@example.com', phone: '617-555-5555', managerId: 1002},
            {employeeId: 1006, name: 'Paul Executive', email: 'paul.executive@example.com', phone: '617-555-6666', managerId: 1002},
            {employeeId: 1007, name: 'Queen Executive', email: 'queen.executive@example.com', phone: '617-555-7777', managerId: 1002},
            {employeeId: 1008, name: 'Rick Director', email: 'rick.director@example.com', phone: '617-555-8888', managerId: 1003},
            {employeeId: 1009, name: 'Susan Director', email: 'susan.director@example.com', phone: '617-555-9999', managerId: 1003},
            {employeeId: 1010, name: 'Tom Manager', email: 'tom.manager@example.com', phone: '617-555-1010', managerId: 1001}
        ] AS e
        CREATE (:Employee {
            employeeId: e.employeeId,
            name: e.name,
            email: e.email,
            phone: e.phone
        })""",

        # Household User nodes
        """UNWIND [
            {userId: 54321, name: 'Alice Johnson', email: 'alice.johnson@example.com', phone: '617-555-0101',
             consumptionRate: 150.75, address: '123 Main St, Boston, MA, USA', renewableCapacity: 25.50, regionId: 3},
            {userId: 54322, name: 'Brian Smith', email: 'brian.smith@example.com', phone: '617-555-0102',
             consumptionRate: 160.20, address: '456 Elm St, Cambridge, MA, USA', renewableCapacity: 30.00, regionId: 1},
            {userId: 54323, name: 'Carol Davis', email: 'carol.davis@example.com', phone: '617-555-0103',
             consumptionRate: 140.00, address: '789 Oak St, Worcester, MA, USA', renewableCapacity: 22.30, regionId: 6},
            {userId: 54324, name: 'David Brown', email: 'david.brown@example.com', phone: '617-555-0104',
             consumptionRate: 180.45, address: '101 Pine St, Springfield, MA, USA', renewableCapacity: 35.00, regionId: 2},
            {userId: 54325, name: 'Emily Wilson', email: 'emily.wilson@example.com', phone: '617-555-0105',
             consumptionRate: 200.00, address: '202 Maple Ave, Lowell, MA, USA', renewableCapacity: 28.75, regionId: 4},
            {userId: 54326, name: 'Frank Miller', email: 'frank.miller@example.com', phone: '617-555-0106',
             consumptionRate: 175.50, address: '303 Cedar Rd, Lawrence, MA, USA', renewableCapacity: 20.50, regionId: 5},
            {userId: 54327, name: 'Grace Taylor', email: 'grace.taylor@example.com', phone: '617-555-0107',
             consumptionRate: 190.00, address: '404 Birch Ln, Newton, MA, USA', renewableCapacity: 33.00, regionId: 1},
            {userId: 54328, name: 'Henry Anderson', email: 'henry.anderson@example.com', phone: '617-555-0108',
             consumptionRate: 165.25, address: '505 Walnut St, Quincy, MA, USA', renewableCapacity: 27.00, regionId: 2},
            {userId: 54329, name: 'Irene Thomas', email: 'irene.thomas@example.com', phone: '617-555-0109',
             consumptionRate: 155.75, address: '606 Cherry Ave, Brockton, MA, USA', renewableCapacity: 26.50, regionId: 3},
            {userId: 54330, name: 'Jack Moore', email: 'jack.moore@example.com', phone: '617-555-0110',
             consumptionRate: 185.00, address: '707 Poplar Dr, Fall River, MA, USA', renewableCapacity: 32.00, regionId: 6},
            {userId: 54331, name: 'Karen Martin', email: 'karen.martin@example.com', phone: '617-555-0111',
             consumptionRate: 170.50, address: '808 Ash St, Lynn, MA, USA', renewableCapacity: 21.50, regionId: 5},
            {userId: 54332, name: 'Larry Jackson', email: 'larry.jackson@example.com', phone: '617-555-0112',
             consumptionRate: 160.00, address: '909 Chestnut St, New Bedford, MA, USA', renewableCapacity: 23.75, regionId: 4},
            {userId: 54333, name: 'Monica White', email: 'monica.white@example.com', phone: '617-555-0113',
             consumptionRate: 210.00, address: '111 Spruce St, Salem, MA, USA', renewableCapacity: 40.00, regionId: 2},
            {userId: 54334, name: 'Nathan Harris', email: 'nathan.harris@example.com', phone: '617-555-0114',
             consumptionRate: 195.00, address: '222 Fir St, Framingham, MA, USA', renewableCapacity: 34.50, regionId: 1},
            {userId: 54335, name: 'Olivia Clark', email: 'olivia.clark@example.com', phone: '617-555-0115',
             consumptionRate: 180.00, address: '333 Willow Ln, Peabody, MA, USA', renewableCapacity: 29.00, regionId: 6},
            {userId: 54336, name: 'Peter Lewis', email: 'peter.lewis@example.com', phone: '617-555-0116',
             consumptionRate: 165.00, address: '444 Sycamore Ave, Medford, MA, USA', renewableCapacity: 25.00, regionId: 3},
            {userId: 54337, name: 'Quinn Robinson', email: 'quinn.robinson@example.com', phone: '617-555-0117',
             consumptionRate: 155.00, address: '555 Cypress Rd, Waltham, MA, USA', renewableCapacity: 20.00, regionId: 4},
            {userId: 54338, name: 'Rachel Walker', email: 'rachel.walker@example.com', phone: '617-555-0118',
             consumptionRate: 175.00, address: '666 Redwood Blvd, Malden, MA, USA', renewableCapacity: 30.25, regionId: 5},
            {userId: 54339, name: 'Steven Hall', email: 'steven.hall@example.com', phone: '617-555-0119',
             consumptionRate: 185.25, address: '777 Sequoia St, Everett, MA, USA', renewableCapacity: 27.75, regionId: 2},
            {userId: 54340, name: 'Tina Allen', email: 'tina.allen@example.com', phone: '617-555-0120',
             consumptionRate: 160.75, address: '888 Magnolia Ave, Revere, MA, USA', renewableCapacity: 24.50, regionId: 1}
        ] AS u
        CREATE (:User:Household {
            userId: u.userId,
            name: u.name,
            email: u.email,
            phone: u.phone,
            consumptionRate: u.consumptionRate,
            address: u.address,
            renewableCapacity: u.renewableCapacity
        })""",

        # Business User nodes
        """UNWIND [
            {userId: 54341, name: 'Acme Corporation', email: 'acme.corporation@example.com', phone: '617-555-0201',
             consumptionRate: 210.00, address: '10 Corporate Plaza, Boston, MA, USA', renewableCapacity: 35.50, regionId: 4},
            {userId: 54342, name: 'Beta Solutions', email: 'beta.solutions@example.com', phone: '617-555-0202',
             consumptionRate: 220.00, address: '20 Business Rd, Cambridge, MA, USA', renewableCapacity: 36.00, regionId: 2},
            {userId: 54343, name: 'Gamma Industries', email: 'gamma.industries@example.com', phone: '617-555-0203',
             consumptionRate: 205.50, address: '30 Industrial Way, Worcester, MA, USA', renewableCapacity: 34.25, regionId: 6},
            {userId: 54344, name: 'Delta Enterprises', email: 'delta.enterprises@example.com', phone: '617-555-0204',
             consumptionRate: 215.75, address: '40 Commerce St, Springfield, MA, USA', renewableCapacity: 33.00, regionId: 3},
            {userId: 54345, name: 'Epsilon Trading', email: 'epsilon.trading@example.com', phone: '617-555-0205',
             consumptionRate: 230.00, address: '50 Market Ave, Lowell, MA, USA', renewableCapacity: 38.00, regionId: 1},
            {userId: 54346, name: 'Zeta Logistics', email: 'zeta.logistics@example.com', phone: '617-555-0206',
             consumptionRate: 240.50, address: '60 Innovation Dr, Lawrence, MA, USA', renewableCapacity: 37.50, regionId: 5},
            {userId: 54347, name: 'Eta Manufacturing', email: 'eta.manufacturing@example.com', phone: '617-555-0207',
             consumptionRate: 225.25, address: '70 Enterprise Blvd, Newton, MA, USA', renewableCapacity: 32.50, regionId: 2},
            {userId: 54348, name: 'Theta Services', email: 'theta.services@example.com', phone: '617-555-0208',
             consumptionRate: 235.00, address: '80 Venture St, Quincy, MA, USA', renewableCapacity: 39.00, regionId: 1},
            {userId: 54349, name: 'Iota Retail', email: 'iota.retail@example.com', phone: '617-555-0209',
             consumptionRate: 210.75, address: '90 Executive Ave, Brockton, MA, USA', renewableCapacity: 31.50, regionId: 6},
            {userId: 54350, name: 'Kappa Technologies', email: 'kappa.technologies@example.com', phone: '617-555-0210',
             consumptionRate: 220.50, address: '100 Trade St, Fall River, MA, USA', renewableCapacity: 30.00, regionId: 3},
            {userId: 54351, name: 'Lambda Consulting', email: 'lambda.consulting@example.com', phone: '617-555-0211',
             consumptionRate: 215.00, address: '110 Office Park, Lynn, MA, USA', renewableCapacity: 35.00, regionId: 5},
            {userId: 54352, name: 'Mu Investments', email: 'mu.investments@example.com', phone: '617-555-0212',
             consumptionRate: 230.25, address: '120 Commerce Pkwy, New Bedford, MA, USA', renewableCapacity: 36.50, regionId: 4},
            {userId: 54353, name: 'Nu Energy', email: 'nu.energy@example.com', phone: '617-555-0213',
             consumptionRate: 240.00, address: '130 Business Loop, Salem, MA, USA', renewableCapacity: 38.25, regionId: 2},
            {userId: 54354, name: 'Xi Systems', email: 'xi.systems@example.com', phone: '617-555-0214',
             consumptionRate: 225.75, address: '140 Corporate Ct, Framingham, MA, USA', renewableCapacity: 33.75, regionId: 3},
            {userId: 54355, name: 'Omicron Holdings', email: 'omicron.holdings@example.com', phone: '617-555-0215',
             consumptionRate: 235.25, address: '150 Innovation Way, Peabody, MA, USA', renewableCapacity: 34.50, regionId: 1},
            {userId: 54356, name: 'Pi Innovations', email: 'pi.innovations@example.com', phone: '617-555-0216',
             consumptionRate: 210.50, address: '160 Executive Blvd, Medford, MA, USA', renewableCapacity: 32.00, regionId: 6},
            {userId: 54357, name: 'Rho Electronics', email: 'rho.electronics@example.com', phone: '617-555-0217',
             consumptionRate: 220.75, address: '170 Enterprise Ave, Waltham, MA, USA', renewableCapacity: 31.25, regionId: 4},
            {userId: 54358, name: 'Sigma Foods', email: 'sigma.foods@example.com', phone: '617-555-0218',
             consumptionRate: 215.50, address: '180 Trade Rd, Malden, MA, USA', renewableCapacity: 30.75, regionId: 5},
            {userId: 54359, name: 'Tau Construction', email: 'tau.construction@example.com', phone: '617-555-0219',
             consumptionRate: 230.50, address: '190 Market St, Everett, MA, USA', renewableCapacity: 37.00, regionId: 2},
            {userId: 54360, name: 'Upsilon Media', email: 'upsilon.media@example.com', phone: '617-555-0220',
             consumptionRate: 240.25, address: '200 Corporate Dr, Revere, MA, USA', renewableCapacity: 36.25, regionId: 3}
        ] AS u
        CREATE (:User:Business {
            userId: u.userId,
            name: u.name,
            email: u.email,
            phone: u.phone,
            consumptionRate: u.consumptionRate,
            address: u.address,
            renewableCapacity: u.renewableCapacity
        })""",

        # MEMBER_OF relationships (Users to Grid)
        """UNWIND [
            {userId: 54321, connectionId: 8001},
            {userId: 54322, connectionId: 8001},
            {userId: 54323, connectionId: 8001},
            {userId: 54324, connectionId: 8002},
            {userId: 54325, connectionId: 8002},
            {userId: 54326, connectionId: 8002},
            {userId: 54327, connectionId: 8003},
            {userId: 54328, connectionId: 8003},
            {userId: 54329, connectionId: 8003},
            {userId: 54330, connectionId: 8004},
            {userId: 54331, connectionId: 8004},
            {userId: 54332, connectionId: 8004},
            {userId: 54333, connectionId: 8005},
            {userId: 54334, connectionId: 8005},
            {userId: 54335, connectionId: 8005},
            {userId: 54336, connectionId: 8006},
            {userId: 54337, connectionId: 8006},
            {userId: 54338, connectionId: 8006},
            {userId: 54339, connectionId: 8007},
            {userId: 54340, connectionId: 8007},
            {userId: 54341, connectionId: 8007},
            {userId: 54342, connectionId: 8008},
            {userId: 54343, connectionId: 8008},
            {userId: 54344, connectionId: 8008},
            {userId: 54345, connectionId: 8009},
            {userId: 54346, connectionId: 8009},
            {userId: 54347, connectionId: 8009},
            {userId: 54348, connectionId: 8010},
            {userId: 54349, connectionId: 8010},
            {userId: 54350, connectionId: 8010},
            {userId: 54351, connectionId: 8011},
            {userId: 54352, connectionId: 8011},
            {userId: 54353, connectionId: 8011},
            {userId: 54354, connectionId: 8012},
            {userId: 54355, connectionId: 8012},
            {userId: 54356, connectionId: 8012},
            {userId: 54357, connectionId: 8013},
            {userId: 54358, connectionId: 8013},
            {userId: 54359, connectionId: 8013},
            {userId: 54360, connectionId: 8014}
        ] AS m
        MATCH (u:User {userId: m.userId}), (g:Grid {connectionId: m.connectionId})
        CREATE (u)-[:MEMBER_OF]->(g)""",

        # EnergyProfile nodes and HAS_PROFILE relationships
        """UNWIND [
            {profileId: 1, userId: 54321, energyProduced: 160.00, energyConsumed: 150.75, surplusEnergy: 9.25},
            {profileId: 2, userId: 54322, energyProduced: 170.00, energyConsumed: 160.20, surplusEnergy: 9.80},
            {profileId: 3, userId: 54323, energyProduced: 150.00, energyConsumed: 140.00, surplusEnergy: 10.00},
            {profileId: 4, userId: 54324, energyProduced: 190.00, energyConsumed: 180.45, surplusEnergy: 9.55},
            {profileId: 5, userId: 54325, energyProduced: 210.00, energyConsumed: 200.00, surplusEnergy: 10.00},
            {profileId: 6, userId: 54326, energyProduced: 185.00, energyConsumed: 175.50, surplusEnergy: 9.50},
            {profileId: 7, userId: 54327, energyProduced: 200.00, energyConsumed: 190.00, surplusEnergy: 10.00},
            {profileId: 8, userId: 54328, energyProduced: 175.00, energyConsumed: 165.25, surplusEnergy: 9.75},
            {profileId: 9, userId: 54329, energyProduced: 165.00, energyConsumed: 155.75, surplusEnergy: 9.25},
            {profileId: 10, userId: 54330, energyProduced: 195.00, energyConsumed: 185.00, surplusEnergy: 10.00},
            {profileId: 11, userId: 54331, energyProduced: 180.00, energyConsumed: 170.50, surplusEnergy: 9.50},
            {profileId: 12, userId: 54332, energyProduced: 170.00, energyConsumed: 160.00, surplusEnergy: 10.00},
            {profileId: 13, userId: 54333, energyProduced: 220.00, energyConsumed: 210.00, surplusEnergy: 10.00},
            {profileId: 14, userId: 54334, energyProduced: 205.00, energyConsumed: 195.00, surplusEnergy: 10.00},
            {profileId: 15, userId: 54335, energyProduced: 190.00, energyConsumed: 180.00, surplusEnergy: 10.00},
            {profileId: 16, userId: 54336, energyProduced: 175.00, energyConsumed: 165.00, surplusEnergy: 10.00},
            {profileId: 17, userId: 54337, energyProduced: 165.00, energyConsumed: 155.00, surplusEnergy: 10.00},
            {profileId: 18, userId: 54338, energyProduced: 185.00, energyConsumed: 175.00, surplusEnergy: 10.00},
            {profileId: 19, userId: 54339, energyProduced: 195.00, energyConsumed: 185.25, surplusEnergy: 9.75},
            {profileId: 20, userId: 54340, energyProduced: 170.00, energyConsumed: 160.75, surplusEnergy: 9.25},
            {profileId: 21, userId: 54341, energyProduced: 215.00, energyConsumed: 210.00, surplusEnergy: 5.00},
            {profileId: 22, userId: 54342, energyProduced: 225.00, energyConsumed: 220.00, surplusEnergy: 5.00},
            {profileId: 23, userId: 54343, energyProduced: 210.00, energyConsumed: 205.50, surplusEnergy: 4.50},
            {profileId: 24, userId: 54344, energyProduced: 220.00, energyConsumed: 215.75, surplusEnergy: 4.25},
            {profileId: 25, userId: 54345, energyProduced: 235.00, energyConsumed: 230.00, surplusEnergy: 5.00},
            {profileId: 26, userId: 54346, energyProduced: 245.00, energyConsumed: 240.50, surplusEnergy: 4.50},
            {profileId: 27, userId: 54347, energyProduced: 230.00, energyConsumed: 225.25, surplusEnergy: 4.75},
            {profileId: 28, userId: 54348, energyProduced: 240.00, energyConsumed: 235.00, surplusEnergy: 5.00},
            {profileId: 29, userId: 54349, energyProduced: 215.00, energyConsumed: 210.75, surplusEnergy: 4.25},
            {profileId: 30, userId: 54350, energyProduced: 225.00, energyConsumed: 220.50, surplusEnergy: 4.50},
            {profileId: 31, userId: 54351, energyProduced: 220.00, energyConsumed: 215.00, surplusEnergy: 5.00},
            {profileId: 32, userId: 54352, energyProduced: 235.00, energyConsumed: 230.25, surplusEnergy: 4.75},
            {profileId: 33, userId: 54353, energyProduced: 245.00, energyConsumed: 240.00, surplusEnergy: 5.00},
            {profileId: 34, userId: 54354, energyProduced: 230.00, energyConsumed: 225.75, surplusEnergy: 4.25},
            {profileId: 35, userId: 54355, energyProduced: 240.00, energyConsumed: 235.25, surplusEnergy: 4.75},
            {profileId: 36, userId: 54356, energyProduced: 215.00, energyConsumed: 210.50, surplusEnergy: 4.50},
            {profileId: 37, userId: 54357, energyProduced: 225.00, energyConsumed: 220.75, surplusEnergy: 4.25},
            {profileId: 38, userId: 54358, energyProduced: 220.00, energyConsumed: 215.50, surplusEnergy: 4.50},
            {profileId: 39, userId: 54359, energyProduced: 235.00, energyConsumed: 230.50, surplusEnergy: 4.50},
            {profileId: 40, userId: 54360, energyProduced: 245.00, energyConsumed: 240.25, surplusEnergy: 4.75}
        ] AS ep
        MATCH (u:User {userId: ep.userId})
        CREATE (u)-[:HAS_PROFILE]->(:EnergyProfile {
            profileId: ep.profileId,
            energyProduced: ep.energyProduced,
            energyConsumed: ep.energyConsumed,
            surplusEnergy: ep.surplusEnergy
        })""",

        # EnergyTransaction nodes and relationships
        """UNWIND [
            {transactionId: 5001, date: '2025-03-01', buyerId: 54321, sellerId: 54341, energyAmount: 50.00, price: 100.00},
            {transactionId: 5002, date: '2025-03-01', buyerId: 54322, sellerId: 54342, energyAmount: 55.00, price: 110.00},
            {transactionId: 5003, date: '2025-03-01', buyerId: 54323, sellerId: 54343, energyAmount: 60.00, price: 120.00},
            {transactionId: 5004, date: '2025-03-01', buyerId: 54324, sellerId: 54344, energyAmount: 65.00, price: 130.00},
            {transactionId: 5005, date: '2025-03-01', buyerId: 54325, sellerId: 54345, energyAmount: 70.00, price: 140.00},
            {transactionId: 5006, date: '2025-03-01', buyerId: 54326, sellerId: 54346, energyAmount: 75.00, price: 150.00},
            {transactionId: 5007, date: '2025-03-02', buyerId: 54327, sellerId: 54347, energyAmount: 80.00, price: 160.00},
            {transactionId: 5008, date: '2025-03-02', buyerId: 54328, sellerId: 54348, energyAmount: 85.00, price: 170.00},
            {transactionId: 5009, date: '2025-03-02', buyerId: 54329, sellerId: 54349, energyAmount: 90.00, price: 180.00},
            {transactionId: 5010, date: '2025-03-02', buyerId: 54330, sellerId: 54350, energyAmount: 95.00, price: 190.00},
            {transactionId: 5011, date: '2025-03-03', buyerId: 54331, sellerId: 54351, energyAmount: 100.00, price: 200.00},
            {transactionId: 5012, date: '2025-03-03', buyerId: 54332, sellerId: 54352, energyAmount: 105.00, price: 210.00},
            {transactionId: 5013, date: '2025-03-03', buyerId: 54333, sellerId: 54353, energyAmount: 110.00, price: 220.00},
            {transactionId: 5014, date: '2025-03-03', buyerId: 54334, sellerId: 54354, energyAmount: 115.00, price: 230.00},
            {transactionId: 5015, date: '2025-03-04', buyerId: 54335, sellerId: 54355, energyAmount: 120.00, price: 240.00},
            {transactionId: 5016, date: '2025-03-04', buyerId: 54336, sellerId: 54356, energyAmount: 125.00, price: 250.00},
            {transactionId: 5017, date: '2025-03-04', buyerId: 54337, sellerId: 54357, energyAmount: 130.00, price: 260.00},
            {transactionId: 5018, date: '2025-03-04', buyerId: 54338, sellerId: 54358, energyAmount: 135.00, price: 270.00},
            {transactionId: 5019, date: '2025-03-05', buyerId: 54339, sellerId: 54359, energyAmount: 140.00, price: 280.00},
            {transactionId: 5020, date: '2025-03-05', buyerId: 54340, sellerId: 54360, energyAmount: 145.00, price: 290.00},
            {transactionId: 5021, date: '2025-03-05', buyerId: 54321, sellerId: 54342, energyAmount: 55.50, price: 111.00},
            {transactionId: 5022, date: '2025-03-05', buyerId: 54322, sellerId: 54343, energyAmount: 60.50, price: 121.00},
            {transactionId: 5023, date: '2025-03-06', buyerId: 54323, sellerId: 54344, energyAmount: 65.50, price: 131.00},
            {transactionId: 5024, date: '2025-03-06', buyerId: 54324, sellerId: 54345, energyAmount: 70.50, price: 141.00},
            {transactionId: 5025, date: '2025-03-06', buyerId: 54325, sellerId: 54346, energyAmount: 75.50, price: 151.00},
            {transactionId: 5026, date: '2025-03-06', buyerId: 54326, sellerId: 54347, energyAmount: 80.50, price: 161.00},
            {transactionId: 5027, date: '2025-03-07', buyerId: 54327, sellerId: 54348, energyAmount: 85.50, price: 171.00},
            {transactionId: 5028, date: '2025-03-07', buyerId: 54328, sellerId: 54349, energyAmount: 90.50, -----
            {transactionId: 5150, date: '2025-10-13', buyerId: 54410, sellerId: 54414, energyAmount: 498.75, price: 997.50}
        ] AS t
        CREATE (tNode:EnergyTransaction {
            transactionId: t.transactionId,
            date: date(t.date),
            energyAmount: t.energyAmount,
            price: t.price
        })
        WITH t, tNode
        MATCH (buyer:User {userId: t.buyerId}), (seller:User {userId: t.sellerId})
        CREATE (buyer)-[:BOUGHT_FROM]->(tNode)<-[:SOLD_TO]-(seller)""",

        # Payment nodes and HAS_PAYMENT relationships
        """UNWIND [
            {paymentId: 6001, transactionId: 5001, date: '2025-03-02', status: 'Completed', amount: 100.00},
            {paymentId: 6002, transactionId: 5002, date: '2025-03-02', status: 'Completed', amount: 110.00},
            {paymentId: 6003, transactionId: 5003, date: '2025-03-02', status: 'Completed', amount: 120.00},
            {paymentId: 6004, transactionId: 5004, date: '2025-03-02', status: 'Completed', amount: 130.00},
            {paymentId: 6005, transactionId: 5005, date: '2025-03-02', status: 'Completed', amount: 140.00},
            {paymentId: 6006, transactionId: 5006, date: '2025-03-02', status: 'Completed', amount: 150.00},
            {paymentId: 6007, transactionId: 5007, date: '2025-03-03', status: 'Completed', amount: 160.00},
            {paymentId: 6008, transactionId: 5008, date: '2025-03-03', status: 'Completed', amount: 170.00},
            {paymentId: 6009, transactionId: 5009, date: '2025-03-03', status: 'Completed', amount: 180.00},
            {paymentId: 6010, transactionId: 5010, date: '2025-03-03', status: 'Completed', amount: 190.00},
            {paymentId: 6011, transactionId: 5011, date: '2025-03-04', status: 'Completed', amount: 200.00},
            {paymentId: 6012, transactionId: 5012, date: '2025-03-04', status: 'Completed', amount: 210.00},
            {paymentId: 6013, transactionId: 5013, date: '2025-03-04', status: 'Completed', amount: 220.00},
            {paymentId: 6014, transactionId: 5014, date: '2025-03-04', status: 'Completed', amount: 230.00},
            {paymentId: 6015, transactionId: 5015, date: '2025-03-05', status: 'Completed', amount: 240.00},
            {paymentId: 6016, transactionId: 5016, date: '2025-03-05', status: 'Completed', amount: 250.00},
            {paymentId: 6017, transactionId: 5017, date: '2025-03-05', status: 'Completed', amount: 260.00},
            {paymentId: 6018, transactionId: 5018, date: '2025-03-05', status: 'Completed', amount lymphocytes: 270.00},
            {paymentId: 6019, transactionId: 5019, date: '2025-03-06', status: 'Completed', amount: 280.00},
            {paymentId: 6020, transactionId: 5020, date: '2025-03-06', status: 'Completed', amount: 290.00},
            {paymentId: 6021, transactionId: 5021, date: '2025-03-06', status: 'Completed', amount: 111.00},
            {paymentId: 6022, transactionId: 5022, date: '2025-03-06', status: 'Completed', amount: 121.00},
            {paymentId: 6023, transactionId: 5023, date: '2025-03-06', status: 'Completed', amount: 131.00},
            {paymentId: 6024, transactionId: 5024, date: '2025-03-06', status: 'Completed', amount: 141.00},
            {paymentId: 6025, transactionId: 5025, date: '2025-03-06', status: 'Completed', amount: 151.00},
            {paymentId: 6026, transactionId: 5026, date: '2025-03-06', status: 'Completed', amount: 161.00},
            {paymentId: 6027, transactionId: 5027, date: '2025-03-07', status: 'Completed', amount: 171.00},
            {paymentId: 6028, transactionId: 5028, date: '2025-03-07', status: 'Completed', amount: 181.00},
            {paymentId: 6029, transactionId: 5029, date: '2025-03-07', status: 'Completed', amount: 191.00},
            {paymentId: 6030, transactionId: 5030, date: '2025-03-07', status: 'Completed', amount: 201.00},
            {paymentId: 6031, transactionId: 5031, date: '2025-03-08', status: 'Completed', amount: 211.00},
            {paymentId: 6032, transactionId: 5032, date: '2025-03-08', status: 'Completed', amount: 221.00},
            {paymentId: 6033, transactionId: 5033, date: '2025-03-08', status: 'Completed', amount: 231.00},
            {paymentId: 6034, transactionId: 5034, date: '2025-03-08', status: 'Completed', amount: 241.00},
            {paymentId: 6035, transactionId: 5035, date: '2025-03-09', status: 'Completed', amount: 251.00},
            {paymentId: 6036, transactionId: 5036, date: '2025-03-09', status: 'Completed', amount: 261.00},
            {paymentId: 6037, transactionId: 5037, date: '2025-03-09', status: 'Completed', amount: 271.00},
            {paymentId: 6038, transactionId: 5038, date: '2025-03-09', status: 'Completed', amount: 281.00},
            {paymentId: 6039, transactionId: 5039, date: '2025-03-10', status: 'Completed', amount: 291.00},
            {paymentId: 6040, transactionId: 5040, date: '2025-03-10', status: 'Completed', amount: 301.00},
            {paymentId: 6041, transactionId: 5041, date: '2025-03-11', status: 'Completed', amount: 104.50},
            {paymentId: 6042, transactionId: 5042, date: '2025-03-11', status: 'Completed', amount: 114.50},
            {paymentId: 6043, transactionId: 5043, date: '2025-03-11', status: 'Completed', amount: 124.50},
            {paymentId: 6044, transactionId: 5044, date: '2025-03-11', status: 'Completed', amount: 134.50},
            {paymentId: 6045, transactionId: 5045, date: '2025-03-11', status: 'Completed', amount: 144.50},
            {paymentId: 6046, transactionId: 5046, date: '2025-03-11', status: 'Completed', amount: 154.50},
            {paymentId: 6047, transactionId: 5047, date: '2025-03-11', status: 'Completed', amount: 164.50},
            {paymentId: 6048, transactionId: 5048, date: '2025-03-11', status: 'Completed', amount: 174.50},
            {paymentId: 6049, transactionId: 5049, date: '2025-03-11', status: 'Completed', amount: 184.50},
            {paymentId: 6050, transactionId: 5050, date: '2025-03-11', status: 'Completed', amount: 194.50},
            {paymentId: 6051, transactionId: 5051, date: '2025-03-12', status: 'Completed', amount: 204.50},
            {paymentId: 6052, transactionId: 5052, date: '2025-03-12', status: 'Completed', amount: 214.50},
            {paymentId: 6053, transactionId: 5053, date: '2025-03-12', status: 'Completed', amount: 224.50},
            {paymentId: 6054, transactionId: 5054, date: '2025-03-12', status: 'Completed', amount: 234.50},
            {paymentId: 6055, transactionId: 5055, date: '2025-03-12', status: 'Completed', amount: 244.50},
            {paymentId: 6056, transactionId: 5056, date: '2025-03-12', status: 'Completed', amount: 254.50},
            {paymentId: 6057, transactionId: 5057, date: '2025-03-12', status: 'Completed', amount: 264.50},
            {paymentId: 6058, transactionId: 5058, date: '2025-03-12', status: 'Completed', amount: 274.50},
            {paymentId: 6059, transactionId: 5059, date: '2025-03-12', status: 'Completed', amount: 284.50},
            {paymentId: 6060, transactionId: 5060, date: '2025-03-12', status: 'Completed', amount: 294.50},
            {paymentId: 6061, transactionId: 5061, date: '2025-03-13', status: 'Completed', amount: 107.50},
            {paymentId: 6062, transactionId: 5062, date: '2025-03-13', status: 'Completed', amount: 117.50},
            {paymentId: 6063, transactionId: 5063, date: '2025-03-13', status: 'Completed', amount: 127.50},
            {paymentId: 6064, transactionId: 5064, date: '2025-03-13', status: 'Completed', amount: 137.50},
            {paymentId: 6065, transactionId: 5065, date: '2025-03-13', status: 'Completed', amount: 147.50},
            {paymentId: 6066, transactionId: 5066, date: '2025-03-13', status: 'Completed', amount: 157.50},
            {paymentId: 6067, transactionId: 5067, date: '2025-03-13', status: 'Completed', amount: 167.50},
            {paymentId: 6068, transactionId: 5068, date: '2025-03-13', status: 'Completed', amount: 177.50},
            {paymentId: 6069, transactionId: 5069, date: '2025-03-13', status: 'Completed', amount: 187.50},
            {paymentId: 6070, transactionId: 5070, date: '2025-03-13', status: 'Completed', amount: 197.50},
            {paymentId: 6071, transactionId: 5071, date: '2025-03-14', status: 'Completed', amount: 207.50},
            {paymentId: 6072, transactionId: 5072, date: '2025-03-14', status: 'Completed', amount: 217.50},
            {paymentId: 6073, transactionId: 5073, date: '2025-03-14', status: 'Completed', amount: 227.50},
            {paymentId: 6074, transactionId: 5074, date: '2025-03-14', status: 'Completed', amount: 237.50},
            {paymentId: 6075, transactionId: 5075, date: '2025-03-14', status: 'Completed', amount: 247.50},
            {paymentId: 6076, transactionId: 5076, date: '2025-03-14', status: 'Completed', amount: 257.50},
            {paymentId: 6077, transactionId: 5077, date: '2025-03-14', status: 'Completed', amount: 267.50},
            {paymentId: 6078, transactionId: 5078, date: '2025-03-14', status: 'Completed', amount: 277.50},
            {paymentId: 6079, transactionId: 5079, date: '2025-03-14', status: 'Completed', amount: 287.50},
            {paymentId: 6080, transactionId: 5080, date: '2025-03-14', status: 'Completed', amount: 297.50}
        ] AS p
        MATCH (t:EnergyTransaction {transactionId: p.transactionId})
        CREATE (t)-[:HAS_PAYMENT]->(:Payment {
            paymentId: p.paymentId,
            date: date(p.date),
            status: p.status,
            amount: p.amount
        })""",

        # Complaint nodes and relationships
        """UNWIND [
            {complaintId: 7001, userId: 54321, date: '2025-03-15', description: 'Billing error', employeeId: 1002, 
             status: 'Resolved', resolutionDate: '2025-03-16'},
            {complaintId: 7002, userId: 54322, date: '2025-03-16', description: 'Service outage', employeeId: 1003, 
             status: 'Pending', resolutionDate: NULL},
            {paymentId: 7003, complaintId: 54323, date: '2025-03-17', description: 'Meter malfunction', employeeId: 1004, 
             status: 'Resolved', resolutionDate: '2025-03-18'},
            {complaintId: 7004, userId: 54324, date: '2025-03-18', description: 'Incorrect charges', employeeId: 1005, 
             status: 'Resolved', resolutionDate: '2025-03-19'},
            {complaintId: 7005, userId: 54325, date: '2025-03-19', description: 'Customer service issue', employeeId: 1002, 
             status: 'Pending', resolutionDate: NULL},
            {complaintId: 7006, userId: 54326, date: '2025-03-20', description: 'Delayed response', employeeId: 1006, 
             status: 'Resolved', resolutionDate: '2025-03-21'},
            {complaintId: 7007, userId: 54327, date: '2025-03-21', description: 'Overbilling', employeeId: 1007, 
             status: 'Pending', resolutionDate: NULL},
            {complaintId: 7008, userId: 54328, date: '2025-03-22', description: 'Technical issue', employeeId: 1008, 
             status: 'Resolved', resolutionDate: '2025-03-23'},
            {complaintId: 7009, userId: 54329, date: '2025-03-23', description: 'Installation error', employeeId: 1009, 
             status: 'Resolved', resolutionDate: '2025-03-24'},
            {complaintId: 7010, userId: 54330, date: '2025-03-24', description: 'Payment discrepancy', employeeId: 1010, 
             status: 'Pending', resolutionDate: NULL}
        ] AS c
        CREATE (complaint:Complaint {
            complaintId: c.complaintId,
            date: date(c.date),
            description: c.description,
            status: c.status,
            resolutionDate: CASE WHEN c.resolutionDate IS NOT NULL THEN date(c.resolutionDate) ELSE NULL END
        })
        WITH c, complaint
        OPTIONAL MATCH (u:User {userId: c.userId})
        MATCH (e:Employee {employeeId: c.employeeId})
        FOREACH (ignore IN CASE WHEN u IS NOT NULL THEN [1] ELSE [] END |
            CREATE (u)-[:SUBMITTED]->(complaint)
        )
        CREATE (e)-[:HANDLED]->(complaint)""",

        # Grid nodes and MEMBER_OF relationships
        """UNWIND [
            {connectionId: 8001, date: '2025-03-20', users: [54321, 54322, 54323]},
            {connectionId: 8002, date: '2025-03-20', users: [54324, 54325, 54326]},
            {connectionId: 8003, date: '2025-03-20', users: [54327, 54328, 54329]},
            {connectionId: 8004, date: '2025-03-20', users: [54330, 54331, 54332]},
            {connectionId: 8005, date: '2025-03-20', users: [54333, 54334, 54335]},
            {connectionId: 8006, date: '2025-03-20', users: [54336, 54337, 54338]},
            {connectionId: 8007, date: '2025-03-20', users: [54339, 54340, 54341]},
            {connectionId: 8008, date: '2025-03-20', users: [54342, 54343, 54344]},
            {connectionId: 8009, date: '2025-03-20', users: [54345, 54346, 54347]},
            {connectionId: 8010, date: '2025-03-20', users: [54348, 54349, 54350]},
            {connectionId: 8011, date: '2025-03-20', users: [54351, 54352, 54353]},
            {connectionId: 8012, date: '2025-03-20', users: [54354, 54355, 54356]},
            {connectionId: 8013, date: '2025-03-20', users: [54357, 54358, 54359]},
            {connectionId: 8014, date: '2025-03-20', users: [54360]}
        ] AS g
        CREATE (grid:Grid {
            connectionId: g.connectionId,
            date: date(g.date)
        })
        WITH g, grid
        UNWIND g.users AS userId
        MATCH (u:User {userId: userId})
        CREATE (u)-[:MEMBER_OF]->(grid)""",

        # PARTICIPATES_IN relationships
        """UNWIND [
            {userId: 54321, transactionId: 5001},
            {userId: 54321, transactionId: 5021},
            {userId: 54321, transactionId: 5041},
            {userId: 54321, transactionId: 5061},
            {userId: 54322, transactionId: 5002},
            {userId: 54322, transactionId: 5022},
            {userId: 54322, transactionId: 5042},
            {userId: 54322, transactionId: 5062},
            {userId: 54323, transactionId: 5003},
            {userId: 54323, transactionId: 5023},
            {userId: 54323, transactionId: 5043},
            {userId: 54323, transactionId: 5063},
            {userId: 54324, transactionId: 5004},
            {userId: 54324, transactionId: 5024},
            {userId: 54324, transactionId: 5044},
            {userId: 54324, transactionId: 5064},
            {userId: 54325, transactionId: 5005},
            {userId: 54325, transactionId: 5025},
            {userId: 54325, transactionId: 5045},
            {userId: 54325, transactionId: 5065},
            {userId: 54326, transactionId: 5006},
            {userId: 54326, transactionId: 5026},
            {userId: 54326, transactionId: 5046},
            {userId: 54326, transactionId: 5066},
            {userId: 54327, transactionId: 5007},
            {userId: 54327, transactionId: 5027},
            {userId: 54327, transactionId: 5047},
            {userId: 54327, transactionId: 5067},
            {userId: 54328, transactionId: 5008},
            {userId: 54328, transactionId: 5028},
            {userId: 54328, transactionId: 5048},
            {userId: 54328, transactionId: 5068},
            {userId: 54329, transactionId: 5009},
            {userId: 54329, transactionId: 5029},
            {userId: 54329, transactionId: 5049},
            {userId: 54329, transactionId: 5069},
            {userId: 54330, transactionId: 5010},
            {userId: 54330, transactionId: 5030},
            {userId: 54330, transactionId: 5050},
            {userId: 54330, transactionId: 5070},
            {userId: 54331, transactionId: 5011},
            {userId: 54331, transactionId: 5031},
            {userId: 54331, transactionId: 5051},
            {userId: 54331, transactionId: 5071},
            {userId: 54332, transactionId: 5012},
            {userId: 54332, transactionId: 5032},
            {userId: 54332, transactionId: 5052},
            {userId: 54332, transactionId: 5072},
            {userId: 54333, transactionId: 5013},
            {userId: 54333, transactionId: 5033},
            {userId: 54333, transactionId: 5053},
            {userId: 54333, transactionId: 5073},
            {userId: 54334, transactionId: 5014},
            {userId: 54334, transactionId: 5034},
            {userId: 54334, transactionId: 5054},
            {userId: 54334, transactionId: 5074},
            {userId: 54335, transactionId: 5015},
            {userId: 54335, transactionId: 5035},
            {userId: 54335, transactionId: 5055},
            {userId: 54335, transactionId: 5075},
            {userId: 54336, transactionId: 5016},
            {userId: 54336, transactionId: 5036},
            {userId: 54336, transactionId: 5056},
            {userId: 54336, transactionId: 5076},
            {userId: 54337, transactionId: 5017},
            {userId: 54337, transactionId: 5037},
            {userId: 54337, transactionId: 5057},
            {userId: 54337, transactionId: 5077},
            {userId: 54338, transactionId: 5018},
            {userId: 54338, transactionId: 5038},
            {userId: 54338, transactionId: 5058},
            {userId: 54338, transactionId: 5078},
            {userId: 54339, transactionId: 5019},
            {userId: 54339, transactionId: 5039},
            {userId: 54339, transactionId: 5059},
            {userId: 54339, transactionId: 5079},
            {userId: 54340, transactionId: 5020},
            {userId: 54340, transactionId: 5040},
            {userId: 54340, transactionId: 5060},
            {userId: 54340, transactionId: 5080}
        ] AS p
        MATCH (u:User {userId: p.userId}), (t:EnergyTransaction {transactionId: p.transactionId})
        CREATE (u)-[:PARTICIPATES_IN]->(t)""",

        # REPORTS_TO relationships
        """MATCH (e:Employee), (m:Employee {employeeId: e.managerId})
        WHERE e.employeeId <> m.employeeId
        CREATE (e)-[:REPORTS_TO]->(m)""",

        # SUPERVISED_BY relationships
        """MATCH (r:Region), (e:Employee {employeeId: r.supervisorId})
        CREATE (r)-[:SUPERVISED_BY]->(e)""",

        # LOCATED_IN relationships
        """UNWIND [
            {userId: 54341, regionId: 4},
            {userId: 54342, regionId: 2},
            {userId: 54343, regionId: 6},
            {userId: 54344, regionId: 3},
            {userId: 54345, regionId: 1},
            {userId: 54346, regionId: 5},
            {userId: 54347, regionId: 2},
            {userId: 54348, regionId: 1},
            {userId: 54349, regionId: 6},
            {userId: 54350, regionId: 3},
            {userId: 54351, regionId: 5},
            {userId: 54352, regionId: 4},
            {userId: 54353, regionId: 2},
            {userId: 54354, regionId: 3},
            {userId: 54355, regionId: 1},
            {userId: 54356, regionId: 6},
            {userId: 54357, regionId: 4},
            {userId: 54358, regionId: 5},
            {userId: 54359, regionId: 2},
            {userId: 54360, regionId: 3},
            {userId: 54321, regionId: 3},
            {userId: 54322, regionId: 1},
            {userId: 54323, regionId: 6},
            {userId: 54324, regionId: 2},
            {userId: 54325, regionId: 4},
            {userId: 54326, regionId: 5},
            {userId: 54327, regionId: 1},
            {userId: 54328, regionId: 2},
            {userId: 54329, regionId: 3},
            {userId: 54330, regionId: 6},
            {userId: 54331, regionId: 5},
            {userId: 54332, regionId: 4},
            {userId: 54333, regionId: 2},
            {userId: 54334, regionId: 1},
            {userId: 54335, regionId: 6},
            {userId: 54336, regionId: 3},
            {userId: 54337, regionId: 4},
            {userId: 54338, regionId: 5},
            {userId: 54339, regionId: 2},
            {userId: 54340, regionId: 1}
        ] AS ur
        MATCH (u:User {userId: ur.userId}), (r:Region {regionId: ur.regionId})
        CREATE (u)-[:LOCATED_IN]->(r)"""
    ]

    conn = Neo4jConnector()
    try:
        for i, query in enumerate(queries, 1):
            print(f"Executing query set {i}/{len(queries)}")
            conn.execute_query(query)
    finally:
        conn.close()

if __name__ == "__main__":
    load_full_data()