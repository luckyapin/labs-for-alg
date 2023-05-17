
"""
Paзpaбoтaйтe aлгopитм, пpoвepяющий peзультaт игpы в кpeстики-нoлики (3х3).
"""

# Создаем игровое поле
field = [["X", "O", "X"],
        ["X", "X", "O"],
        ["O", "X", "O"]]

# Функция проверки победителя
def check_game_result(field):

    # Проверяем строки
    for row in field:
        if row[0] == row[1] == row[2] != "-":
            return f"Победил игрок - {row[0]}"

    # Проверяем столбцы
    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] != "-":
            return f"Победил игрок - {field[0][col]}"

    # Проверяем диагонали
    if field[0][0] == field[1][1] == field[2][2] != "-" or \
                field[0][2] == field[1][1] == field[2][0] != "-":
        return f"Победил игрок - {field[1][1]}"

    return "Ничья"

