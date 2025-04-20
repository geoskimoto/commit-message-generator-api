# Directories
$INPUT_DIR = "."      # Folder where all test JS files live
$OUTPUT_DIR = "test_outputs"   # Folder where commit messages will be saved

# Create output directory if it doesn't exist
if (-not (Test-Path -Path $OUTPUT_DIR)) {
    New-Item -ItemType Directory -Path $OUTPUT_DIR
}

# Loop through all files matching *original*.js
Get-ChildItem -Path $INPUT_DIR -Filter "*original*.js" | ForEach-Object {
    $original_file = $_.FullName
    $base = $_.Name

    # Derive test name prefix and number
    $prefix_and_number = $base -replace "original", ""  # Remove "original"
    $prefix_and_number = $prefix_and_number -replace ".js", ""  # Remove ".js"

    # Build matching changed file name
    $changed_file = $original_file -replace "original", "changed"

    if (-not (Test-Path -Path $changed_file)) {
        Write-Host "No matching file for $original_file. Skipping."
        return
    }

    Write-Host "Generating diff for $original_file and $changed_file..."
    $diff_output = diff -u $original_file $changed_file

    Write-Host "Diff output:"
    Write-Host $diff_output

    if (-not $diff_output) {
        Write-Host "No changes detected. Skipping."
        return
    }

    # Send diff to the API and capture the response
    $response = Invoke-RestMethod -Uri "http://0.0.0.0:8000/generate" -Method Post -ContentType "application/json" -Body (@{ diff = $diff_output } | ConvertTo-Json)

    $http_status = $response.PSObject.Properties["StatusCode"].Value
    $response_body = $response.Content

    Write-Host "API response for $prefix_and_number (HTTP status: $http_status):"
    Write-Host $response_body

    # Extract the commit message from the response body
    $commit_message = ($response_body | ConvertFrom-Json).commit_message

    if (-not $commit_message) {
        Write-Host "No commit message returned for $prefix_and_number. Skipping."
        return
    }

    # Save the commit message to the output directory
    $commit_message | Out-File -FilePath "$OUTPUT_DIR\$prefix_and_number.out"
    Write-Host "Saved commit message to $OUTPUT_DIR\$prefix_and_number.out"
}
