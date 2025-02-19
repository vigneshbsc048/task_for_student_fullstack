

##### ////// checking name, age, grade

# class ValidationError(Exception):
#     pass


# def validate_json(data, config):
#     errors = []

#     for key, value in config.items():
#         is_required = 'mandatory' in value
#         data_type = 'string' if 'string' in value else 'number' if 'number' in value else None
#         min_length = None

#         # Extract min length if present
#         if 'min length is' in value:
#             try:
#                 min_length = int(value.split('min length is ')[1].split()[0])
#             except (ValueError, IndexError):
#                 raise ValidationError(f"Invalid configuration for {key}: {value}")

#         # Check for required fields
#         if is_required and key not in data:
#             errors.append(f"{key} is required.")
#         elif key in data:
#             # Type checking
#             if data_type == 'string' and not isinstance(data[key], str):
#                 errors.append(f"{key} must be a string.")
#             if data_type == 'number' and not isinstance(data[key], (int, float)):
#                 errors.append(f"{key} must be a number.")
#             # Min length check
#             if min_length is not None and isinstance(data[key], str) and len(data[key]) < min_length:
#                 errors.append(f"{key} must be at least {min_length} characters long.")

#     # Grade field validation (custom validation for grade)
#     if 'grade' in data:
#         if not isinstance(data['grade'], str):
#             errors.append("grade must be a string.")
#         elif data['grade'].upper() not in ['A', 'B', 'C', 'D', 'E', 'F']:
#             errors.append("grade must be a valid grade (A, B, C, D, E, F).")

#     if errors:
#         raise ValidationError(", ".join(errors))



##################### checking for name , age, clss error



###############################################################
############# working good, showing, and expcted error is working goog,
#############"name must be at least 10 characters long."
#############"data.class is required."
################## but not working data.class is required error...... 
############################################################### 

# class ValidationError(Exception):
#     pass


# def validate_json(data, config):
#     errors = []

#     for key, value in config.items():
#         is_required = 'mandatory' in value
#         data_type = 'string' if 'string' in value else 'number' if 'number' in value else None
#         min_length = None

#         # Extract min length if present
#         if 'min length is' in value:
#             try:
#                 min_length = int(value.split('min length is ')[1].split()[0])
#             except (ValueError, IndexError):
#                 raise ValidationError(f"Invalid configuration for {key}: {value}")

#         # Check for required fields
#         if is_required and key not in data:
#             errors.append(f"{key} is required.")
#         elif key in data:
#             # Type checking
#             if data_type == 'string' and not isinstance(data[key], str):
#                 errors.append(f"{key} must be a string.")
#             if data_type == 'number' and not isinstance(data[key], (int, float)):
#                 errors.append(f"{key} must be a number.")
#             # Min length check (for name field)
#             if key == 'name' and min_length is not None and isinstance(data[key], str) and len(data[key]) < min_length:
#                 errors.append(f"{key} must be at least {min_length} characters long.")

#     # Nested validation for data.class (mandatory field)
#     if 'data' in config and 'class' in config['data']:
#         if 'data' not in data or 'class' not in data['data']:
#             errors.append("data.class is required.")
#         elif not isinstance(data['data']['class'], str):
#             errors.append("data.class must be a string.")

#     if errors:
#         raise ValidationError(", ".join(errors))



###### /////// best solution for checking name, age, class, grade, and error is working good



class ValidationError(Exception):
    pass

def validate_json(data, config):
    errors = []

    for key, value in config.items():
        is_required = 'mandatory' in value
        data_type = 'string' if 'string' in value else 'number' if 'number' in value else None
        min_length = None

        # Extract min length if present
        if 'min length is' in value:
            try:
                min_length = int(value.split('min length is ')[1].split()[0])
            except (ValueError, IndexError):
                raise ValidationError(f"Invalid configuration for {key}: {value}")

        # Check for required fields
        if is_required and key not in data:
            errors.append(f"{key} is required.")
        elif key in data:
            # Type checking
            if data_type == 'string' and not isinstance(data[key], str):
                errors.append(f"{key} must be a string.")
            if data_type == 'number' and not isinstance(data[key], (int, float)):
                errors.append(f"{key} must be a number.")
            # Min length check (for name field)
            if key == 'name' and min_length is not None and isinstance(data[key], str) and len(data[key]) < min_length:
                errors.append(f"{key} must be at least {min_length} characters long.")

    # ✅ Check for 'data.class' inside a nested 'data' object
    if "data" in config and isinstance(config["data"], dict) and "class" in config["data"]:
        if "data" not in data:
            errors.append("data.class is required.")
        elif "class" not in data["data"]:
            errors.append("data.class is required.")
        elif not isinstance(data["data"]["class"], str):
            errors.append("data.class must be a string.")

    if errors:
        raise ValidationError(", ".join(errors))
