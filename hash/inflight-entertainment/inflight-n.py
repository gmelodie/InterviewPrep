# O(n) solution
from collections import defaultdict

def can_watch_two_movies(flight_length, movie_lengths):
    lengths_map = defaultdict(int)

    for i, length in enumerate(movie_lengths):
        if length <= 0:
            raise ValueError("Invalid movie lenght zero at index " + str(i))
        lengths_map[length] += 1

    for length in movie_lengths:
        complement_length = flight_length - length

        if complement_length in lengths_map:
            if complement_length == length and lengths_map[length] == 1:
                continue
            return True

    return False


if __name__ == "__main__":
    flight_length = int(input())
    movie_lengths = [int(a) for a in input().split()]
    print(can_watch_two_movies(flight_length, movie_lengths))
