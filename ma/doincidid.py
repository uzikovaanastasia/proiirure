try:
    # Some code that may raise an exception
    result = some_function()
except SomeSpecificException as e:
    # Handle the specific exception, such as logging or cleaning up
    log_error(e)
    # Re-raise the caught exception to allow it to propagate further
    raise e
