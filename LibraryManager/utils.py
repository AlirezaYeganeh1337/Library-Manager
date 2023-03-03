from typing import Any, ItemsView


def dynamic_query(
    query_params: ItemsView[str, str], model_fields: list[str]
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    for key, value in query_params:
        if key not in model_fields:
            continue

        value_is_bool = value.lower() in ["true", "false"]

        fixed_key = f"{key}{'' if value_is_bool else '__icontains'}"

        fixed_value = value.title() if value_is_bool else value

        params[fixed_key] = fixed_value

    return params
