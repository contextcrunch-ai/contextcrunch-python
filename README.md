# ContextCrunch Python Client
Use the [ContextCrunch API](https://contextcrunch.com) easily with python!

## Prerequsites
- You need an API key from [https://contextcrunch.com/console/keys](https://contextcrunch.com/console/keys)
- Install contextcrunch with `pip install contextcrunch`
## Quick Start
```python
from contextcrunch import ContextCrunchClient
client = ContextCrunchClient('API_KEY_HERE')

compressed = client.compress(
  context=['compress this text'],
  prompt='last message',
  compression_ratio=0.95
)
print(f'Although this text is too short to compress, we can see the API works! {compressed}')
```

## Uploading to PyPi

```bash
python3 -m build
python3 -m twine upload dist/*
```

Username: `__token__`