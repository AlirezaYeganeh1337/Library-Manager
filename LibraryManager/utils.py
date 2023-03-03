def dynamic_query(query_params: dict.__delitem__, model_fields: list) -> dict:
    return {f"{k}{'' if v.lower() in ['true', 'false'] else '__icontains'}": v.title()
    if v.lower() in ['true', 'false'] else v for k, v in query_params
            if k in model_fields and v is not None}
