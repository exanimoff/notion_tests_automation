RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "object": {"type": "string"},
        "id": {"type": "string"},
        "created_time": {"type": "string"},
        "last_edited_time": {"type": "string"},
        "created_by": {
            "type": "object",
            "properties": {
                "object": {"type": "string"},
                "id": {"type": "string"}
            },
            "required": ["object", "id"]
        },
        "parent": {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "page_id": {"type": "string"},
                "block_id": {"type": "string"},
                "discussion_id": {"type": "string"}
            },
            "required": ["type"]
        },
        "rich_text": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "text": {
                        "type": "object",
                        "properties": {
                            "content": {"type": "string"},
                            "link": {"type": ["null", "string"]}
                        },
                        "required": ["content"]
                    }
                },
                "required": ["type", "text"]
            }
        }
    },
    "required": ["object", "id", "created_time", "last_edited_time", "created_by", "parent", "rich_text"]
}


RESPONSE_SCHEMA_400_401_404 = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "object": {
      "type": "string"
    },
    "status": {
      "type": "integer"
    },
    "code": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "request_id": {
      "type": "string"
    }
  },
  "required": [
    "object",
    "status",
    "code",
    "message",
    "request_id"
  ]
}