def solution(genres, plays):
    song = {}
    genres_total = {}
    answer = []

    for g, (idx, p) in zip(genres, enumerate(plays)):
        try: 
            song[g].append((idx, p))
            genres_total[g] += p
        except:
            song[g] = [(idx, p)]
            genres_total[g] = p

    for gp in sorted(genres_total.items(), reverse=True, key=lambda item: item[1]):
        song[gp[0]].sort(key=lambda item: (-item[1], item[0]))
        answer.append(song[gp[0]][0][0])
        if len(song[gp[0]]) > 1:
            answer.append(song[gp[0]][1][0])

    return answer
