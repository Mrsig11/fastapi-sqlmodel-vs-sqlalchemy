#!/usr/bin/env bash
set -e

RESULTS_DIR="app/benchmarks/results"
RAW_DIR="$RESULTS_DIR/raw"
FINAL_FILE="$RESULTS_DIR/benchmark_results.json"

mkdir -p "$RAW_DIR/sqlmodel" "$RAW_DIR/sqlalchemy"

echo "🚀 Starting full benchmark suite..."

run_for_orm () {
    ORM=$1
    echo ""
    echo "==============================="
    echo "🔬 Running benchmarks for $ORM"
    echo "==============================="

    export ORM_BACKEND=$ORM

    # 1️⃣ pytest-benchmark
    pytest app/tests/performance \
        --benchmark-only \
        --benchmark-json="$RAW_DIR/$ORM/pytest_benchmark.json"

    # 2️⃣ Profiling
    python -m app.benchmarks.profiling \
        > "$RAW_DIR/$ORM/profiling.txt"


    # 3️⃣ k6
    if command -v k6 &> /dev/null; then
        k6 run app/benchmarks/k6.js \
        --summary-export="$RAW_DIR/$ORM/k6.json"
    else
        echo "⚠️ k6 not installed, skipping"
    fi

    # 4️⃣ Locust (headless)
    locust -f app/benchmarks/locustfile.py \
        --headless \
        -u 20 -r 5 -t 30s \
        --host=http://localhost:8000 \
        --csv="$RAW_DIR/$ORM/locust" \
        --csv-full-history
}

# run_for_orm "sqlmodel"
run_for_orm "sqlalchemy"

# echo "📦 Aggregating results..."
python app/benchmarks/collect_profiling.py

echo "✅ All benchmarks completed"
echo "📄 Final report: $FINAL_FILE"
