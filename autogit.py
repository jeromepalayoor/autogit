import subprocess
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "'updated stuff'"])
subprocess.call(["git", "push", "origin", "main"])