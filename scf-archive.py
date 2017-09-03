import scfutils
import pandas as pd

# Get the last 2000 issues
response = scfutils.get_issues_by_place('newport_2', max_pages=100, archived=True)

# output to json file
filename = 'newport_2_issues_archive.json'
response.to_json(filename, orient="records")
