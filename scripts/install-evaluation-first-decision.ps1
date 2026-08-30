[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Source = Join-Path $RepoRoot ".agents/skills/evaluation-first-decision"
$Timestamp = Get-Date -Format "yyyyMMddHHmmss"

if (-not (Test-Path (Join-Path $Source "SKILL.md"))) {
    throw "Skill source not found: $Source"
}

function Install-SkillCopy {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Destination
    )

    $Parent = Split-Path -Parent $Destination
    New-Item -ItemType Directory -Path $Parent -Force | Out-Null

    if (Test-Path $Destination) {
        $Backup = "$Destination.bak-$Timestamp"
        Move-Item -Path $Destination -Destination $Backup
        Write-Host "Backed up existing skill to $Backup"
    }

    Copy-Item -Path $Source -Destination $Destination -Recurse
    Write-Host "Installed $Destination"
}

Install-SkillCopy -Destination (Join-Path $HOME ".agents/skills/evaluation-first-decision")
Install-SkillCopy -Destination (Join-Path $HOME ".claude/skills/evaluation-first-decision")

Write-Host ""
Write-Host 'Done. In Codex use: $evaluation-first-decision'
Write-Host 'In Claude Code use: /evaluation-first-decision'
