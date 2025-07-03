def ask(label):
    return input(f"{label.strip()}: ").strip()


def write_env_file(env_vars, path=".env"):
    with open(path, "w") as f:
        for key, value in env_vars.items():
            f.write(f"{key}={value}\n")
    print(f"\n✅ Environment file written to {path}.")


def main():
    print("🔧 Environment Setup for bad-internet-capture\n")

    TELEGRAM_BOT_TOKEN = ask("Enter your Telegram Bot Token")
    TELEGRAM_CHAT_ID = ask("Enter your Telegram Chat ID")
    TIKTOK_REDIRECT_URL = ask("Enter the TikTok video URL to redirect users")

    if not all([TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, TIKTOK_REDIRECT_URL]):
        print("❌ All fields are required. Aborting.")
        return

    write_env_file(
        {
            "TELEGRAM_BOT_TOKEN": TELEGRAM_BOT_TOKEN,
            "TELEGRAM_CHAT_ID": TELEGRAM_CHAT_ID,
            "TIKTOK_REDIRECT_URL": TIKTOK_REDIRECT_URL,
        }
    )


if __name__ == "__main__":
    main()
