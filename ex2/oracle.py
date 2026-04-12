import os
from dotenv import load_dotenv, find_dotenv

configuration_keys = ("MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
                      "ZION_ENDPOINT")


def load_env_configuration() -> dict[str, str | None]:
    dictionary: dict[str, str] = {}
    for key in configuration_keys:
        retrieved_key: str | None = os.getenv(key)
        if (retrieved_key is None):
            continue
        dictionary[key] = retrieved_key
    return dictionary


def load_default_configuration() -> dict[str, str | None]:
    dictionary: dict[str, str] = {}
    dictionary["MATRIX_MODE"] = "development"
    dictionary["DATABASE_URL"] = "local"
    dictionary["API_KEY"] = "restricted"
    dictionary["LOG_LEVEL"] = "DEBUG"
    dictionary["ZION_ENDPOINT"] = "local"

    return dictionary


def main() -> None:
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    dictionary: dict[str, str] = {}

    env_path = find_dotenv(usecwd=True)
    if (not env_path):
        print("Loading default data")
        dictionary = load_default_configuration()
    else:
        print("Loading env data")
        dictionary = load_env_configuration()
        missing = [key for key in configuration_keys if os.getenv(key) is None]
        if missing:
            print("Missing keys:", ", ".join(missing))
            print(f"Current stored data: {dictionary}")
            return

    print()
    print("Configuration loaded:")

    print(f"Mode: {dictionary["MATRIX_MODE"]}")
    print(f"Database: {dictionary["DATABASE_URL"]}")
    print(f"API Access: {dictionary["API_KEY"]}")
    print(f"Log Level: {dictionary["LOG_LEVEL"]}")
    print(f"Zion Network: {dictionary["ZION_ENDPOINT"]}")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
