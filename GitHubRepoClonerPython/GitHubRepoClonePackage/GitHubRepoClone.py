# GitHubRepoClone.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import subprocess
import os

class GitHubRepoClone:
    def clone_repo(self, url, destination_dir):
        """Clones a GitHub repository to a specified destination directory.

        Args:
            url (str): The URL of the GitHub repository.
            destination_dir (str): The path to the destination directory.
        """
        
        status = None
        try:
            os.makedirs(destination_dir, exist_ok=True)
            subprocess.run(["git", "clone", url, destination_dir], check=True)
            #print(f"Successfully cloned {url} to {destination_dir}")
            status = True
        except subprocess.CalledProcessError as e:
            print(f"Error cloning {url}: {e}")
            status = False

        return status
    