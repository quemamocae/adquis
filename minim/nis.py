import re

pattern = re.compile(r"</h(\d)>\n", re.MULTILINE | re.IGNORECASE)
text = "<h1>Title</h1>\n<h2>Subtitle</h2>\n<h3>Subheading</h3>\n"

matches = pattern.findall(text)
print(matches)
