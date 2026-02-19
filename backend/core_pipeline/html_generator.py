import json

def generate_html_form(fields_json, output_html):
    with open(fields_json, "r", encoding="utf-8") as f:
        fields = json.load(f)

    html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AI Generated Accessible Form</title>
<style>
body {
    font-family: Arial, sans-serif;
    padding: 30px;
}
label {
    display: block;
    margin-top: 15px;
    font-weight: bold;
}
input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
}
</style>
</head>
<body>

<h2>AI-Generated Accessible Form</h2>
<form>
"""

    for field in fields:
        label = field.get("label", "Unknown Field")
        value = field.get("value", "")
        field_id = label.lower().replace(" ", "_")

        html += f"""
<label for="{field_id}">{label}</label>
<input type="text" id="{field_id}" name="{field_id}" value="{value}">
"""

    html += """
<br><br>
<button type="submit">Submit</button>
</form>
</body>
</html>
"""

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"HTML form generated: {output_html}")
