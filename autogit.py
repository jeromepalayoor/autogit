import subprocess
import sys
subprocess.call(["git", "add", "."])
if len(sys.argv) > 1:
    subprocess.call(["git", "commit", "-m", f"{sys.argv[1]}"])
else:
    subprocess.call(["git", "commit", "-m", "'updated stuff'"])
subprocess.call(["git", "push", "origin", "main"])
