from importlib.metadata import version, PackageNotFoundError
from importlib import import_module
import tomllib

deps = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}

data_points_count = 1000
filename = "matrix_analysis.png"
requierements_file = "ex1/requirements.txt"
pyproject_file = "ex1/pyproject.toml"


def check_dependencies() -> list[str]:

    missing: list[str] = []
    for pkg, msg in deps.items():
        try:
            v = version(pkg)
            import_module(pkg)
            print(f"[OK] {pkg} ({v}) - {msg}")
        except PackageNotFoundError:
            print(f"[MISSING] {pkg} - not installed")
            print("install dependencies with 'pip install -r requirements.txt'"
                  " or poetry install --no-root")
            missing.append(pkg)
    return missing


def version_comparision(dict_versions_requirements: dict[str, str],
                        dict_versions_pyproject: dict[str, str]) -> (
                            tuple[list[str], list[str]]):

    mismatch_requirements: list[str] = []
    mismatch_pyproject: list[str] = []
    print("Checking requirements")
    for pkg in deps.keys():
        v = version(pkg)
        if (dict_versions_requirements[pkg] != v):
            print(f"[MISMATCH] installed {pkg} ({v}) is not "
                  "the same as the requirements "
                  f"({dict_versions_requirements[pkg]}) ")
            mismatch_requirements.append(pkg)
        else:
            print(f"[MATCH] {pkg} ({v})")

    print("Checking pyproject")
    for pkg in deps.keys():
        v = version(pkg)
        if (dict_versions_pyproject[pkg] != v):
            print(f"[MISMATCH] installed {pkg} ({v}) is not "
                  "the same as the "
                  f"pyproject ({dict_versions_pyproject[pkg]}) ")
            mismatch_pyproject.append(pkg)
        else:
            print(f"[MATCH] {pkg} ({v})")
    return (mismatch_requirements, mismatch_pyproject)


def get_requirements_data() -> dict[str, str] | None:
    dict_versions: dict[str, str] = {}
    with open(requierements_file) as file:
        try:
            lines: list[str] = file.readlines()
            if (not lines):
                print("requirements file is empty")
                return None
        except FileNotFoundError as e:
            print(f"{e}")
            return None
    for line in lines:
        line = line.strip()
        parts: list[str] = line.split("=")
        dict_versions[parts[0]] = parts[1]
    return dict_versions


def get_pyproject_data() -> dict[str, str] | None:
    dict_versions: dict[str, str] = {}
    with open(pyproject_file, "r+b") as file:
        try:
            data = tomllib.load(file)
        except FileNotFoundError as e:
            print(f"{e}")
            return None
    if (not data):
        return None
    for line in data["project"]["dependencies"]:
        line = line.strip()
        parts: list[str] = line.split("==")
        dict_versions[parts[0]] = parts[1]
    return dict_versions


def run_analysis() -> None:
    import numpy as np
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print(f"Processing {data_points_count} data points...")
    print("Generating visualization..")
    print()
    print("Analysis complete!")
    data = np.random.normal(loc=0.0, scale=1.0, size=data_points_count)
    plt.plot(data[:100])
    print(f"Results saved to: {filename}")
    plt.savefig(filename)


def Compare_versions(dict_versions_requirements, dict_versions_pyproject):
    print("Installed Version comparison")
    version_comparision(
        dict_versions_requirements, dict_versions_pyproject)
    print()
    print("Version comparison between pip & poetry")
    for key in dict_versions_pyproject.keys():
        if (dict_versions_pyproject[key] != dict_versions_requirements[key]):
            print(f"[MISMATCH] Version of '{key}' differs between pip "
                  f"({dict_versions_requirements[key]}) "
                  f"and & poetry ({dict_versions_pyproject[key]})")
        else:
            print(f"[OK] Version of '{key}' is the same between "
                  "pip and & poetry "
                  f"({dict_versions_pyproject[key]})")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    dict_versions_requirements: dict[str, str] | None = {}
    dict_versions_pyproject: dict[str, str] | None = {}

    dict_versions_requirements = get_requirements_data()
    if (dict_versions_requirements is None):
        print("Requirements is not valid")
        return
    dict_versions_pyproject = get_pyproject_data()
    if (dict_versions_pyproject is None):
        print("Pyproject is not valid")
        return

    missing_packages: list[str] = []

    missing_packages = check_dependencies()

    if missing_packages:
        print()
        print("install dependencies with:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install --no-root")
        return
    print()
    Compare_versions(dict_versions_requirements, dict_versions_pyproject)
    run_analysis()


if __name__ == "__main__":
    main()
