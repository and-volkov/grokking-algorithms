from collections import deque  # очередь

graph = {
    'you': ['alice', 'bob', 'claire'], 'bob': ['anuj', 'peggy'],
    'alice': ['peggy'], 'claire': ['thom', 'jonny'], 'anuj': [],
    'thom': [], 'peggy': [], 'jonny': []
}


def person_is_target(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph.get(name)
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_target(person):
                print(f'{person} is target')
                return True
            else:
                search_queue += graph.get(person)
                searched.append(person)
    return False


search('you')
