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
You're checking people into a student event. They must show a student ID
and be on the guest list to get in.

1. Ask the user "Do you have a student ID?" (yes/no)
2. Ask the user "Are you on the guest list?" (yes/no)
3. If both answers are yes, print "Welcome in!"
4. Otherwise, print "Sorry, you can't come in."
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

has_id = input("Do you have a student ID? (yes/no): ")
on_list = input("Are you on the guest list? (yes/no): ")

if has_id == "yes" and on_list == "yes":
    print("Welcome in!")
else:
    print("Sorry, you can't come in.")
