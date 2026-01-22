import os

CONTENT_DIR = r"d:\GCP\gcp-study-plan\curriculum\content"

def check_quizzes():
    for f in os.listdir(CONTENT_DIR):
        if not f.endswith(".md"): continue
        with open(os.path.join(CONTENT_DIR, f), "r", encoding="utf-8") as file:
            content = file.read()
            if "Knowledge Check" in content:
                print(f"{f}: Found Quiz")
            else:
                print(f"{f}: NO QUIZ")

if __name__ == "__main__":
    check_quizzes()
