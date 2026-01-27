import json
import os
import subprocess
import sys
import platform
from datetime import datetime
from pathlib import Path

RESULTS_DIR = Path("benchmarks/results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

FINAL_RESULTS_FILE = RESULTS_DIR / "benchmark_results.json"


def run_command(cmd: list[str], env: dict) -> str:
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env,
    )
    if result.returncode != 0:
        print(result.stderr)
        sys.exit(result.returncode)
    return result.stdout


def run_pytest_benchmark(orm: str) -> dict:
    output_file = RESULTS_DIR / f"pytest_benchmark_{orm}.json"

    run_command(
        [
            "pytest",
            "app/tests/performance",
            "--benchmark-only",
            "--benchmark-min-rounds=15",
            "--benchmark-max-time=2",
            "--benchmark-warmup=on",
            f"--benchmark-json={output_file}",
        ],
        env={**os.environ, "ORM_ENGINE": orm},
    )

    with open(output_file) as f:
        return json.load(f)


def run_profiling(orm: str) -> dict:
    env = {**os.environ, "ORM_ENGINE": orm}
    output_file = f"profiling_{os.getenv('ORM_ENGINE', 'sqlmodel').lower()}_results.json"
    
    run_command(
        [
            "python", 
            "-m", 
            "app.benchmarks.profiling",
            f"output={output_file}",
        ],
        env=env,
    )

    with open(output_file) as f:
        return json.load(f)


def main():
    results = {
        "metadata": {
            "date": datetime.utcnow().isoformat(),
            "python_version": sys.version,
            "platform": platform.platform(),
        }
    }

    for orm in ("sqlmodel", "sqlalchemy"):
        print(f"\n▶ Running benchmarks for {orm.upper()}")

        results[orm] = {
            "pytest_benchmark": run_pytest_benchmark(orm),
            "profiling": run_profiling(orm),
        }

    with open(FINAL_RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n✅ Benchmarks completed")
    print(f"📄 Results saved to: {FINAL_RESULTS_FILE}")


if __name__ == "__main__":
    main()
