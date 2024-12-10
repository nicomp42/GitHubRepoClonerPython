# utilities.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import os
import re

def read_html_files(folder_path):
  """Reads all HTML files from a given folder.

  Args:
    folder_path: The path to the folder containing the HTML files.

  Returns:
    A list of strings, where each string is the content of an HTML file.
  """

  html_files = []
  for file in os.listdir(folder_path):
    if file.endswith(".html"):
      file_path = os.path.join(folder_path, file)
      with open(file_path, "r") as f:
        html_content = f.read()
        html_files.append(html_content)
  return html_files


def extract_href(html_string):
  """Extracts the first HREF URL from an HTML string.

  Args:
    html_string: The HTML string to parse.

  Returns:
    The extracted URL, or None if no HREF is found.
  """

  match = re.search(r'href="([^"]+)"', html_string)
  if match:
    return match.group(1)
  else:
    return None

if __name__ == "__main__":
    # Example usage:
    html_string = "<p>This is a paragraph with a <a href=\"https://www.example.com\">link</a>.</p>"
    url = extract_href(html_string)
    print(url)  # Output: https://www.example.com
