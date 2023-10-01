import requests
import os
from pathlib import Path
docs = [
    'https://api-explorer.alfresco.com/api-explorer/definitions/alfresco-core.yaml'
]
folder = './api-def'
# if not os.path.exists(folder):
#     os.mkdir(folder)
# for url in docs:
#     file_name = url.split('/')[-1]
#     print(file_name)
#     res = requests.get(url)
#     res.raise_for_status()
#     with open(os.path.join(folder, file_name), 'wb') as fd:
#         fd.write(res.content)

