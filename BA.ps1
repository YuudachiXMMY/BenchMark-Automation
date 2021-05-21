# Change the below string variable to point to the directory where the game binary exists:
$workingDirectory = "C:\Users\Navi\Desktop\BenchMark-Automation"

$filePath = "m.exe"
$argumentList = "--readLocal 1 --language 'cn'"

# Check for the path set by environmental variables
if ($env:bhUnigineSanctuary -ne $null) {
    $workingDirectory = $env:bhUnigineSanctuary
}

# Start Unigine Sanctuary
echo "INIT: Launching Unigine Sanctuary..."
$p = Start-Process -WorkingDirectory $workingDirectory -FilePath $filePath -ArgumentList $argumentList -PassThru

# Run the app
echo "LOOP: Running benchmark for 1 hour"
Start-Sleep 3600

# Kill the process
echo "QUIT: Killing process"
Stop-Process -InputObject $p

# Wait 20 seconds for the process to exit
Start-Sleep 20