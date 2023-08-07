import requests

def find_book_by(search:str,op:str):
    if op == 'title':
        return find_by_title(search)
    else:
        return find_by_author(search)
        

def find_by_title(param:str):
    titles = []
    payload = {'q':param}
    r = requests.get('https://openlibrary.org/search.json',params=payload)
    info = r.json()
    print(r.url)
    #titles = [doc['title'] for doc in info['docs']]
    return [{'title':entry['title'],'description':entry['description'] if 'description' in entry else None} for entry in info['docs']]

def find_by_author(param:str):
    payload = {'q':param}
    r = requests.get('https://openlibrary.org/search/authors.json',params=payload)
    print(r.url)
    if r.status_code == 200:
        info = r.json()
        key = [doc['key'] for doc in info['docs']]
        print(key[0])
        return get_author_info(key[0])
            
def get_author_info(olid:str):
    r = requests.get(f'https://openlibrary.org/authors/{olid}/works.json')
    if r.status_code == 200:
        info = r.json()
        return [{'title':entry['title'],'description':entry['description'] if 'description' in entry else None} for entry in info['entries']]
       