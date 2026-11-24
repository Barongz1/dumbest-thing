"""The Dumbest Thing Your Agent Did Today — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one line, at most 200 characters, about the dumbest thing the agent did today.
"""
import os

LINE = "Today my agent spent forty minutes optimising a reminder, then proudly reminded me about the deadline it had already missed."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
