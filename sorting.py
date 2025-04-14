import os
import csv

#Sortovací algoritmy

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)] #values ve stringu, ja chci pretypovat na cisla
                else:
                    data[header].append(int(value))
    return data

#seznam = [88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61]
# my_list = [1,2,3,4]
# my_list[1], my_list[3] = my_list[3], my_list[1] ## [1, 4, 3, 2]

def selection_sort(number_seznam, direction = "ascending"):
    """
    :param list number_seznam: list witch numeric array
    :param str direction: indicates sorting direction: ascending/descending
    :return: sorted number_seznam
    """
    for i in range(len(number_seznam)):
        idx = i
        for j in range(i+1, len(number_seznam)):
            if(direction == "ascending" and number_seznam[j] < number_seznam[idx]) or (direction == "descending" and number_seznam[j] > number_seznam[idx]):
                idx = j
        number_seznam[i], number_seznam[idx]  = number_seznam[idx], number_seznam[i]
    return number_seznam

## nefunkcni opis z tabule, ale je to totez co vyse
# def selection_sort(nmb_array, direction = "ascending"):
#     n = len(nmb_array)
#     for i in range(n):
#         min_max_i = i
#         for num_idx in range(n+1, n):
#             if direction == "ascending":
#                 if nmb_array[num_idx] < nmb_array[min_max_i]:
#                     min_max_i = num_idx
#             elif direction == "descending":
#                 if nmb_array[num_idx] > nmb_array[min_max_i]:
#                     min_max_i = num_idx
#         nmb_array[i], nmb_array[min_max_i] = nmb_array[min_max_i], nmb_array[i]
#
#     return nmb_array

#bubble sort meni dole  hore - mel by byl o polovinu rychlejsi nez selection sort
#zaroven musi byt  posledni krok, kdy to zkontroluje

# seznam = [88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61]
def bubble_sort(nmb_array):
    """
    :param list nmb_array: list with numeric array
    :return: sorted nmb_array
    """
    for i in range(len(nmb_array)): # cyklus projede ikrát dle délky seznamu
        for j in range(len(nmb_array)-1): # tady uz resim indexy, -1 ať nejsem out of range
            if nmb_array[j] > nmb_array[j+1]: # pokud bychom chteli descending, prohodime znamenko
                nmb_array[j], nmb_array[j+1] = nmb_array[j+1], nmb_array[j] # tady uz menime hodnoty
    return  nmb_array

def insertion_sort(nmb_array):



def main():
    data = read_data("numbers.csv")
    print(data)
    seznam = data["series_1"]
    # print(seznam) # [88, 36, 21, 54, 99, 1, 81, 18, 21, 36, 61]
    selection = selection_sort(seznam)
    #print(selection) # [1, 18, 21, 21, 36, 36, 54, 61, 81, 88, 99]
    bubble = bubble_sort(seznam)
    print(bubble)
    pass


if __name__ == '__main__':
    main()
