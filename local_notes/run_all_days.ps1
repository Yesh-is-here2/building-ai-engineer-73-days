Write-Host "Running all day scripts (folder-aware)..."
Write-Host "--------------------------------"

# skip interactive/server scripts during batch run
$skipFolders = @(
  "phase2_llm_nlp\30_llm_cli_chatbot",
  "phase3_software_ai\31_flask_basic_app",
  "phase3_software_ai\32_fastapi_hello",
  "phase3_software_ai\33_rest_post_endpoint",
  "phase3_software_ai\45_ai_powered_api",
  "phase5_data_systems_polish\61_matplotlib_line_plot",   # shows window
  "phase5_data_systems_polish\62_seaborn_bar_chart",      # shows window
  "phase5_data_systems_polish\63_plotly_interactive"      # opens browser
)

$root = (Get-Location).Path

$mainFiles = Get-ChildItem -Recurse -Filter main.py |
  Where-Object { $_.FullName -notmatch "\\.venv\\" }

foreach ($file in $mainFiles) {
  $folder = Split-Path $file.FullName
  $relativeFolder = $folder.Replace($root + "\", "")

  $shouldSkip = $false
  foreach ($s in $skipFolders) {
    if ($relativeFolder -like "$s*") { $shouldSkip = $true; break }
  }

  if ($shouldSkip) {
    Write-Host "`n>>> SKIP: $relativeFolder"
    continue
  }

  Write-Host "`n>>> Running: $relativeFolder\main.py"

  Push-Location $folder
  try {
    python .\main.py
  } catch {
    Write-Host "FAILED: $relativeFolder"
    Write-Host $_
  }
  Pop-Location
}

Write-Host "`n--------------------------------"
Write-Host "Finished."
