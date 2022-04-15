start_letter = input('Введите букву латинского алфавита: ')
end_letter = input('Введите еще одну букву латинского алфавита: ')
start_letter = start_letter.upper()
end_letter = end_letter.upper()
place_st_let = ord(start_letter) - 64
place_end_let = ord(end_letter) - 64
interval_letters = abs(place_end_let - place_st_let) - 1
print(f'Буква {start_letter} находится на {place_st_let} месте.\n'
      f'Буква {end_letter} находится на {place_end_let} месте.\n'
      f'Интервал между ними {interval_letters} букв(/ы).')
