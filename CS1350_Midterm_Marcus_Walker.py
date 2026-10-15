"""CS1350AA Midterm Problems 1, 2, 3, and 4.
"""
import json
from abc import ABC, abstractmethod


# Problem 1: Course Gradebook
class Gradebook:
    def __init__(self):
        self.grades = {}

    def add_score(self, student, assignment, score):
        if student not in self.grades:
            self.grades[student] = {}
        self.grades[student][assignment] = score

    def student_average(self, student):
        scores = self.grades.get(student, {})
        if not scores:
            return None
        return sum(scores.values()) / len(scores)

    def assignment_average(self, assignment):
        scores = [grades[assignment] for grades in self.grades.values()
                  if assignment in grades]
        return sum(scores) / len(scores) if scores else None

    def top_students(self, n):
        students = [name for name in self.grades
                    if self.student_average(name) is not None]
        return sorted(students, key=lambda name: self.student_average(name),
                      reverse=True)[:n]

    def missing(self, assignment):
        return sorted(name for name, scores in self.grades.items()
                      if assignment not in scores)


# Problem 2: Access Control with Sets
class Door:
    def __init__(self, name):
        self.name = name
        self.cards = set()

    def grant(self, card_id):
        self.cards.add(card_id)

    def revoke(self, card_id):
        self.cards.discard(card_id)

    def can_open(self, card_id):
        return card_id in self.cards


def master_cards(doors):
    if not doors:
        return set()
    result = doors[0].cards.copy()
    for door in doors[1:]:
        result &= door.cards
    return result


def single_door_cards(doors):
    counts = {}
    for door in doors:
        for card in door.cards:
            counts[card] = counts.get(card, 0) + 1
    return {card for card, count in counts.items() if count == 1}


def unused_cards(all_cards, doors):
    used = set()
    for door in doors:
        used |= door.cards
    return set(all_cards) - used


def audit(doors):
    for door in doors:
        print(f"{door.name}: {len(door.cards)} cards")
    print(f"Master cards: {master_cards(doors)}")


# Problem 3: Sensor Log Processor
def process_readings(in_file, json_file, alert_file, limit):
    readings = {}
    alerts = 0
    with open(in_file, "r") as source, open(alert_file, "w") as output:
        for line in source:
            if not line.strip():
                continue
            timestamp, sensor_id, value = line.strip().split(",")
            number = float(value)
            readings.setdefault(sensor_id, []).append(number)
            if number > limit:
                output.write(f"{timestamp} {sensor_id} {value}\n")
                alerts += 1

    summary = {}
    for sensor_id, values in readings.items():
        summary[sensor_id] = {
            "count": len(values),
            "average": sum(values) / len(values),
            "max": max(values)
        }
    with open(json_file, "w") as output:
        json.dump(summary, output, indent=2)
    return alerts


# Problem 4: Shipping Rates with Inheritance
class Shipment(ABC):
    def __init__(self, tracking_id, weight_kg):
        self.validate_weight(weight_kg)
        self.tracking_id = tracking_id
        self.weight_kg = weight_kg

    @abstractmethod
    def cost(self):
        pass

    def label(self):
        return f"{self.tracking_id} ({self.weight_kg} kg): ${self.cost():.2f}"

    @staticmethod
    def validate_weight(weight_kg):
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")


class StandardShipment(Shipment):
    def __init__(self, tracking_id, weight_kg, rate_per_kg=2.00):
        super().__init__(tracking_id, weight_kg)
        self.rate_per_kg = rate_per_kg

    def cost(self):
        return self.weight_kg * self.rate_per_kg


class ExpressShipment(StandardShipment):
    def __init__(self, tracking_id, weight_kg, surcharge=10.00):
        super().__init__(tracking_id, weight_kg)
        self.surcharge = surcharge

    def cost(self):
        return super().cost() + self.surcharge


class InternationalShipment(Shipment):
    def __init__(self, tracking_id, weight_kg, country, customs_pct=0.15):
        super().__init__(tracking_id, weight_kg)
        self.country = country
        self.customs_pct = customs_pct

    def cost(self):
        return self.weight_kg * 5.00 * (1 + self.customs_pct)


def manifest(shipments):
    total = 0
    for shipment in shipments:
        print(shipment.label())
        total += shipment.cost()
    print(f"Total: ${total:.2f}")
    return total


if __name__ == "__main__":
    print("=== Problem 1 ===")
    gb = Gradebook()
    gb.add_score("Alice", "hw1", 90)
    gb.add_score("Alice", "hw2", 80)
    gb.add_score("Bob", "hw1", 70)
    gb.add_score("Bob", "hw2", 60)
    gb.add_score("Carol", "hw1", 100)
    gb.add_score("Bob", "hw2", 75)
    assert gb.student_average("Alice") == 85.0
    assert gb.student_average("Bob") == 72.5
    assert gb.student_average("Zed") is None
    assert abs(gb.assignment_average("hw1") - 86.66666666666667) < 1e-10
    assert gb.assignment_average("hw9") is None
    assert gb.top_students(2) == ["Carol", "Alice"]
    assert gb.missing("hw2") == ["Carol"]
    print("All Gradebook tests passed")

    print("\n=== Problem 2 ===")
    lobby = Door("Lobby")
    for card in [101, 102, 103, 104]:
        lobby.grant(card)
    lab = Door("Lab")
    for card in [101, 103, 105]:
        lab.grant(card)
    server = Door("Server Room")
    for card in [101, 105]:
        server.grant(card)
    lab.revoke(105)
    lab.revoke(999)
    doors = [lobby, lab, server]
    assert lab.can_open(103) and not lab.can_open(105)
    assert master_cards(doors) == {101}
    assert single_door_cards(doors) == {102, 104, 105}
    assert unused_cards({101, 102, 105, 200}, doors) == {200}
    audit(doors)
    print("All Door tests passed")

    print("\n=== Problem 3 ===")
    with open("readings.txt", "w") as f:
        f.write("08:00,temp1,21.5\n08:00,temp2,19.0\n\n")
        f.write("08:10,temp1,26.0\n08:10,temp2,18.5\n08:20,temp1,24.5\n")
    alerts = process_readings("readings.txt", "summary.json", "alerts.txt", 24.0)
    with open("summary.json", "r") as f:
        summary = json.load(f)
    with open("alerts.txt", "r") as f:
        alert_text = f.read()
    assert alerts == 2
    assert summary["temp1"] == {"count": 3, "average": 24.0, "max": 26.0}
    assert summary["temp2"] == {"count": 2, "average": 18.75, "max": 19.0}
    assert alert_text == "08:10 temp1 26.0\n08:20 temp1 24.5\n"
    print("All Sensor tests passed")

    print("\n=== Problem 4 ===")
    shipments = [StandardShipment("S100", 4.0),
                 ExpressShipment("E200", 2.5),
                 InternationalShipment("I300", 3.0, country="Canada")]
    assert manifest(shipments) == 40.25
    try:
        Shipment.validate_weight(-1)
    except ValueError as e:
        assert str(e) == "Weight must be positive"
        print("Caught:", e)
    else:
        raise AssertionError("Expected ValueError")
    print("All Shipment tests passed")
