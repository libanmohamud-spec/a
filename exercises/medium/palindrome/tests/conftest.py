import sys
from pathlib import Path

# Add parent directory to Python path so we can import task
# Only add if not already present to avoid duplicates
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

