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
You're working at the BYU Creamery and need to apply a student discount.

1. Ask the user if they are a student (answer "yes" or "no").
2. If they are a student, print "You get a discount!"
3. Otherwise, print "No discount available."
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

is_student = input("Are you a student? (yes/no): ")

if is_student == "yes":
    print("You get a discount!")
else:
    print("No discount available.")
