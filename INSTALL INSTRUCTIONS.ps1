$WshShell = New-Object -comObject Wscript.Shell

$AnacondaPath = [System.Environment]::GetEnvironmentVariable('USERPROFILE') + "\Anaconda3"
$PythonWPath = $AnacondaPath + "\pythonw.exe"
if (!(Test-Path $PythonWPath)) {
    $WshShell.Popup('default Anaconda3 Installation not found.',0,'Fehler',16)
    [System.Environment]::Exit(1)
}

$ScriptsPath = [String](Get-Location)
$WrapperPath = $ScriptsPath + "\wrapper.py"
if (!(Test-Path $WrapperPath)) {
    $WshShell.Popup('wrapper.py not found.',0,'Fehler',16)
    [System.Environment]::Exit(1)
}

$MainPath = [String](Get-Location) + "\main.py"
if (!(Test-Path $MainPath)) {
    $WshShell.Popup('main.py not found.',0,'Fehler',16)
    [System.Environment]::Exit(1)
}

Write-Host "Please follw the Setup Instructions:"
Write-Host "------------------------------------"
Write-Host "Make sure Anaconda3 Python Environment is installed on your System."
Write-Host "Create a link on your Desktop"
Write-Host "Mark the following text with the mouse, copy with Strg-C"
Write-Host "and paste it with Strg-V into 'Geben Sie den Speicherort des Elements ein:"
Write-Host ""
Write-Host ""
Write-Host $PythonWPath $WrapperPath $AnacondaPath $PythonWPath $MainPath
Write-Host ""
Write-Host ""
Write-Host "Click on 'weiter'"
Write-Host "Give it a name like 'OilCSV'"
Write-Host "Click on 'Fertig stellen:'"
Write-Host ""
Write-Host "Right Click on the Link and Click on 'Eigenschaften'"
Write-Host "then paste the following text into 'Ausfuehren in:'"
Write-Host ""
Write-Host ""
Write-Host $ScriptsPath
Write-Host ""
Write-Host ""
Write-Host "Right Click on the Link and Click on 'Eigenschaften'"
Write-Host "then Click on 'Anderes Symbol...' and select the Icon in the Script Folder."
Write-Host "Have Fun !"
Write-Host ""
Write-Host ""
Pause
