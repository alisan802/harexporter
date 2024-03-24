import re
import json
import base64
from urllib.parse import urlparse
from haralyzer import HarParser


def export_files(har_file: str, pattern: str) -> None:
    with open(har_file, 'r', encoding='utf-8') as har_file_fp:
        har_parser = HarParser(json.load(har_file_fp))
    pages = har_parser.pages
    for page in pages:
        for entry in page.entries:
            if re.match(pattern, entry.url):
                print(entry.url)
                out_file_path = str(urlparse(entry.url).path).lstrip('/').replace('/', '_')
                with open(out_file_path, 'wb') as out_file_fp:
                    out_file_fp.write(
                        base64.b64decode(entry.response.text)
                    )


if __name__ == '__main__':
    import sys
    HAR_FILE = sys.argv[1]
    PATTERN = sys.argv[2]
    export_files(HAR_FILE, PATTERN)
