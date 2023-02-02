#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def StringCompressing(text):
    count = 1
    compressed_string = ''

    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count +=1
        else:
            compressed_string += str(count) + text[i]
            count = 1

    compressed_string += str(count) + text[len(text) - 1]
    return compressed_string

def StringDecopressing(text):
    decompressed_string = ''
    temp = ''
    # 18q3r [18q3r, 1q3r]
    # 1q3r
    for i in text:
        for element in i:
            if element.isdigit():
                temp += element
            else:
                decompressed_string += element * int(temp)
                temp = ''
        decompressed_string += '\n'
    return decompressed_string

def main():
    compressed_data = open('hw_024_compressed_data', 'w')
    w = True

    while w:
        print('Enter your new text. Enter "quit" to exit.')
        q = input()
        if q.lower() == 'quit':
            w = False
        else:
            compressed_data.writelines(StringCompressing(q) + '\n')

        compressed_data.close()

        compressed_data = open('hw_024_compressed_data', 'r')
        compressed_string = compressed_data.readlines()
    compressed_data.close()

    q = StringDecopressing(compressed_string)

    decompressed_data = open('Decompressed_data', 'w')
    for element in compressed_string:
        decompressed_data.writelines(element)
    decompressed_data.close()



if __name__ == "__main__":
    main()