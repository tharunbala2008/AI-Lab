def list_statistics(values):
    if not values:
        raise ValueError("List cannot be empty")
    return {"minimum": min(values), "maximum": max(values),
            "range": max(values) - min(values)}
