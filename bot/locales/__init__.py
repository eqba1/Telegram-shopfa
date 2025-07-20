from importlib import import_module

_cache = {}

def translate(key: str, lang: str = 'ru', **kwargs) -> str:
    if lang not in _cache:
        _cache[lang] = import_module(f'.{lang}', __name__).MESSAGES
    text = _cache[lang].get(key, key)
    return text.format(**kwargs)
