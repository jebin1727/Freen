from src.db.qdrant_memory import FreenMemory

memory = FreenMemory()
print("✅ Connected to Qdrant successfully!")

# Test adding memory
memory.add_memory("Hello from Freen test run!")
print("✅ Added test memory successfully.")
