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