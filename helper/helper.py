# coding=utf-8


import json

def validate_form(form_class, data, files=None):
    form = form_class(data, files)
    if form.is_valid():
        return True, form.cleaned_data
    errors = []
    for key, field in form.declared_fields.items():
        if field.required and key not in data:
            errors.append({"field": key, "code": "missing_field"})
        elif key in form.errors:
            errors.append({"field": key, "code": "invalid"})
    return False, errors


def result_json(state=200, message='OK', result=None):
    return json.dumps(dict(status=state, message=message, result=result))
