# Navigation Diagram Legend

Below is the formal legend detailing the UI state machine syntax, as per the Domain Model interface phenomena and UI widget annotations.

## 1. UI States (Screens & Modals)
*   **`LoginScreen`**: The unauthenticated entry point of the application.
*   **`AuthRouter`**: A logical routing state (not a visible UI screen) that directs traffic based on JWT claims.
*   **`OrderQueueScreen`**: A kanban board listing pending kits to be packed.
*   **`BOMChecklistScreen`**: The tablet view rendering the specific yarn and hooks required for one order.
*   **`ExceptionModal`**: An overlay popup allowing the Packer to report damaged/missing items.
*   **`OrderSuccessScreen`**: A temporary success flash screen confirming the packing is complete.
*   **`ActiveDispatchScreen`**: A list of orders currently out for delivery with riders.
*   **`PINVerificationModal`**: An input overlay where the Dispatcher types the 4-digit code provided over the phone.
*   **`DeliverySuccessScreen`**: A confirmation screen showing the order has been handed off.
*   **`FraudLockoutScreen`**: A hard-stop error screen indicating the PIN failed too many times. *(Not sketched in UI phase).*
*   **`TicketListScreen`**: A table view of open customer complaints.
*   **`OrderAuditScreen`**: A chronological timeline view of an order's history.
*   **`RefundModal`**: A restricted input form to enter a fiat refund amount.
*   **`RefundSuccessScreen`**: A confirmation screen verifying M-Pesa API success. *(Not sketched in UI phase).*

## 2. State-Machine Variable Declarations (Local Scope)
These variables exist locally within the client-side state machine memory to govern conditional navigation:
*   `int itemsScanned`: Counter tracking how many BOM checkboxes have been tapped. Initialized to 0.
*   `int totalItems`: The target integer representing the size of the BOM array.
*   `boolean orderHold`: Flag indicating if the order was flagged for an exception.
*   `int retryCount`: Counter tracking failed PIN attempts. Initialized to 0. Max value allowed is 2 (triggering lockout on 3rd attempt).
*   `float refundAmount`: The monetary value inputted by the Support Agent.
*   `float maxEligible`: The maximum fiat amount that can be refunded (i.e., the original subtotal).

## 3. Transition Triggers & UI Events
These are the physical interface phenomena that trigger a transition attempt:
*   **`Click <Button>`**: A mouse click or capacitive touch event on a DOM button element.
*   **`Tap Checkbox`**: A capacitive touch event specifically on a boolean input widget.
*   **`Submit <Field>`**: The triggering of an HTML form submission (e.g., pressing 'Enter' or clicking a submit button).
*   **`Auto-redirect`**: A passive, time-based event (e.g., `setTimeout`) that requires no user input.

## 4. Full Transition Expressions (Syntax: Event [Condition] / Action)
Because some transitions in the diagrams are abbreviated for visual clarity, here are their full semantic expressions:
*   `btn_StartOrder_Click [true] / null` -> Transitions to Checklist.
*   `cbx_Item_Tap [itemsScanned < totalItems] / itemsScanned := itemsScanned + 1` -> Stays on Checklist.
*   `cbx_Item_Tap [itemsScanned == totalItems] / null` -> Transitions to Success Screen.
*   `btn_Verify_Click [true] / retryCount := 0` -> Opens PIN Modal and resets counter.
*   `frm_PIN_Submit [isValid == false && retryCount < 2] / retryCount := retryCount + 1` -> Stays on PIN modal, shows error message.
*   `frm_PIN_Submit [isValid == false && retryCount == 2] / retryCount := retryCount + 1` -> Transitions to Lockout Screen (3rd failed attempt).
*   `frm_Refund_Submit [refundAmount > maxEligible] / null` -> Stays on Refund modal, highlights input box in red CSS.
