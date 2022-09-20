def edit_row(row_number: int):
    return f'#edit-record-{row_number}'


def delete_row(row_number: int):
    return f'#delete-record-{row_number}'


def get_row_group(row_number):
    return f'.rt-tr-group:nth-child({row_number})'
