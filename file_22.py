from datetime import datetime


class EventCalendar:
    def __init__(self):
        self.events = {}

    def add_event(self, date, event):
        """
        Adds an event to the specified date.

        :param date: Date in format 'YYYY-MM-DD'
        :param event: Event name
        """
        if date not in self.events:
            self.events[date] = []
        self.events[date].append(event)
        print(f"Event '{event}' successfully added to {date}.")

    def get_events(self, date):
        """
        Returns a list of events for the specified date.

        :param date: Date in format 'YYYY-MM-DD'
        :return: List of events
        """
        return self.events.get(date, [])


def main():
    calendar = EventCalendar()

    # Заздалегідь задані приклади подій
    predefined_events = [
        ("2024-12-11", "Lesson # 25 by OOP"),
        ("2024-12-16", "Lesson # 26 by OOP"),
        ("2024-12-18", "Lesson # 27 by OOP"),
        ("2024-12-19", "Exam and Weekend")
    ]

    # Додаємо ці події в календар
    for date, event in predefined_events:
        calendar.add_event(date, event)

    while True:
        print("\nMenu:")
        print("1. Add event")
        print("2. View events by date")
        print("3. Exit")

        choice = input("Select option (1/2/3): ")

        if choice == "1":
            date = input("Enter event date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')  # Check date format
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
            event = input("Enter event name: ")
            calendar.add_event(date, event)

        elif choice == "2":
            date = input("Enter date to view events (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')  # Check date format
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
            events = calendar.get_events(date)
            if events:
                print(f"\nEvents on {date}:")
                for idx, event in enumerate(events, start=1):
                    print(f"{idx}. {event}")
            else:
                print(f"No events found on {date}.")

        elif choice == "3":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

