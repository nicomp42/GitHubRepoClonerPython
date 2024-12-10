# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import subprocess
import os
from GitHubRepoClonePackage.GitHubRepoClone import GitHubRepoClone
from UtilitiesPackage.utilities import *

def main():

    html_files = read_html_files("Data\\URLs\\")
    print("Processing",len(html_files), "HTML files that were downloaded from Canvas:")
    print(html_files)
    """
    repo_urls = {
          "https://github.com/someUser/someRepo"
    }
    """
    destination_dir = "cloned_repos"
    #destination_dir = "d:\\IS4010\\"  # This times out sometimes because the USB drive is sooooo slow. 
    
    myGitHubRepoClone = GitHubRepoClone()

    count = 0
    error_count = 0
    #for url in repo_urls:
    for html in html_files:
        url = extract_href(html)
        print(url)
        if myGitHubRepoClone.clone_repo(url, os.path.join(destination_dir, url.split("/")[-1].split(".")[0])) == True:
            count += 1
        else:
            error_count += 1
    print(count, "repos cloned")
    print(error_count, "repo clones failed")
    
if __name__ == "__main__":
    main()
 