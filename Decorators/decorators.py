from functools import wraps

def make_html(element):
    def make_html_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function()
            return '<' + element + '>' + result + '</' + element + '>'
        return wrapper
    return make_html_decorator
