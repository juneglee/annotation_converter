def cast(value, type_conv, default=None):
    if value is None:
        return default
    try:
        return type_conv(value)
    except Exception:
        return default
