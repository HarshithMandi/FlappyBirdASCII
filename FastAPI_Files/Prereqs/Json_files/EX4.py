import json

def parse_json(raw):
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None
    
data=parse_json ('{"name":"harshith"}')
print(data)