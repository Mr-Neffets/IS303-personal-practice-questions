'''
OPTIONAL AI GUIDANCE PROMPT:
----------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions to
a practice problem that my professor gave me to try before class. Please be my
kind tutor and walk me through how to solve the problem step by step.

Don't just give me the full solution all at once (unless I later ask for it).
Instead, help me work through it gradually, with clear explanations and small,
easy-to-understand examples. Please use everyday language and explain things
in a simple, friendly way.


INSTRUCTIONS:
-------------
You are helping run sign-ups for student clubs at a campus fair. You need to
track which students joined which clubs.

You should store the club data using a dictionary where:
- The keys are club names (strings)
- The values are lists of student names (strings)

Create a program that:
1. Uses a while loop to repeatedly show this menu:

    1. Sign up a student for a club
    2. View members of a club
    3. Quit

2. If the user chooses option 1:
   - Ask for the student's name
   - Ask for the club name
   - Add the student to the list of members for that club
   - If the club does not exist in the dictionary yet, add it

3. If the user chooses option 2:
   - Ask for the club name
   - Print all members of that club (or a message if no one is signed up)

4. If the user chooses option 3:
   - Exit the loop and print a goodbye message
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

clubs_dict = {}
continue_running = True

while continue_running:
    print("\nMenu:")
    print("1. Sign up a student for a club")
    print("2. View members of a club")
    print("3. Quit")

    choice = input("Choose an option (1, 2, or 3): ")

    if choice == "1":
        student = input("Enter the student's name: ")
        club = input("Enter the club name: ")

        # if a club isn't in the dictionary yet, we need to add it and 
        # make it have an empty list as its value.
        if club not in clubs_dict:
            clubs_dict[club] = []
        
        clubs_dict[club].append(student)
        print(f"{student} has been signed up for {club}.")

    elif choice == "2":
        club = input("Enter the club name to view: ")

        # make sure the club exists before trying to get its value.
        if club in clubs_dict:
            print(f"Members of {club}:")
            for member in clubs_dict[club]:
                print(f"- {member}")
        else:
            print(f"No members signed up for {club} yet.")

    elif choice == "3":
        print("Exiting the club sign-up system. Goodbye!")
        continue_running = False
    else:
        print("Invalid option. Please enter 1, 2, or 3.")
