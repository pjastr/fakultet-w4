import unittest
from src.trip import Trip


class TestTripInitialization(unittest.TestCase):
    def test_trip_creation(self):
        trip = Trip("Paris", 7)
        self.assertIsInstance(trip, Trip)

    def test_trip_attributes(self):
        trip = Trip("Paris", 7)
        self.assertEqual(trip.destination, "Paris")
        self.assertEqual(trip.duration, 7)


class TestCalculateCost(unittest.TestCase):
    def test_calculate_cost_paris(self):
        trip = Trip("Paris", 7)
        self.assertEqual(trip.calculate_cost(), 700)

    def test_calculate_cost_rome(self):
        trip = Trip("Rome", 5)
        self.assertEqual(trip.calculate_cost(), 500)

    def test_calculate_cost_zero_duration(self):
        trip = Trip("Paris", 0)
        self.assertEqual(trip.calculate_cost(), 0)


class TestAddParticipant(unittest.TestCase):
    def test_add_participant(self):
        trip = Trip("Paris", 7)
        trip.add_participant("John")
        self.assertIn("John", trip.participants)

    def test_add_multiple_participants(self):
        trip = Trip("Paris", 7)
        participants = ["John", "Alice", "Bob"]
        for participant in participants:
            trip.add_participant(participant)
        self.assertEqual(trip.participants, participants)

    def test_add_duplicate_participant(self):
        trip = Trip("Paris", 7)
        trip.add_participant("John")
        trip.add_participant("John")
        self.assertEqual(trip.participants.count("John"), 2)

    def test_add_empty_participant(self):
        trip = Trip("Paris", 7)
        with self.assertRaises(ValueError) as context:
            trip.add_participant("")
        self.assertEqual(str(context.exception), "Participant name cannot be empty")


if __name__ == "__main__":
    unittest.main()
