
def nonWorking(reason:str = None):
    def wrap(fn):
        def wrapper(*args, **kwargs):
            # Perform some non-working behavior or logic here
            if reason:
                raise NotImplementedError(f"{fn.__name__} is currently not functional, reason: {reason}.")
            else:
                raise NotImplementedError(f"{fn.__name__} is currently not functional.")
            exit(1)
        return wrapper
    return wrap
