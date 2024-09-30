#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    Executes a function safely with given arguments.
    Think of this as giving someone a parachute before they try something risky.
    If they mess up, we let everyone know (gently) without total destruction.
    """
    try:
        result = fct(*args)
        return result
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
