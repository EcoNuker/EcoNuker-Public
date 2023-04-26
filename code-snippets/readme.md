# Code Snippets
Most of the code here is not complete. It's likely missing requirements, imports, and some functions. Here's a list of things you should need for most code snippets. Assume `guilded.py` as a common requirement, as that's what the bot was made with.

guilded.py shared imports:
```
import guilded
from guilded.ext import commands
```

- chess.py - Incomplete, missing functions and requirements. (*Don't expect to be able to run this.*)
    - `chess`, `uplink_python`, `cairosvg`, `PIL`
- ispremium-function.py - Complete
- meme-command.py - Complete, missing requirements and imports.
    - `aiohttp` (installed along with `guilded.py`)
    - `import aiohttp; from html.parser import HTMLParser`

# Requirement Notices
Some of our requirements can be tricky. This includes `cairosvg` and `uplink_python`.
- If you're on Windows, cairosvg will require extra setup. Run pip install pipwin, then run pipwin install cairocffi
- Chess may encounter issues when installing uplink-python. Read https://pypi.org/project/uplink-python/ (Option 2) for more info.
    - This will require GO. Install it on your platform.
        - There may be issues on Windows. If you're getting the loadinternal: cannot find runtime\cgo error, run this command: go env -w CGO_ENABLED=1
        - There may be issues on Windows. If you're getting the cgo: C compiler "gcc" not found: exec: "gcc": executable file not found in %PATH% error, install https://jmeubank.github.io/tdm-gcc/. Make sure to check "Add to Path" at the bottom of the list of items!
        - Once you have built libuplinkc.so, check the error message again. There should be a path where the uplink-python library is installed; this is normally located at (Windows) %localappdata%\Programs\Python\Python310\Lib\site-packages\uplink_python, (Linux) /usr/local/lib/python3.10/dist-packages/uplink_python
Navigate to the directory, and drop libuplinkc.so into it. Verify the uplink works by running the bot again.
