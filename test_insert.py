import urllib.request
import json
import uuid

SUPABASE_URL = "https://yjgskbdtnyzsmuzvnrsz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqZ3NrYmR0bnl6c211enZucnN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTA5NDQ5NzEsImV4cCI6MjEwNjUyMDk3MX0.elz2qyCCXBRFTCdbzqYqoiltkkmBALKrQhAv-I4SC7Q"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

order_payload = {
    "customer_name": "QA Test 2",
    "customer_phone": "254700000000",
    "delivery_type": "rider",
    "delivery_address": "QA Lab",
    "kit_name": "QA Test Kit",
    "payment_ref": "QA_123",
    "cart_items": [],
    "status": "PENDING_PAYMENT"
}
url = f"{SUPABASE_URL}/rest/v1/orders"
req_data = json.dumps(order_payload).encode('utf-8')
request = urllib.request.Request(url, data=req_data, headers=HEADERS, method="POST")
try:
    with urllib.request.urlopen(request) as response:
        print("Success! Status code:", response.getcode())
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode('utf-8')}")
