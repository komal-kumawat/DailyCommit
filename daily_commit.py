from datetime import datetime

TEXT = "Good morning"

def main():
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("daily_log.txt", "a") as f:
        f.write(f"{today}\n{TEXT}\n\n")

if __name__ == "__main__":
    main()
