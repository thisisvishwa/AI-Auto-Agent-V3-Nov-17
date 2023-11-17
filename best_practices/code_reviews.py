```python
import os
from git import Repo

def reviewCode():
    repo = Repo(os.getcwd())

    # Get the list of all commits
    commits = list(repo.iter_commits('master'))

    # Iterate over each commit
    for commit in commits:
        # Get the diff of the commit with its parent
        diff_index = commit.diff(commit.parents[0] if commit.parents else None)

        # Iterate over each change in the diff
        for diff in diff_index.iter_change_type('M'):
            # Check if the change is in a Python file
            if diff.a_path.endswith('.py'):
                # Print the commit message and the change
                print(f'Commit: {commit.message}')
                print(f'Change in {diff.a_path}:')
                print(diff)

if __name__ == "__main__":
    reviewCode()
```
This Python script uses the GitPython library to access the Git repository in the current directory. It iterates over each commit in the master branch, and for each commit, it gets the diff with its parent commit. It then iterates over each change in the diff, and if the change is in a Python file, it prints the commit message and the change. This can be used as a simple code review tool, allowing you to see the changes made in each commit for Python files.