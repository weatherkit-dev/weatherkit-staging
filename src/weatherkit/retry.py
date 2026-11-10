def with_backoff(call, retries=3, jitter=0.0):
    return call()
