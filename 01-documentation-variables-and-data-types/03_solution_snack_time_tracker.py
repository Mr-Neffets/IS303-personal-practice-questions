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
You work in a student office and want to track snack consumption. You know
how many granola bars you started with and how many are left.

1. Create a variable for how many bars you started with.
2. Create a variable for how many are left.
3. Create a variable for how many were eaten.
4. Print out the number of bars that were eaten.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

bars_start = 20
bars_left = 7
bars_eaten = bars_start - bars_left

print("Granola bars eaten:", bars_eaten)
