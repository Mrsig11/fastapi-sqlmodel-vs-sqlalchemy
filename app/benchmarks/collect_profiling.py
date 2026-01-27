import json
from pathlib import Path

BASE_DIR = Path("app/benchmarks/results/raw")
OUTPUT_FILE = Path("app/benchmarks/results/benchmark_results.json")

def load_json(path):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return None

def load_text(path):
    if path.exists():
        return path.read_text()
    return None

results = {}

for orm in ["sqlmodel", "sqlalchemy"]:
    orm_dir = BASE_DIR / orm
    results[orm] = {
        "pytest_benchmark": load_json(orm_dir / "pytest_benchmark.json"),
        "k6": load_json(orm_dir / "k6.json"),
        "profiling": load_text(orm_dir / "profiling.txt"),
        "locust": {
            "stats": load_text(orm_dir / "locust_stats.csv"),
            "history": load_text(orm_dir / "locust_stats_history.csv"),
        }
    }

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_FILE, "w") as f:
    json.dump(results, f, indent=2)

print(f"✅ Benchmark results aggregated into {OUTPUT_FILE}")
