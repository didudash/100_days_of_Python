def read_names(file_with_names: str) -> list:
    with open(file_with_names) as file:
        names = file.readlines()
        names = [name.strip() for name in names]
        return names


def get_template(model_letter: str) -> list:
    with open(model_letter) as file:
        template = file.readlines()
    return template


def letter_content(template: list, name: str) -> list:
    content = template[:]
    salutation = template[0].replace("[name]", name)
    content[0] = salutation
    return content


def create_letter(name: str, content: list) -> None:
    with open(f"./Output/ReadyToSend/letter_{name}.txt", "w") as file:
        for line in content:
            file.write(line)


model_letter = "./Input/Letters/starting_letter.txt"
names = read_names("./Input/Names/invited_names.txt")
template = get_template(model_letter)

for name in names:
    content = letter_content(template, name)
    create_letter(name, content)
