post_response_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "priority": {"type": "string", "enum": ["низкий", "средний", "высокий"]},
        "steps": {
            "type": "array",
            "items": {"type": "string"}
        },
        "expected_result": {"type": "string"}
    },
    "required": ["id", "name", "description", "priority", "steps", "expected_result"]
}

get_all_response_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "steps": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "expected_result": {
                "type": "string"
            },
            "priority": {
                "type": "string",
                "enum": ["низкий", "средний", "высокий"]
            }
        },
        "required": ["id", "name", "description", "steps", "expected_result", "priority"],
    }
}

get_by_id_json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "steps": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "expected_result": {
            "type": "string"
        },
        "priority": {
            "type": "string",
            "enum": ["низкий", "средний", "высокий"]
        }
    },
    "required": ["id", "name", "description", "steps", "expected_result", "priority"],
}

delete_response_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "detail": {
            "type": "string",
            "enum": ["Test case deleted.", "Test case not found."]
        }
    }
}
