#!/bin/bash

# Directories
INPUT_DIR="."      # Folder where all test JS files live
OUTPUT_DIR="test_outputs"   # Folder where commit messages will be saved
####
# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through all files matching *original*.js
for original_file in "$INPUT_DIR"/*original*.js; do
    # Extract base name without path
    base=$(basename "$original_file")

    # Derive test name prefix and number
    prefix_and_number="${base/original/}"         # Remove "original"
    prefix_and_number="${prefix_and_number%.js}"  # Remove ".js"

    # Build matching changed file name
    changed_file="$INPUT_DIR/${base/original/changed}"

    if [ ! -f "$changed_file" ]; then
        echo "No matching file for $original_file. Skipping."
        continue
    fi

    echo "Generating diff for $original_file and $changed_file..."
    diff_output=$(diff -u "$original_file" "$changed_file")

    echo "Diff output:"
    echo "$diff_output"

    if [ -z "$diff_output" ]; then
        echo "No changes detected. Skipping."
        continue
    fi



# Send diff to the API and capture the response
    response=$(curl -w "%{http_code}" -s -X POST http://0.0.0.0:8000/generate \
        -H "Content-Type: application/json" \
        -d "{\"diff\": $(jq -Rs <<< "$diff_output")}")

    # Separate the HTTP status code from the response body
    http_status=$(echo "$response" | tail -n 1)  # Get the HTTP status code
    response_body=$(echo "$response" | sed '$d')  # Remove the last line (status code)

    echo "API response for $prefix_and_number (HTTP status: $http_status):"
    echo "$response_body"  # Print the response body

    # Extract the commit message from the response body
    commit_message=$(echo "$response_body" | jq -r '.commit_message')

    if [ -z "$commit_message" ]; then
        echo "No commit message returned for $prefix_and_number. Skipping."
        continue
    fi

# Save the commit message to the output directory
    echo "$commit_message" > "$OUTPUT_DIR/${prefix_and_number}.out"
    echo "Saved commit message to $OUTPUT_DIR/${prefix_and_number}.out"
done
