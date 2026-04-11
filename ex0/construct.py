import sys
import site


def is_inside_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    python_route: str = sys.executable
    print()
    if (is_inside_venv()):
        package_installation_route: str = site.getsitepackages()[0]
        env_path: str = sys.prefix
        venv_name: str = sys.prefix.split("/")[-1]
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {python_route}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {env_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(f"{package_installation_route}")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {python_route}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv venv")
        print("source venv/bin/activate # On Unix")
        print("venv\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
