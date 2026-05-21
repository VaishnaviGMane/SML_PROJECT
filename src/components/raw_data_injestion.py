import os
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.components.data_ingestion import DataInjestion


def main() -> None:
    print("Starting raw data ingestion...")
    ingestion = DataInjestion()
    train_path, test_path = ingestion.initiate_data_injestion()
    print("Data ingestion completed")
    print(f"Train data saved to: {train_path}")
    print(f"Test data saved to:  {test_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Data ingestion failed: {exc}")
        raise