#coding=utf-8

"""
        Автор: Колесниченко Вадим, группа № P3355
"""


from date import DateDictionaries
from time import TimeDictionaries



class DateConverter:
    """
        Класс реализующий перевод даты и времени из числового в текстовый формат
    """

    def __init__(self, date_sting):
        self.date = date_sting.split(' ')[0]
        self.time = date_sting.split(' ')[1]


    def convert_date_string(self):
        """
            Функция реализующая преобразование даты и времени из числового в текстовый формат
        """

        result = ''
        splitted_string = self.date.split('.')
        day = int(splitted_string[0])
        month = int(splitted_string[1])
        year = splitted_string[2]

        result += DateDictionaries.days[day] + ' '
        result += DateDictionaries.months[month]
        result += self.convert_year(year)

        splitted_string = self.time.split(':')
        hours = int(splitted_string[0])
        minutes = int(splitted_string[1])
        seconds = int(splitted_string[2])

        result += self.convert_hours(hours)
        result += self.convert_minutes(minutes)
        result += self.convert_seconds(seconds)

        return result


    def convert_year(self, year):
        """
            Функция конверктирующая код из числового формата в текстовый
            Входные данные:
            год в формате число
            Выходные данные:
            год в  формате строки
        """

        result_string = ' '
        list_year = [int(x) for x in list(year)]

        if list_year[0] != 0:
            if list_year[1] == 0 and list_year[2] == 0 and list_year[3] == 0:
                result_string += DateDictionaries.year_thousands_number_rounded[list_year[0]] + \
                               DateDictionaries.thousands['rounded'] + ' года'
                return result_string
            else:
                result_string += DateDictionaries.year_thousands_number[list_year[0]] + ' '
                if list_year[0] == 1:
                     result_string += DateDictionaries.thousands['singular'] + ' '
                elif list_year[0] in [2, 3, 4]:
                    result_string += DateDictionaries.thousands['plural_alt'] + ' '
                else:
                    result_string += DateDictionaries.thousands['plural'] + ' '

        if list_year[1] != 0:
            if list_year[2] == 0 and list_year[3] == 0:
                result_string += DateDictionaries.hundreds_rounded[list_year[1]] + ' года'
                return result_string
            else:
                result_string += DateDictionaries.hundreds[list_year[1]] + ' '

        if list_year[2] != 0:
            if list_year[3] == 0:
                result_string += DateDictionaries.tens_rounded[list_year[2]] + ' года'
                return result_string
            else:
                if list_year[2] == 1:
                    ten = str(list_year[2]) + str(list_year[3])
                    result_string += DateDictionaries.first_ten_year[int(ten)] + ' года'
                    return result_string
                else:
                    result_string += DateDictionaries.tens[list_year[2]] + ' '

        if list_year[3] != 0:
            result_string += DateDictionaries.year_last_number[list_year[3]] + ' года'

        return result_string


    def convert_hours(self, hours):
        """
            Функция конверктирующая код из числового формата в текстовый
            Входные данные:
            час в формате число
            Выходные данные:
            час в  формате строки
        """

        result_string = ' '

        if hours < 10:
            result_string += TimeDictionaries.decimials[hours]['hours'] + ' '

        elif hours < 20:
            result_string += TimeDictionaries.ten[hours] + ' '

        else:
            list_hour = list(str(hours))
            result_string += TimeDictionaries.tens[int(list_hour[0])] + ' '
            result_string += TimeDictionaries.decimials[int(list_hour[1])]['hours'] + ' '

        if hours in [10, 11, 12]:
            result_string += TimeDictionaries.hours['plural']

        elif hours % 10 == 1:
            result_string += TimeDictionaries.hours['singular']

        elif hours % 10 > 0 and hours % 10 < 5:
            result_string += TimeDictionaries.hours['plural_alt']

        else:
            result_string += TimeDictionaries.hours['plural']

        return result_string


    def convert_minutes(self, minutes):
        """
            Функция конверктирующая код из числового формата в текстовый
            Входные данные:
            минута в формате число
            Выходные данные:
            минута в  формате строки
        """
        result_string = ' '
        if minutes < 10:
            result_string += TimeDictionaries.decimials[minutes]['else'] + ' '

        elif minutes < 20:
            result_string += TimeDictionaries.ten[minutes] + ' '

        elif minutes % 10 == 0:
            result_string += TimeDictionaries.tens[minutes // 10] + ' '

        else:
            list_minute = list(str(minutes))
            result_string += TimeDictionaries.tens[int(list_minute[0])] + ' '
            result_string += TimeDictionaries.decimials[int(list_minute[1])]['else'] + ' '

        if minutes in [10, 11, 12]:
            result_string += TimeDictionaries.minutes['plural']

        elif minutes % 10 == 1:
            result_string += TimeDictionaries.minutes['singular']

        elif minutes % 10 > 0 and minutes % 10 < 5:
            result_string += TimeDictionaries.minutes['plural_alt']

        else:
            result_string += TimeDictionaries.minutes['plural']
        return result_string


    def convert_seconds(self, seconds):
        """
            Функция конверктирующая код из числового формата в текстовый
            Входные данные:
            секунда в формате число
            Выходные данные:
            секунда в  формате строки
        """
        result_string = ' '
        if seconds < 10:
            result_string += TimeDictionaries.decimials[seconds]['else'] + ' '

        elif seconds < 20:
            result_string += TimeDictionaries.ten[seconds] + ' '

        elif seconds % 10 == 0:
            result_string += TimeDictionaries.tens[seconds // 10] + ' '

        else:
            list_second = list(str(seconds))
            result_string += TimeDictionaries.tens[int(list_second[0])] + ' '
            result_string += TimeDictionaries.decimials[int(list_second[1])]['else'] + ' '

        if seconds in [10, 11, 12]:
            result_string += TimeDictionaries.seconds['plural']

        elif seconds % 10 == 1:
            result_string += TimeDictionaries.seconds['singular']

        elif seconds % 10 > 0 and seconds % 10 < 5:
            result_string += TimeDictionaries.seconds['plural_alt']

        else:
            result_string += TimeDictionaries.seconds['plural']
        return result_string


if __name__ == '__main__':
    assert DateConverter('01.01.0001 00:00:00').convert_date_string() == 'Первое января первого года ноль часов ноль минут ноль секунд'
    assert DateConverter('10.04.1500 02:10:05').convert_date_string() == 'Десятое апреля одна тысяча пятисотого года два часа десять минут пять секунд'
    assert DateConverter('06.09.1990 23:45:06').convert_date_string() == 'Шестое сентября одна тысяча девятьсот девяностого года двадцать три часа сорок пять минут шесть секунд'
    assert DateConverter('12.06.1995 15:22:01').convert_date_string() == 'Двенадцатое июня одна тысяча девятьсот девяносто пятого года пятнадцать часов двадцать две минуты одна секунда'
    assert DateConverter('20.08.2000 07:30:23').convert_date_string() == 'Двадцатое августа двухтысячного года семь часов тридцать минут двадцать три секунды'
    assert DateConverter('27.10.2007 04:20:00').convert_date_string() == 'Двадцать седьмое октября две тысячи седьмого года четыре часа двадцать минут ноль секунд'
    assert DateConverter('25.07.2019 08:17:59').convert_date_string() == 'Двадцать пятое июля две тысячи девятнадцатого года восемь часов семнадцать минут пятьдесят девять секунд'
    assert DateConverter('30.11.5031 09:48:45').convert_date_string() == 'Тридцатое ноября пять тысяч тридцать первого года девять часов сорок восемь минут сорок пять секунд'
    assert DateConverter('31.12.9999 23:59:58').convert_date_string() == 'Тридцать первое декабря девять тысяч девятьсот девяносто девятого года двадцать три часа пятьдесят девять минут пятьдесят восемь секунд'
