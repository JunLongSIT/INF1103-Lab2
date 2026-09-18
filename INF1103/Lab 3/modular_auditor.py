"""
Smart Inventory Auditor (Modular Version)
------------------------------------------
Processes daily stock deliveries. Validates each entry against business
rules without crashing. Now split into functions so new features (tax,
discounts, etc.) can be added without touching the main loop.
"""

TAX_RATE = 0.10
OVERSTOCK_LIMIT = 500


def get_valid_input():
    """
    Prompts the user for a stock quantity.
    Returns:
        - an int if the entry is a valid, non-negative whole number
        - the string "quit" if the user wants to stop
        - None if the entry was invalid (caller should count it as failed)
    """
    user_input = input("Enter stock quantity: ")

    if user_input.lower() == "quit":
        return "quit"

    # Validate: must be all digits (rejects text, decimals, symbols)
    if not user_input.isdigit():
        print(f"  ❌ Invalid entry: '{user_input}' is not a valid whole number.\n")
        return None

    quantity = int(user_input)

    # Business rule: reject negative numbers
    # (isdigit() already blocks a literal '-' sign, but this guard stays
    # here in case validation logic changes later)
    if quantity < 0:
        print(f"  ❌ Invalid entry: {quantity} is negative. Stock cannot be negative.\n")
        return None

    return quantity


def process_delivery(current_total, new_value):
    """Adds a new delivery to the running total and returns the new total."""
    return current_total + new_value


def calculate_tax(amount):
    """Returns the tax owed on a single delivery amount (10% of that delivery)."""
    return amount * TAX_RATE


def generate_report(total_units, failed_attempts, deliveries_processed, total_tax):
    """Prints the final end-of-session summary."""
    print("\n=== End of Session Report ===")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Total Units Processed: {total_units}")
    print(f"Total Tax Collected: {total_tax:.2f}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    total_inventory = 0
    failed_entries = 0
    deliveries_processed = 0
    total_tax_collected = 0.0

    print("=== Smart Inventory Auditor (Modular) ===")
    print("Enter stock quantities one at a time. Type 'quit' to finish.\n")

    while True:
        result = get_valid_input()

        # Exit condition
        if result == "quit":
            break

        # Invalid entry — already printed inside get_valid_input()
        if result is None:
            failed_entries += 1
            continue

        quantity = result

        # Valid entry — update running total via dedicated function
        total_inventory = process_delivery(total_inventory, quantity)
        deliveries_processed += 1

        # Calculate tax for this specific delivery
        delivery_tax = calculate_tax(quantity)
        total_tax_collected += delivery_tax

        print(f"  ✅ Accepted. Delivery tax: {delivery_tax:.2f} | Running total: {total_inventory}\n")

        # Overstock check
        if total_inventory > OVERSTOCK_LIMIT:
            print(f"  🚨 OVERSTOCK ALERT: Inventory ({total_inventory}) exceeds limit of {OVERSTOCK_LIMIT}!")
            print("  Rejecting further entries.\n")
            break
        elif total_inventory == OVERSTOCK_LIMIT:
            print("  ⚠️  Inventory is exactly at capacity. Next entry will trigger an alert.\n")

    generate_report(total_inventory, failed_entries, deliveries_processed, total_tax_collected)


if __name__ == "__main__":
    main()