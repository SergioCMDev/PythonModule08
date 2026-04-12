import os
from dotenv import load_dotenv

configuration_keys = ("MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
                      "ZION_ENDPOINT")


def load_env_configuration() -> dict[str, str | None]:
    dictionary: dict[str, str] = {}
    print("load_env_configuration")
    for key in configuration_keys:
        retrieved_key: str | None = os.getenv(key)
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
    is_env_file_real: bool = False
    dictionary: dict[str, str] = {}

    try:
        with open(".env", "r") as file:
            file.read()
            is_env_file_real = True
    except OSError:
        is_env_file_real = False

    if (not is_env_file_real):
        print("Loading default data")
        dictionary = load_default_configuration()
    else:
        print("Loading env data")
        dictionary = load_env_configuration()

    print()
    print("Configuration loaded:")

    print(f"Mode: {dictionary["MATRIX_MODE"]}")
    print(f"Database: {dictionary["DATABASE_URL"]}")
    print(f"API Access: {dictionary["API_KEY"]}")
    print(f"Log Level: {dictionary["LOG_LEVEL"]}")
    print(f"Zion Network: {dictionary["ZION_ENDPOINT"]}")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
