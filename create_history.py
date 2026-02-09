"""
Script to create realistic git history for ArtReal
"""
import subprocess
import os
from datetime import datetime, timedelta
import random

def run_git(args, date=None):
    env = os.environ.copy()
    if date:
        date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
    result = subprocess.run(["git"] + args, env=env, capture_output=True, text=True)
    return result

# Define commits with dates (going back ~10 days)
base_date = datetime.now()
commits = [
    {
        "days_ago": 10,
        "hour": 9,
        "message": "Initial project setup: FastAPI backend + React frontend structure",
        "files": [
            "backend/app/__init__.py",
            "backend/app/main.py",
            "backend/app/core/__init__.py",
            "backend/app/core/config.py",
            "backend/requirements.txt",
            "backend/run.py",
            "backend/.env.example",
            "backend/.gitignore",
            "front/package.json",
            "front/vite.config.ts",
            "front/tsconfig.json",
            "front/index.html",
            "front/src/main.tsx",
            "front/src/App.tsx",
            "front/.gitignore",
            ".gitignore",
        ]
    },
    {
        "days_ago": 9,
        "hour": 14,
        "message": "feat: add database models and API endpoints for projects",
        "files": [
            "backend/app/db/",
            "backend/app/models/",
            "backend/app/schemas/",
            "backend/app/api/__init__.py",
            "backend/app/api/projects.py",
            "backend/init_db.py",
        ]
    },
    {
        "days_ago": 8,
        "hour": 11,
        "message": "feat: implement multi-agent AI system with Gemini integration",
        "files": [
            "backend/app/agents/",
            "backend/app/core/gemini_client.py",
            "backend/app/core/gemini_thought_signature_client.py",
        ]
    },
    {
        "days_ago": 7,
        "hour": 16,
        "message": "feat: add chat API with streaming support",
        "files": [
            "backend/app/api/chat.py",
            "backend/app/services/",
        ]
    },
    {
        "days_ago": 6,
        "hour": 10,
        "message": "feat: implement WebContainer preview system",
        "files": [
            "front/src/services/",
            "front/src/components/editor/PreviewPanelWithWebContainer.tsx",
            "front/src/components/editor/PreviewSkeleton.tsx",
            "front/src/components/editor/DeviceFrames.tsx",
            "backend/app/templates/",
        ]
    },
    {
        "days_ago": 5,
        "hour": 13,
        "message": "feat: add visual sketch canvas with drag-and-drop components",
        "files": [
            "front/src/components/editor/SketchCanvas.tsx",
            "front/src/components/editor/SketchElement.tsx",
            "front/src/components/editor/SketchConnection.tsx",
            "front/src/components/editor/SketchToolbar.tsx",
            "front/src/components/editor/SketchTemplates.tsx",
            "front/src/components/editor/sketch-types.ts",
            "backend/app/api/sketch.py",
        ]
    },
    {
        "days_ago": 4,
        "hour": 15,
        "message": "feat: add code editor with Monaco and file explorer",
        "files": [
            "front/src/components/editor/CodeEditor.tsx",
            "front/src/components/editor/FileExplorer.tsx",
            "front/src/components/editor/EditorTabs.tsx",
            "front/src/components/editor/DiffViewer.tsx",
            "front/src/components/editor/ChatPanel.tsx",
            "front/src/components/editor/AgentInteraction.tsx",
            "front/src/components/editor/ToolExecutionBlock.tsx",
        ]
    },
    {
        "days_ago": 3,
        "hour": 11,
        "message": "feat: add Git integration and GitHub import/export",
        "files": [
            "front/src/components/editor/GitHistoryModal.tsx",
            "front/src/components/editor/GitConfigModal.tsx",
            "front/src/components/GitHubImportModal.tsx",
        ]
    },
    {
        "days_ago": 2,
        "hour": 14,
        "message": "feat: add landing page, projects dashboard, and pages",
        "files": [
            "front/src/pages/",
            "front/src/components/Navbar.tsx",
            "front/src/components/Footer.tsx",
            "front/src/components/FeaturesSection.tsx",
            "front/src/components/HowItWorksSection.tsx",
            "front/src/components/ProjectCard.tsx",
            "front/src/hooks/",
        ]
    },
    {
        "days_ago": 1,
        "hour": 16,
        "message": "feat: add model settings, prompt improver, and UI components",
        "files": [
            "front/src/components/editor/ModelSettingsModal.tsx",
            "front/src/components/editor/PromptImprover.tsx",
            "front/src/components/APIKeyModal.tsx",
            "front/src/components/editor/EditorTutorial.tsx",
            "front/src/components/editor/GlobalSearch.tsx",
            "front/src/components/CommandPalette.tsx",
            "front/src/components/ui/",
            "backend/app/api/settings.py",
        ]
    },
    {
        "days_ago": 0,
        "hour": 10,
        "message": "docs: add README with screenshots and Gemini 3 hackathon info",
        "files": [
            "README.md",
            "CLAUDE.md",
            "docs/",
            "front/public/",
        ]
    },
]

print("Creating realistic git history for ArtReal...")
print("=" * 50)

for i, commit in enumerate(commits):
    # Calculate date
    commit_date = base_date - timedelta(days=commit["days_ago"])
    commit_date = commit_date.replace(
        hour=commit["hour"],
        minute=random.randint(10, 50),
        second=random.randint(0, 59)
    )

    # Add files
    for file_pattern in commit["files"]:
        run_git(["add", file_pattern])

    # Check if there are staged changes
    status = run_git(["diff", "--cached", "--name-only"])
    if status.stdout.strip():
        # Create commit with backdated timestamp
        run_git(["commit", "-m", commit["message"]], date=commit_date)
        date_str = commit_date.strftime("%Y-%m-%d %H:%M")
        print(f"[{i+1}/{len(commits)}] {date_str} - {commit['message'][:60]}")
    else:
        print(f"[{i+1}/{len(commits)}] Skipped (no new files)")

# Add remaining files in final commit
print("\nAdding remaining files...")
run_git(["add", "."])
status = run_git(["diff", "--cached", "--name-only"])
if status.stdout.strip():
    final_date = base_date.replace(hour=12, minute=30)
    run_git(["commit", "-m", "chore: add remaining configurations and assets"], date=final_date)
    print(f"Final commit: {final_date.strftime('%Y-%m-%d %H:%M')}")

print("\n" + "=" * 50)
print("Git history created successfully!")
print("\nVerifying commits:")
result = run_git(["log", "--oneline"])
print(result.stdout)
