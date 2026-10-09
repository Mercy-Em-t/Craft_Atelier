import urllib.request
import json
import uuid
import sys

SUPABASE_URL = "https://yjgskbdtnyzsmuzvnrsz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqZ3NrYmR0bnl6c211enZucnN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTA5NDQ5NzEsImV4cCI6MjEwNjUyMDk3MX0.elz2qyCCXBRFTCdbzqYqoiltkkmBALKrQhAv-I4SC7Q"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

def print_step(msg):
    print(f"\n[*] {msg}...")

def print_pass(msg):
    print(f"[PASS] {msg}")

def print_fail(msg):
    print(f"[FAIL] {msg}")
    sys.exit(1)

def req(method, endpoint, data=None):
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    req_data = json.dumps(data).encode('utf-8') if data else None
    request = urllib.request.Request(url, data=req_data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(request) as response:
            res_body = response.read().decode('utf-8')
            return json.loads(res_body) if res_body else []
    except urllib.error.HTTPError as e:
        print_fail(f"HTTP {e.code}: {e.read().decode('utf-8')}")

print("=========================================")
print(" CRAFT ATELIER QA AUTOMATION TEST SUITE")
print("=========================================")

test_mpesa_ref = f"QA_{uuid.uuid4().hex[:8].upper()}"

# 1. Test Order Insertion & Financial Snapshot
print_step("TEST 1: Submitting Storefront Order & Financial Snapshot")
order_payload = {
    "customer_name": "QA Test User",
    "customer_phone": "254700000000",
    "delivery_type": "rider",
    "delivery_address": "QA Lab",
    "kit_name": "QA Test Kit",
    "payment_ref": test_mpesa_ref,
    "cart_items": [{"title": "QA Test Kit", "price": 2500}],
    "status": "PENDING_PAYMENT",
    "subtotal_cents": 250000,
    "delivery_fee_cents": 30000,
    "total_cents": 280000
}

new_order = req("POST", "orders", order_payload)
if not new_order:
    print_fail("Failed to create order")
order_id = new_order[0]['id']

if new_order[0]['total_cents'] == 280000:
    print_pass(f"Financial snapshot stored securely. Order ID: {order_id}")
else:
    print_fail("Financial snapshot failed.")


# 2. Test M-Pesa SMS Auto-Verification RPC
print_step("TEST 2: Triggering M-Pesa SMS Auto-Reconciliation Webhook")
rpc_url = f"{SUPABASE_URL}/rest/v1/rpc/auto_verify_mpesa_payment"
rpc_data = json.dumps({
    "p_mpesa_code": test_mpesa_ref,
    "p_raw_sms": f"{test_mpesa_ref} Confirmed. KES 2,800.00 paid to Craft Atelier."
}).encode('utf-8')

rpc_req = urllib.request.Request(rpc_url, data=rpc_data, headers=HEADERS, method="POST")
try:
    with urllib.request.urlopen(rpc_req) as response:
        rpc_res = response.read().decode('utf-8')
        if "true" in rpc_res.lower():
            print_pass("RPC executed successfully. SMS Webhook works.")
        else:
            print_fail("RPC returned false.")
except Exception as e:
    print_fail(f"RPC Error: {e}")

# Verify Order State Changed
check_order = req("GET", f"orders?id=eq.{order_id}")
if check_order[0]['status'] == 'QUEUED_FOR_PACKING':
    print_pass("Order status automatically transitioned to QUEUED_FOR_PACKING!")
else:
    print_fail(f"Order status is {check_order[0]['status']}, expected QUEUED_FOR_PACKING.")

# 3. Test Audit Logging
print_step("TEST 3: Validating Chain of Custody Audit Logs")
audit_logs = req("GET", f"order_audit_logs?order_id=eq.{order_id}")
if len(audit_logs) > 0 and audit_logs[0]['new_status'] == 'QUEUED_FOR_PACKING':
    print_pass(f"Audit log found! Changed by: {audit_logs[0]['changed_by']} | Notes: {audit_logs[0]['notes']}")
else:
    print_fail("Audit log not recorded.")

# 4. Test Delivery PIN Injection
print_step("TEST 4: Dispatch & Delivery PIN Generation")
pin_update = req("PATCH", f"orders?id=eq.{order_id}", {"status": "IN_TRANSIT", "delivery_pin": "4812"})
check_pin = req("GET", f"orders?id=eq.{order_id}")
if check_pin[0]['delivery_pin'] == "4812":
    print_pass("Delivery PIN securely written to database.")
else:
    print_fail("Delivery PIN injection failed.")

# Cleanup
print_step("CLEANUP: Removing QA Test Data")
req("DELETE", f"order_audit_logs?order_id=eq.{order_id}")
req("DELETE", f"orders?id=eq.{order_id}")
print_pass("Test data purged.")

print("\n=========================================")
print(" ALL AUTOMATED QA TESTS PASSED! ")
print("=========================================")
