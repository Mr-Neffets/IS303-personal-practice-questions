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
You are helping plan a student activity. A student can participate if:

- They are a full-time student, OR
- They are a part-time student AND not working a job

1. Ask the user if they are a full-time student (yes/no)
2. Ask the user if they are a part-time student (yes/no)
3. Ask the user if they have a job (yes/no)
4. Use logic to determine if they can participate
5. Print "You can participate!" or "Sorry, you are not eligible."
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

is_full_time = input("Are you a full-time student? (yes/no): ")
is_part_time = input("Are you a part-time student? (yes/no): ")
has_job = input("Do you have a job? (yes/no): ")

if is_full_time == "yes" or (is_part_time == "yes" and has_job != "yes"):
    print("You can participate!")
else:
    print("Sorry, you are not eligible.")
