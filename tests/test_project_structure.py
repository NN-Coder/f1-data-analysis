from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_expected_project_files_exist() -> None:
    required_files = [
        "data/constructors.csv",
        "data/results.csv",
        "scripts/main.py",
        "scripts/scatter-plot.py",
        "scripts/interactive-scatter-plot.py",
        "requirements.txt",
    ]

    missing_files = [path for path in required_files if not (REPO_ROOT / path).is_file()]
    assert not missing_files, f"Missing expected files: {missing_files}"
