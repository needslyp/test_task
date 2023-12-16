def input_info() -> dict:
    journal = {}
    n = int(input('Write number of students: '))

    for i in range(n):
        name = input(f'Name of {i+1} student: ')
        subjects = input(f'Subjects of {i+1} student: ').split(sep=' ')
        journal[name] = subjects

    return journal

def show_all(journal: dict) -> None:
    new_journal = {key: value for key, value in sorted(journal.items(), key=lambda item: item[0], reverse=True)}
    for key in new_journal.keys():
        print(f'{key}: {str(new_journal[key])}')

def student_for_sub(journal: dict, name: str) -> list:
    if name in journal.keys():
        return journal[name]
    return 'Name not found'

def sub_for_students(journal: dict, sub: str) -> list:
    names = [name for name in journal.keys() if sub in journal[name]]
    
    if len(names) > 0:
        return names
    return 'Nothing found'

journal = input_info()
print(journal)
show_all(journal)

print(student_for_sub(journal, 'John'))
print(sub_for_students(journal, 'math'))
