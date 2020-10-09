# 테스트 2, 15번 통과 못함
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
            answer.append(raw.index(song))
    return answer
