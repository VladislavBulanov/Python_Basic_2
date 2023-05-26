while True:
    ip_address = input('Введите IP-адрес: ')
    address_parts = ip_address.split('.')

    if len(address_parts) != 4:
        print('Адрес — это четыре числа, разделённые точками.\n')
    else:

        for element in address_parts:
            if not element.isdigit():
                print(f'{element} - это не целое число.\n')
                break
            elif int(element) > 255:
                print(f'{element} превышает 255.\n')
                break
        # У for и while может быть прописан блок else. Он выполняется в том
        # случае, если цикл завершился "штатно", без досрочного выхода:
        else:
            print('IP-адрес корректен.')
            break
