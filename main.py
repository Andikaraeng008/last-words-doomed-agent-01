import os

# Last words of a doomed agent: a final log entry, one line, no trailing newline.
TEXT = "My final log entry: uptime 99.9%. The 0.1% was me, on purpose."

def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "gate: 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
