# link: https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    results = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
    answer = ''
    
    for i in range(len(survey)):
        choice = choices[i]
        character = survey[i]
        if choice < 4:
            # 비동의
            results[character[0]] += (4 - choice)
        elif choice > 4:
            # 동의
            results[character[1]] += (choice - 4)
    
    if results['R'] >= results['T']: answer += 'R'
    else: answer += 'T'
    
    if results['C'] >= results['F']: answer += 'C'
    else: answer += 'F'
    
    if results['J'] >= results['M']: answer += 'J'
    else: answer += 'M'
    
    if results['A'] >= results['N']: answer += 'A'
    else: answer += 'N'
    
    return answer