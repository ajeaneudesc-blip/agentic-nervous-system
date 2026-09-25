<#
Nettoyage ponctuel — retrait de l'infrastructure Codex/n8n/LangGraph
suite au passage à Claude Desktop (Cowork/Code/Design) comme unique
environnement d'exécution.

À exécuter UNE FOIS, depuis la racine agentic_nervous_system, avec
PowerShell :
    cd D:\agentic_nervous_system
    .\cleanup_codex_n8n.ps1

Le script liste d'abord ce qu'il va supprimer et demande confirmation.
Il se supprime lui-même à la fin s'il a réussi.
#>

$ErrorActionPreference = "Stop"

# --- Filet de sécurité Git avant suppression irréversible ---
$hasGit = Test-Path ".git"
if (-not $hasGit) {
    Write-Host "Pas de dépôt Git détecté. Initialisation..." -ForegroundColor Yellow
    git init | Out-Null
}
$status = git status --porcelain
if ($status) {
    git add -A
    git commit -m "checkpoint avant nettoyage n8n/Codex/LangGraph" | Out-Null
    Write-Host "Commit de sécurité créé avant suppression." -ForegroundColor Green
} else {
    Write-Host "Rien à committer (arbre déjà propre)." -ForegroundColor DarkGray
}

$targets = @(
    "LEGACY",
    "MIGRATION",
    "scripts\pretriage_legacy.py",
    "scripts\context_router.py",
    "DOMAINS\software\n8n",
    "DOMAINS\software\orchestrator",
    "DOMAINS\software\pyproject.toml",
    "DOMAINS\software\config\mcp_registry.json",
    "DOMAINS\software\scripts\bootstrap_repos.ps1"
)

Write-Host "Les éléments suivants vont être supprimés :" -ForegroundColor Yellow
foreach ($t in $targets) {
    if (Test-Path $t) {
        Write-Host "  - $t"
    } else {
        Write-Host "  - $t (déjà absent)" -ForegroundColor DarkGray
    }
}

$confirm = Read-Host "Confirmer la suppression ? (o/N)"
if ($confirm -ne "o" -and $confirm -ne "O") {
    Write-Host "Annulé." -ForegroundColor Red
    exit 1
}

foreach ($t in $targets) {
    if (Test-Path $t) {
        Remove-Item -Recurse -Force $t
        Write-Host "Supprimé : $t" -ForegroundColor Green
    }
}

# DOMAINS\software\scripts\ ne contenait que bootstrap_repos.ps1 : retirer
# le dossier s'il est vide.
$softwareScripts = "DOMAINS\software\scripts"
if ((Test-Path $softwareScripts) -and (Get-ChildItem $softwareScripts -Force | Measure-Object).Count -eq 0) {
    Remove-Item -Recurse -Force $softwareScripts
    Write-Host "Supprimé (vide) : $softwareScripts" -ForegroundColor Green
}

Write-Host "Nettoyage terminé." -ForegroundColor Cyan
Remove-Item -Force $MyInvocation.MyCommand.Path
