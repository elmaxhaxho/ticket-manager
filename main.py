from collections import deque

tickets_by_id = {}
waiting_ids = deque()
history = []


def enqueue(ticket_id):
    waiting_ids.append(ticket_id)


def dequeue():
    if not waiting_ids:
        print("No waiting tickets.")
        return None

    return waiting_ids.popleft()


def create():

    ticket_id = input("Create a ticket id: ").strip()

    while not ticket_id:
        print("ID cannot be empty.")
        ticket_id = input("Enter a valid id: ").strip()

    if ticket_id in tickets_by_id:
        print("Ticket already exists")

    else:
        title = input("Enter a title: ").strip()

        while not title:
            print("Title cannot be empty.")
            title = input("Enter a valid title: ").strip()

        tickets_by_id[ticket_id] = {
            "title": title,
            "status": "waiting"
        }

        enqueue(ticket_id)
        print("Ticket created successfully!")


def find(ticket_id):

    if ticket_id in tickets_by_id:
        print("Ticket found.")
        print("\nTicket ID:", ticket_id,
              "\nTitle:", tickets_by_id[ticket_id]["title"],
              "\nStatus:", tickets_by_id[ticket_id]["status"])

    else:
        print("Ticket does not exist")


def list_all():

    if not tickets_by_id:
        print("No tickets available.")
        return

    for ticket_id in tickets_by_id:
        print("\nTicket ID:", ticket_id)
        print("Title:", tickets_by_id[ticket_id]["title"])
        print("Status:", tickets_by_id[ticket_id]["status"])


def process_next():

    oldest_id = dequeue()
    if oldest_id is None:
        return

    tickets_by_id[oldest_id]["status"] = "resolved"
    history.append(oldest_id)
    print("Ticket resolved!")



def undo_process():

    if not history:
        print("No resolved tickets to undo.")

    else:
        recent_id = history.pop()
        tickets_by_id[recent_id]["status"] = "waiting"
        waiting_ids.appendleft(recent_id)

        print("Ticket status back to waiting!")


while True:

    print("\nTicket Management"
          "\n1. Manager mode"
          "\n2. Send ticket to manager"
          "\n3. Exit app")

    choice = input("Choose an option: ")

    if choice == "1":

        while True:
            print("\n1. Find ticket by id"
                  "\n2. Display all tickets"
                  "\n3. Resolve ticket status"
                  "\n4. Undo ticket status"
                  "\n5. Exit manager mode")

            action = input("Choose an option: ")

            if action == "1":
                search_id = input("Enter the ticket id: ").strip()
                find(search_id)

            elif action == "2":
                list_all()

            elif action == "3":
                process_next()

            elif action == "4":
                undo_process()

            elif action == "5":
                print("Exiting manager mode...")
                break

            else:
                print("Invalid option.")

    elif choice == "2":
        create()

    elif choice == "3":
        print("Exiting the app...")
        break

    else:
        print("Invalid option.")
