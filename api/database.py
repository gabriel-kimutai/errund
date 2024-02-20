import os
from dotenv import load_dotenv
from supabase.client import Client, create_client

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(supabase_url=url, supabase_key=key)