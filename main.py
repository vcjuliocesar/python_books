import books
def run():
    while True:
        options = ('title','author')
        print('Choose an option')
        
        op = input('Do you want to search by title or author: ').lower()
        
        if op in options:
            search = input(f'Enter a {op}: ')
            result = books.find_book_by(search,op)
            print(result)
        else:
            print('invalid option')
        
        answer = input('Do you want to check another book o author (yes/no) ').lower()
        
        if answer != 'yes':
            print('Bye')
            break
        
if __name__ == '__main__':
    run()