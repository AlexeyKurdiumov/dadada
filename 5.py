def wrap_in_html_tag(tag, text):
    valid_tags = [
        "a", "abbr", "b", "body",
        "caption", "cite", "code", 
        "div", "form", "h1", "h2",
        "h3", "h4", "h5", "h6", 
        "header", "i", "s"
    ]
    if tag in valid_tags:
        return f"<{tag}>{text}</{tag}>"
    else:
        return "Введён неверный тег"
print(wrap_in_html_tag("i", "Python"))
print(wrap_in_html_tag("h1", "Заголовок"))
print(wrap_in_html_tag("span", "Текст"))
