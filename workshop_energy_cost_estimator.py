"""Workshop Energy Cost Estimator
Calculates daily and monthly energy use (kWh) and cost for workshop machines.
"""

DAYS_PER_MONTH = 30  # assumption used for the monthly figures


def get_positive_number(prompt):
    """Keep asking until the user types a number greater than zero.
    Returns the number as a float."""
    while True:
        text = input(prompt)
        try:
            value = float(text)  # convert the text to a decimal number
        except ValueError:
            print("  Please type a number, for example 2.5 (no letters).")
            continue
        if value <= 0:
            print("  The number must be greater than zero.")
        else:
            return value


def get_hours(prompt):
    """Ask for hours used per day. Must be more than 0 and at most 24."""
    while True:
        hours = get_positive_number(prompt)
        if hours > 24:
            print("  A day only has 24 hours. Try again.")
        else:
            return hours


def daily_kwh(power_watts, hours_per_day):
    """Convert power (W) and hours per day into energy in kWh per day."""
    return power_watts * hours_per_day / 1000


def print_report(machines, tariff):
    """Print a table of every machine plus totals, and return the total
    monthly cost."""
    print("\n" + "=" * 62)
    print(f"{'Machine':<16}{'kWh/day':>10}{'kWh/month':>12}{'Cost/month':>14}")
    print("-" * 62)

    total_daily = 0
    total_monthly = 0

    # Loop through the list of machines (each machine is a dictionary)
    for m in machines:
        d_kwh = daily_kwh(m["watts"], m["hours"])
        m_kwh = d_kwh * DAYS_PER_MONTH
        m["monthly_cost"] = m_kwh * tariff  # stored for the twist below
        total_daily += d_kwh
        total_monthly += m_kwh
        print(f"{m['name']:<16}{d_kwh:>10.2f}{m_kwh:>12.2f}"
              f"{m['monthly_cost']:>14.2f}")

    print("-" * 62)
    total_cost = total_monthly * tariff
    print(f"{'TOTAL':<16}{total_daily:>10.2f}{total_monthly:>12.2f}"
          f"{total_cost:>14.2f}")
    print("=" * 62)
    print(f"Daily cost: {total_daily * tariff:.2f}  "
          f"(tariff: {tariff:.2f} per kWh, {DAYS_PER_MONTH}-day month)")
    return total_cost


def show_twist(machines, total_cost):
    """MY TWIST: find the most expensive machine, show its share of the
    bill, and show what the owner would save by cutting its hours."""
    biggest = machines[0]
    for m in machines:  # find the machine with the highest monthly cost
        if m["monthly_cost"] > biggest["monthly_cost"]:
            biggest = m

    share = biggest["monthly_cost"] / total_cost * 100
    print(f"\nBiggest spender: {biggest['name']} "
          f"({share:.1f}% of your monthly bill)")

    # Ask what percentage the user would cut and calculate the saving
    cut = get_positive_number("By what percentage could you cut its use "
                              "hours? (1-100): ")
    if cut > 100:
        print("  A cut above 100% is not possible, using 100%.")
        cut = 100
    saving = biggest["monthly_cost"] * cut / 100

    if saving >= total_cost * 0.10:
        comment = "That is a big saving, worth doing!"
    elif saving >= total_cost * 0.03:
        comment = "A useful saving."
    else:
        comment = "A small saving, look at other machines too."
    print(f"Cutting {biggest['name']} by {cut:.0f}% saves "
          f"{saving:.2f} per month. {comment}")


def main():
    print("=== Workshop Energy Cost Estimator ===")
    machines = []  # list that will hold one dictionary per machine

    count = int(get_positive_number("How many machines do you have? "))

    for i in range(count):
        print(f"\nMachine {i + 1} of {count}")
        name = input("  Name: ").strip()
        if name == "":  # use a default name if the user types nothing
            name = f"Machine {i + 1}"
        watts = get_positive_number("  Power in watts: ")
        hours = get_hours("  Hours used per day: ")
        machines.append({"name": name[:15], "watts": watts, "hours": hours})

    tariff = get_positive_number("\nYour tariff (cost per kWh): ")

    total_cost = print_report(machines, tariff)
    show_twist(machines, total_cost)


main()
