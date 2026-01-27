import cProfile
import pstats
import tracemalloc
import sys
import json
import os
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def run_requests():
    for _ in range(100):
        client.get("/api/v1/todos/")
        client.post(
            "/api/v1/todos/",
            json={"title": "profile", "description": "profiling"}
        )


# The first item in sys.argv is the script name itself
# We slice from index 1 onwards to get the actual arguments
cli_args = sys.argv[1:] 
args = [arg for arg in cli_args if '=' not in arg]
kwargs = {k: v for k, v in [arg.split('=') for arg in cli_args if '=' in arg]}

def main(*args, **kwargs):
    print("▶ Starting memory tracing...")
    tracemalloc.start()

    profiler = cProfile.Profile()
    profiler.enable()

    run_requests()

    profiler.disable()

    print("▶ CPU profiling results:")
    stats = pstats.Stats(profiler)
    stats.sort_stats("cumtime").print_stats(20)

    current, peak = tracemalloc.get_traced_memory()

    # output_file = kwargs.get("output", f"profiling_{os.getenv('ORM_ENGINE', 'sqlmodel').lower()}_results.json")
    
    # with open(output_file) as f:
    #     return json.load(f)
    
    print("\n▶ Memory usage:")
    print(f"Current: {current / 1024:.2f} KB")
    print(f"Peak:    {peak / 1024:.2f} KB")

    tracemalloc.stop()


if __name__ == "__main__":
    main(*args, **kwargs)
