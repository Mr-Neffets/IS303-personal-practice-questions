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
You are ordering pizzas for a party. Each pizza has 8 slices. You want to
find out how many slices will be left over if everyone eats the same amount.

1. Ask the user how many pizzas you ordered.
2. Ask the user how many people are at the party.
3. Assume each person eats the same number of slices.
4. Use modulus (%) to find out how many slices will be left over.
5. Print the result in a sentence.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

pizzas = int(input("How many pizzas did you order? "))
people = int(input("How many people are at the party? "))

total_slices = pizzas * 8
leftover_slices = total_slices % people

print(f"There will be {leftover_slices} slice(s) left over.")
