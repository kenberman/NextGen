title = 'the Last emperor'

def fix_title(title):
    title = title.capitalize()
    title_list = title.split()
    for i in range(len(title_list)):
        if title_list[i] not in ('a', 'the', 'an', 'in', 'of'):
            title_list[i] = title_list[i].title()

    title = ' '.join(title_list)


    return title

print(fix_title('about A boy'))