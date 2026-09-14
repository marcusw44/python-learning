# CS1350 Mini-Project 1: Contact Manager

contact_book = {
    "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}

call_log = {
    "Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
    "Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
    "Sister": {"Jan": 80, "Mar": 70},
    "Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
    "Roommate": {"Feb": 15, "Mar": 25},
    "Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
    "Professor": {"Feb": 20, "Mar": 35},
    "Dentist": {"Jan": 10},
}

# PHASE 1 - QUICK CONTACTS

print("=== Phase 1: Quick Contacts ===")

quick_contacts = {}

quick_contacts["Mom"] = "555-1234"
quick_contacts["Dad"] = "555-5678"
quick_contacts["Best Friend"] = "555-8888"
quick_contacts["Pizza Place"] = "555-9999"
quick_contacts["Work"] = "555-0000"

print(quick_contacts)

print("--- Access and Modify ---")

print("Mom's number:", quick_contacts["Mom"])

quick_contacts["Dad"] = "555-4321"

quick_contacts["Dentist"] = "555-2222"

grandma = quick_contacts.get("Grandma")

if grandma is None:
    print("Looking up Grandma: Contact not found")
else:
    print("Looking up Grandma:", grandma)

print("Updated contacts:", quick_contacts)

print("--- Delete and Analyze ---")

del quick_contacts["Pizza Place"]

old_work = quick_contacts.pop("Work")

print("Removed work number:", old_work)

print("Contacts remaining:", len(quick_contacts))
print("Contact names:", list(quick_contacts.keys()))
print("Phone numbers:", list(quick_contacts.values()))

# PHASE 2 - CONTACT ACTIVITY

print()
print("=== Phase 2: Contact Activity ===")

total_minutes = {}

for name, months in call_log.items():

    month_count = len(months)
    total = sum(months.values())
    average = total / month_count

    busiest_month = ""
    busiest_minutes = 0

    for month, minutes in months.items():

        if minutes > busiest_minutes:
            busiest_minutes = minutes
            busiest_month = month

    total_minutes[name] = total

    print(
        f"{name}: {month_count} month(s), "
        f"{total} min total, "
        f"avg: {average:.2f}, "
        f"busiest: {busiest_month} ({busiest_minutes})"
    )

# PHASE 3 - AGGREGATIONS

print()
print("=== Phase 3: Aggregations ===")

month_stats = {}

for name, months in call_log.items():

    for month, minutes in months.items():

        if month not in month_stats:
            month_stats[month] = {
                "minutes": [],
                "total": 0,
                "avg": 0,
                "contacts": 0
            }

        month_stats[month]["minutes"].append(minutes)
        month_stats[month]["total"] += minutes
        month_stats[month]["contacts"] += 1

for month, stats in month_stats.items():
    stats["avg"] = stats["total"] / stats["contacts"]

print("Monthly summary (sorted by average, highest first):")

sorted_months = sorted(
    month_stats.items(),
    key=lambda item: item[1]["avg"],
    reverse=True
)

for month, stats in sorted_months:
    print(
        f"  {month}: {stats['total']} min total, "
        f"{stats['avg']:.2f} avg "
        f"({stats['contacts']} contacts)"
    )

minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

for name, details in contact_book.items():

    category = details["category"]
    city = details["city"]
    total = total_minutes[name]

    minutes_by_category[category] = (
        minutes_by_category.get(category, 0) + total
    )

    minutes_by_city[city] = (
        minutes_by_city.get(city, 0) + total
    )

    contacts_per_city[city] = (
        contacts_per_city.get(city, 0) + 1
    )

print("Minutes by category:", minutes_by_category)
print("Minutes by city:", minutes_by_city)
print("Contacts per city:", contacts_per_city)

# PHASE 4 - DICTIONARY COMPREHENSIONS

print()
print("=== Phase 4: Comprehensions ===")

phone_book = {
    name: details["phone"]
    for name, details in contact_book.items()
}

local_contacts = {
    name: details["phone"]
    for name, details in contact_book.items()
    if details["city"] == "Fort Wayne"
}

activity_level = {
    name: "Frequent" if total >= 200 else "Occasional"
    for name, total in total_minutes.items()
}

print("Phone book:", phone_book)
print("Local contacts (Fort Wayne):", local_contacts)
print("Activity level:", activity_level)


# PHASE 5 - TIERS, DISTRIBUTION, AND RANKINGS

def get_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"


print()
print("=== Phase 5: Tier Report ===")

for name, total in total_minutes.items():
    tier = get_tier(total)
    print(f"{name}: {total} min ({tier})")


platinum = 0
gold = 0
silver = 0
bronze = 0
inactive = 0

for name, total in total_minutes.items():

    tier = get_tier(total)

    if tier == "Platinum":
        platinum += 1
    elif tier == "Gold":
        gold += 1
    elif tier == "Silver":
        silver += 1
    elif tier == "Bronze":
        bronze += 1
    else:
        inactive += 1


print("--- Tier Distribution ---")
print("Platinum:", platinum)
print("Gold:", gold)
print("Silver:", silver)
print("Bronze:", bronze)
print("Inactive:", inactive)


top_name = ""
top_minutes = 0

bottom_name = ""
bottom_minutes = float("inf")

for name, total in total_minutes.items():

    if total > top_minutes:
        top_minutes = total
        top_name = name

    if total < bottom_minutes:
        bottom_minutes = total
        bottom_name = name


print("--- Top and Bottom ---")
print(f"Most contacted: {top_name} ({top_minutes} min)")
print(f"Least contacted: {bottom_name} ({bottom_minutes} min)")

grand_total = sum(total_minutes.values())

average_per_contact = grand_total / len(total_minutes)

print("Total minutes:", grand_total)
print(f"Average per contact: {average_per_contact:.2f}")

print("--- Above Average Contacts ---")

for name, total in total_minutes.items():

    if total > average_per_contact:
        print(f"{name}: {total}")


# PHASE 6 - CONTACT HUB REPORT

print()
print("=== Phase 6: Contact Hub Report ===")

print("Name         Category     City             Minutes Tier")
print("-------------------------------------------------------")

sorted_contacts = sorted(
    total_minutes.items(),
    key=lambda item: item[1],
    reverse=True
)

for name, total in sorted_contacts:

    details = contact_book[name]

    category = details["category"]
    city = details["city"]
    tier = get_tier(total)

    print(
        f"{name:<12}"
        f"{category:<13}"
        f"{city:<17}"
        f"{total:>7} "
        f"{tier}"
    )

print("-------------------------------------------------------")

print(
    f"{len(total_minutes)} contacts | "
    f"{grand_total} total minutes | "
    f"{average_per_contact:.2f} average"
)