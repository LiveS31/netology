def para(boys, girls):
    boys.sort(), girls.sort()
    if len(boys) != len(girls):
        print ('Kто-то может остаться без пары!')
    else:
        for i in range (len(boys)):
            print(f'{boys[i]} и {girls[i]}')
para(['Peter', 'Alex', 'John', 'Arthur', 'Richard'],['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'])