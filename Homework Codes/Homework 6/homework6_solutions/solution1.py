import os

os.makedirs("cs104/slides")
os.makedirs("cs104/labs/lab01")
os.makedirs("cs104/labs/lab02/solutions")

with open("cs104/notes.txt", "w") as f:
    f.write("I like computer\n")
    f.write("programming.")

with open("cs104/slides/lecture01.txt", "w") as f:
    f.write("lecture 01:\n")
    f.write("\"introduction\"")

with open("cs104/labs/lab02/solutions/solution.py", "w") as f:
    f.write("print(\"hello\")\n")
    f.write("for i in range(5):\n")
    f.write("    print(i**2)\n")
