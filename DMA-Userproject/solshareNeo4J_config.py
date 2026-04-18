from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

class Neo4jConnector:
    def __init__(self):
        self.uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.user = os.getenv("NEO4J_USER", "neo4j")
        self.password = os.getenv("NEO4J_PASSWORD", "12345678")
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
    
    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            return session.run(query, parameters).data()
    
    def close(self):
        self.driver.close()

# Test connection
if __name__ == "__main__":
    conn = Neo4jConnector()
    print(conn.execute_query("RETURN 'Connection successful' AS message"))
    conn.close()