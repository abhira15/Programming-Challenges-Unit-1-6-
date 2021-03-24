import queue as Queue

def calc_erdos(adj_lst):
    erdos_numbers = {}
    queue = Queue.Queue()
    queue.put(('Erdos, P.', 0))
    while not queue.empty():
        (cur_author, dist) = queue.get()
        if cur_author not in erdos_numbers:
            erdos_numbers[cur_author] = dist
        for author in adj_lst[cur_author]:
            if author not in erdos_numbers:
                queue.put((author, dist+1))        
    return erdos_numbers


num_scenario = int(input())
for idx_scenario in range(1, num_scenario+1):
    [num_papers, num_queries] = [int(num) for num in input().split()]
    adj_lst = {}
    for _ in range(num_papers):
        paper = input()
        [authors, title] = paper.split(':')
        authors = [author.strip() for author in authors.split(',')]
        
        authors = [', '.join(first_last) for first_last in zip(authors[::2], authors[1::2])]
        
        for author in authors:
            author_neighbors = adj_lst.get(author,set())
            for coauthor in authors:
                if coauthor == author:
                    continue
                author_neighbors.add(coauthor)
            adj_lst[author] = author_neighbors
    erdos_numbers = calc_erdos(adj_lst)
    
print("Scenario",num_scenario)

while num_queries>0  :    
    author = input()
    print('%s %s' % (author, erdos_numbers.get(author,'infinity')))
    num_queries = num_queries - 1    
