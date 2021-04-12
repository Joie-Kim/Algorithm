def solution(phone_book):
    phone_book.sort()
    answer = True
    
    for n in range(len(phone_book) - 1):
        if phone_book[n] in phone_book[n+1]:
            answer = False
    
    return answer