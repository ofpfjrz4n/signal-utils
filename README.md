# signal-utils

Helpers for handling SIGTERM/SIGINT and draining work before exit.

## Why

I kept rewriting the same thirty lines in every project, so I pulled them out.

## Install

```bash
pip install signal-utils
```

## Usage

```python
from signal_utils import signalUtils

result = signalUtils("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
