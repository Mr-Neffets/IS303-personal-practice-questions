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
Keep asking the user to enter the password until they get it right.

1. The correct password is "cougar".
2. Use a while loop to keep asking until they type it correctly.
3. Use break to exit the loop when it's correct.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

while True:
    password = input("Enter the password: ")
    if password == "cougar":
        print("Access granted.")
        break
    else:
        print("Wrong password. Try again.")
