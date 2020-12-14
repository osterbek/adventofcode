from pathlib import Path


def binary_leading_zeroes(num):
    return bin(num)[:2] + '0' * (38 - len(bin(num))) + bin(num)[2:]


def masking(num, mask, replace_set):
    num_bin = binary_leading_zeroes(num)
    for i in range(0, len(num_bin) - 2):
        if mask[len(mask) - 1 - i] in replace_set:
            num_bin = num_bin[:(len(num_bin) - 1 - i)] + mask[len(mask) - 1 - i] + num_bin[(len(num_bin) - 0 - i):]
    return int(num_bin, 2)


def floating(address_list, mask):
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            temp_list = []
            for doubling_candidate in address_list:
                temp_list.append((doubling_candidate[:i+2] + '0' + doubling_candidate[i+3:]))
                temp_list.append((doubling_candidate[:i+2] + '1' + doubling_candidate[i+3:]))
            address_list = temp_list
    return [int(i, 2) for i in address_list]


def writing(addresses, values, adr, val):
    if adr in addresses:
        values[addresses.index(adr)] = val
    else:
        values.append(val)
        addresses.append(adr)
    return addresses, values


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_14.txt').read_text().split('\n')]
    mask = 36 * '0'
    addr_part_1 = []
    values_part_1 = []
    addr_part_2 = []
    values_part_2 = []
    for command in dataset:
        if 'mask' in command:
            mask = command[7:]
            print('.', end='')
        else:
            address = int(command[4:command.find(']')])
            value = int(command.split(' ')[2])
            addr_part_1, values_part_1 = writing(addr_part_1, values_part_1, address, masking(value, mask, ['0', '1']))
            for address in floating([binary_leading_zeroes(masking(address, mask, ['1']))], mask):
                addr_part_2, values_part_2 = writing(addr_part_2, values_part_2, address, value)
    print()
    print('Answer part 1 = {:d} '.format(sum(values_part_1)), (sum(values_part_1) == 9296748256641))
    print('Answer part 2 = {:d} '.format(sum(values_part_2)), (sum(values_part_2) == 4877695371685))
