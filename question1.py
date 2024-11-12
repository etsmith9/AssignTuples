# Task 1: Formatting Flight Itineraries Create a Python function that takes 
# a list of tuples as an argument. Each tuple contains information about a 
# flight itinerary: (traveler_name, origin, destination). The function should 
# format and return a string that lists each itinerary. For example, if the input is 
# `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
# the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

#Question 1

index = 0

def display_choice(plans, choice):
    for index, itinerary in enumerate(plans):
        if itinerary[0].lower() == choice.lower():
            print(f"Itinerary {index + 1}- Name: {itinerary[0]}, Origin: {itinerary[1]} >> Destination: {itinerary[2]}.")
            return
    print("No matching itinerary found")

def flight_itinerary():
    plans = [
        ("Alice", "New York", "London"),
        ("Bob", "Tokyo", "San Francisco"),
        ("Emily", "Newark", "Rome")
    ]

    while True:
        print("\nWelcome, Alice, Bob & Emily are departing for their flights soon")
        choice = input(""" Please enter the name of your passenger whose itinerary you would like to view: (Alice, Bob, Emily)  
        or type 'exit' to quit the program.  """)

        choice = choice.strip().lower()
    
        if choice == "exit":
            print("Exiting the program.")
            break
        elif choice in ["alice", "bob", "emily"]:
            display_choice(plans, choice)
        else:
            print("Invalid choice, please try again.")
        

if __name__ == '__main__':
    flight_itinerary()