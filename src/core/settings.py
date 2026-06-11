from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "configs"
DATA_DIR = PROJECT_ROOT / "data" / "input"
SAMPLE_DIR = PROJECT_ROOT / "data" / "sample"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"
DDL_DIR = PROJECT_ROOT / "sql" / "ddl"
TRANSFORM_DIR = PROJECT_ROOT / "sql" / "transform"
