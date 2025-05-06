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
You are helping a friend calculate a restaurant tip. They want to round the
tip amount to the nearest whole dollar.

1. Ask the user for the total bill as a float.
2. Calculate 18% of the bill for the tip.
3. Round the tip using the round() function.
4. Print out the rounded tip amount using a formatted message.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

bill = float(input("What is the total bill? "))
tip = bill * 0.18
rounded_tip = round(tip)

print(f"You should tip about ${rounded_tip}.")
