from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cities = [city.lower() for city in cities]
    cache = deque()
    time = 0

    for city in cities:
        if city in cache:
            time += 1
            cache.remove(city)
        else:
            time += 5
            if len(cache) >= cacheSize:
                cache.popleft()
        cache.append(city)

    return time
