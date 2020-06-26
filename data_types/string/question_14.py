def add_tag(tag, content):
    return f'<{tag}>{content}</{tag}>'


user_tag = input("Enter a html tag: ")
user_content = input("Enter the content ypu want to enclose inside the tag: ")

print(add_tag(user_tag, user_content))
