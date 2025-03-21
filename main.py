from data import Data, check_name
import os
import json

def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Invalid input')

def input_name(msg):
    while True:
        s = input(msg)
        if check_name(s):
            return s

def main():
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as f:
            json.dump([], f)
    with open('data.json', 'r') as f:
        data = json.load(f)
    while(True):
        print('1. add data')
        print('2. show data')
        print('3. exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            round = input_int('Enter round: ')
            name = input_name('Enter name: ')
            level = input_int('Enter level: ')
            num = input_int('Enter num: ')
            cost = input_int('Enter cost: ')
            not_found = True
            for d in data:
                if d['round'] == round and d['name'] == name and d['level'] == level and d['num'] == num:
                    not_found = False
                    if d['cost'] != cost:
                        print('Conflict data, which one do you want to keep?')
                        print('Old data:', d)
                        user_choice = input_int('1. old data\n2. new data\n')
                        if user_choice == 1:
                            break
                        else:
                            d['cost'] = cost
                            break
                    else:
                        break
            if not_found:
                data.append(Data(round, name, level, num, cost).__dict__)
            with open('data.json', 'w') as f:
                json.dump(data, f)
        elif choice == '2':
            # sort by round, name
            data.sort(key=lambda x: (x['round'], x['name']))
            for d in data:
                print(Data(d['round'], d['name'], d['level'], d['num'], d['cost']))
        elif choice == '3':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()