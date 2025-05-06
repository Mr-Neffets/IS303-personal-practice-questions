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
You are tracking likes on a small business Instagram post throughout the day.

1. Create a variable called likes and set it to 0.
2. Ask the user how many likes they got in the morning.
3. Add that number to likes using +=
4. Ask how many more likes they got in the afternoon.
5. Add that number too using +=
6. Print the total number of likes at the end of the day.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

likes = 0
morning = int(input("How many likes in the morning? "))
likes += morning

afternoon = int(input("How many likes in the afternoon? "))
likes += afternoon

print(f"Total likes today: {likes}")
