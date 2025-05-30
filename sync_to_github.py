import os
import subprocess

def git_push(commit_message="Обновление знаний"):
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_dir)

    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ Токен GitHub не найден!")
        return

    remote_url = f"https://{token}@github.com/Alexbm999/seeker-knowledge.git"
    subprocess.run(["git", "push", remote_url, "main"], check=True)
