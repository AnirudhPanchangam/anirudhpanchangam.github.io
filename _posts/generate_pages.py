import os
from datetime import datetime
import uuid
import random



categories = [
    "programming",
    "personal",
    "linux",
    "windows"
]

for i in range(10000):
    date_str = datetime.now().strftime("%Y-%m-%d")
    _uuid = uuid.uuid1()
    file_name = date_str + "-" + str(_uuid) + '.markdown'
    content = """---
    layout: post
    title:  "Hello %s"
    date:   %s 00:01:35 + 05:30
    categories: %s
---

    ```
    some content
    ```

    """%(str(_uuid), date_str, random.choice(categories))

    with open(file_name, 'w') as f:
        f.write(content)