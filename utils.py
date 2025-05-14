def safe_get(d, key, default):
    return default if d.get(key) is None else d.get(key, default)
