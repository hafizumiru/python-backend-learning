from supabase import create_client, Client

url = "https://YOUR_PROJECT_ID.supabase.co"
key = "YOUR_ANON_OR_SERVICE_KEY"

supabase: Client = create_client(url, key)