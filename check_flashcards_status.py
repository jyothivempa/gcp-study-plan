import os

ARTIFACT_DIR = r"C:\Users\JYOTHI\.gemini\antigravity\brain\4410c013-0004-4b8c-9631-9ccdf699cfbf"

def check_flashcards():
    missing_files = []
    found_files = []
    
    files = [f for f in os.listdir(ARTIFACT_DIR) if f.startswith("section_") and f.endswith(".md")]
    
    print(f"Scanning {len(files)} content files...")
    
    for filename in files:
        path = os.path.join(ARTIFACT_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            if "<!-- FLASHCARDS" in content:
                found_files.append(filename)
            else:
                missing_files.append(filename)
    
    print("\nFILES WITH Flashcards:")
    for f in found_files:
        print(f"  - {f}")
        
    print("\nFILES WITHOUT Flashcards (To Do):")
    for f in missing_files:
        print(f"  - {f}")

if __name__ == "__main__":
    check_flashcards()
