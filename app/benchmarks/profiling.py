import cProfile
import pstats
import tracemalloc

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


def main():
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
    print("\n▶ Memory usage:")
    print(f"Current: {current / 1024:.2f} KB")
    print(f"Peak:    {peak / 1024:.2f} KB")

    tracemalloc.stop()


if __name__ == "__main__":
    main()
