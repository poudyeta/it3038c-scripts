function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

$IP = getIP
$User = $env:USERNAME
$Ver = $HOST.Version.Major
$Hostname = $env:COMPUTERNAME
$date = Get-Date -Format "dddd, MMMM dd, yyyy"
 
$BODY = "This machine's IP is $IP. User is $User. Hostname is $Hostname. PowerShell $Ver. Today's Date is $Date"

$BODY | Out-File -FilePath "C:\system_info.txt"