# Formats the form error message
def format_form_errors(data):
    result = []
    for param, message in data:
        result.append({"param": param, "message": message[0]})
    return result