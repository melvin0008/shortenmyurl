import os

REDIS_HOST = os.getenv("REDIS_HOST", "greeneye.redistogo.com")
REDIS_PORT = int(os.getenv("REDIS_PORT", "11156"))
REDIS_DB = int(os.getenv("REDIS_DB", "1"))