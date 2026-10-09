import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const WHATSAPP_ACCESS_TOKEN = Deno.env.get("WHATSAPP_ACCESS_TOKEN")!;
const WHATSAPP_PHONE_NUMBER_ID = Deno.env.get("WHATSAPP_PHONE_NUMBER_ID")!;
const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const SUPABASE_SERVICE_ROLE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

serve(async (req) => {
 try {
 const payload = await req.json();
 const { record, old_record } = payload;

 // Guard: Only fire when transitioning into IN_TRANSIT
 if (record.status !== "IN_TRANSIT" || old_record.status === "IN_TRANSIT") {
 return new Response(JSON.stringify({ message: "Ignored: Not a transition to IN_TRANSIT" }), { status: 200 });
 }

 // Initialize elevated client to pull fulfillment details
 const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);
 const { data: log } = await supabase
 .from("fulfillment_logs")
 .select("carrier_name, carrier_phone")
 .eq("order_id", record.id)
 .maybeSingle();

 const carrierName = log?.carrier_name || "Assigned Courier Rider";
 const carrierPhone = log?.carrier_phone || "Contact via Station";

 // Format phone to E.164 without '+' or leading zeros for WhatsApp Cloud API
 const formattedPhone = record.customer_phone.replace(/[^0-9]/g, "");

 // WhatsApp Cloud API Message Payload
 const whatsappPayload = {
 messaging_product: "whatsapp",
 recipient_type: "individual",
 to: formattedPhone,
 type: "text",
 text: {
 body: `Your parcel is on the way! 🛵\n\nOrder: #${record.order_number} (${record.kit_name})\nRider: ${carrierName} (${carrierPhone})`
 }
 };

 const res = await fetch(
 `https://graph.facebook.com/v18.0/${WHATSAPP_PHONE_NUMBER_ID}/messages`,
 {
 method: "POST",
 headers: {
 "Authorization": `Bearer ${WHATSAPP_ACCESS_TOKEN}`,
 "Content-Type": "application/json"
 },
 body: JSON.stringify(whatsappPayload)
 }
 );

 const result = await res.json();
 return new Response(JSON.stringify({ success: true, result }), {
 headers: { "Content-Type": "application/json" },
 status: 200
 });
 } catch (err) {
 return new Response(JSON.stringify({ error: err.message }), { status: 500 });
 }
});
