# DONE
def solution(genres, plays):
    answer = []
    raw = list(zip(genres, plays))
    by_genre = {g: 0 for g in genres}
    for g, p in raw:
        by_genre[g] += p
    by_genre = {k: v for k, v in sorted(
        by_genre.items(), key=lambda x: x[1], reverse=True)}
    for genre in by_genre.keys():
        temp = list(filter(lambda x: x[0] == genre,
                           sorted(raw, reverse=True)))[:2]
        for song in temp:
            index = raw.index(song)
            if index in answer:
                answer.append(raw.index(song, index+1))
            else:
                answer.append(index)
    return answer
