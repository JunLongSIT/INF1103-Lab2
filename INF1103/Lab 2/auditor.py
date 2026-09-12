"""
Smart Inventory Auditor
------------------------
Processes daily stock deliveries. Validate each entry against business rules
without crashing. 
"""

def main():
    # Initialize the inventory to zero in the start
    total_inventory = 0
    failed_entries = 0
    overstock_limit = 500

    print("=== Smart Inventory Auditor ===")
    print("Enter stock quantities one at a time. Type 'quit' to finish.\n")

    while True:
        user_input = input("Enter stock quantity: ")

        # Exit condition
        if user_input.lower() == "quit":
            break

        # Validate: must be all digits (rejects text, decimals, symbols)
        if not user_input.isdigit():
            print(f"  ❌ Invalid entry: '{user_input}' is not a valid whole number.\n")
            failed_entries += 1
            continue

        quantity = int(user_input)

        # Business rule: reject negative numbers
        if quantity < 0:
            print(f"  ❌ Invalid entry: {quantity} is negative. Stock cannot be negative.\n")
            failed_entries += 1
            continue

        # Valid entry — update running total
        total_inventory += quantity
        print(f"  ✅ Accepted. Running total: {total_inventory}\n")

        # Overstock check
        if total_inventory > overstock_limit:
            print(f"  🚨 OVERSTOCK ALERT: Inventory ({total_inventory}) exceeds limit of {overstock_limit}!")
            print("  Rejecting further entries.\n")
            break
        elif total_inventory == overstock_limit:
            print("  ⚠️  Inventory is exactly at capacity. Next entry will trigger an alert.\n")
        else:
            pass  # normal operation, no alert needed

    # Final report
    print("\n=== End of Session Report ===")
    print(f"Total Units Processed: {total_inventory}")
    print(f"Number of Failed/Rejected Entries: {failed_entries}")

main()