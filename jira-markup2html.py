import re

def jira_to_html(jira_text):
    # Headers
    jira_text = re.sub(r"h(\d)\.\s(.+)", r"<h\1>\2</h\1>", jira_text)
    # Bold text
    jira_text = re.sub(r"\*(.*?)\*", r"<strong>\1</strong>", jira_text)
    # Italic text
    jira_text = re.sub(r"_(.*?)_", r"<em>\1</em>", jira_text)
    # Strikethrough text
    jira_text = re.sub(r"-{2}(.*?)-{2}", r"<del>\1</del>", jira_text)
    # Monospaced text
    jira_text = re.sub(r"\{\{(.+?)\}\}", r"<code>\1</code>", jira_text)
    # Links [Link text|URL]
    jira_text = re.sub(r"\[(.+?)\|(.+?)\]", r'<a href="\2">\1</a>', jira_text)
    # Bullet points
    jira_text = re.sub(r"^\*\s(.+)", r"<li>\1</li>", jira_text, flags=re.MULTILINE)
    jira_text = re.sub(r"(<li>.*?</li>)", r"<ul>\1</ul>", jira_text, flags=re.DOTALL)
    # Numbered lists
    jira_text = re.sub(r"^\#\s(.+)", r"<li>\1</li>", jira_text, flags=re.MULTILINE)
    jira_text = re.sub(r"(<li>.*?</li>)", r"<ol>\1</ol>", jira_text, flags=re.DOTALL)
    # Color text {color:#hexcolor}text{color}
    jira_text = re.sub(r"\{color:(#?\w+)\}(.*?)\{color\}", r'<span style="color:\1">\2</span>', jira_text)
    # New lines
    jira_text = jira_text.replace("\n", "<br>")

    return jira_text