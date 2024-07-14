#!/usr/bin/python3
def safe_print_division(a, b):
    final_result = 0
    try:
        final_result = a / b
    except:
        final_result = None
    finally:
        print("Inside result: {}".format(final_result))
        return final_result
