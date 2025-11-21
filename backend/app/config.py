# backend/app/config.py
import os
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@db:5432/appdb")
MSRP_WEIGHT = float(os.getenv("MSRP_WEIGHT", 0.6))
HIST_WEIGHT = float(os.getenv("HIST_WEIGHT", 0.4))
