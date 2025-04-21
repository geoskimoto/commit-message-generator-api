#!/bin/bash

# Root folders
ROOT_DIR="."  # Inside test_commits
OUTPUT_BASE="test_outputs"
CSV_FILE="$OUTPUT_BASE/commit_messages.csv"

# Subdirectories to test
SUBFOLDERS=("comments" "java" "javascript" "python")

# Create base output folder and CSV file
mkdir -p "$OUTPUT_BASE"
echo "test_name,test_type,diff,commit_message" > "$CSV_FILE"

# Loop through each folder
for SUBFOLDER in "${SUBFOLDERS[@]}"; do
    INPUT_DIR="$ROOT_DIR/$SUBFOLDER"
    OUTPUT_DIR="$OUTPUT_BASE/$SUBFOLDER"
    mkdir -p "$OUTPUT_DIR"

    echo "🔍 Processing: $INPUT_DIR"

    for original_file in "$INPUT_DIR"/*original*.*; do
        base=$(basename "$original_file")
        prefix=$(echo "$base" | sed -E 's/_original([0-9]+)\..*/_\1/')
        changed_file="$INPUT_DIR/${base/original/changed}"

        if [ ! -f "$changed_file" ]; then
            echo "⚠️  No matching changed file for $original_file. Skipping."
            continue
        fi

        echo "🔧 Generating diff for: $base vs. $(basename "$changed_file")"
        diff_output=$(diff -u "$original_file" "$changed_file")

        if [ -z "$diff_output" ]; then
            echo "⚠️  No changes detected. Skipping."
            continue
        fi

        # Send diff to the API and capture response
        response=$(curl -w "%{http_code}" -s -X POST http://0.0.0.0:8000/generate \
            -H "Content-Type: application/json" \
            -d "{\"diff\": $(jq -Rs <<< "$diff_output")}")

        http_status=$(echo "$response" | tail -n 1)
        response_body=$(echo "$response" | sed '$d')

        echo "📬 API response for $prefix (HTTP $http_status):"
        echo "$response_body"

        commit_message=$(echo "$response_body" | jq -r '.commit_message')

        if [ -z "$commit_message" ]; then
            echo "❌ No commit message returned. Skipping."
            continue
        fi

        # Save commit message as .out file
        echo "$commit_message" > "$OUTPUT_DIR/${prefix}.out"
        echo "✅ Saved to $OUTPUT_DIR/${prefix}.out"

        # Escape CSV fields
        escaped_diff=$(echo "$diff_output" | sed 's/"/""/g' | tr '\n' ' ' | sed 's/,/;/g')
        escaped_msg=$(echo "$commit_message" | sed 's/"/""/g')

        # Append to CSV
        echo "\"$prefix\",\"$SUBFOLDER\",\"$escaped_diff\",\"$escaped_msg\"" >> "$CSV_FILE"
    done
done
