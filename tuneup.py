#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Zachary Gerber help from Joseph Hafed"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):

        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        sortby = 'cumulative'
        ps = pstats.Stats(pr).strip_dirs().sort_stats(sortby)
        ps.print_stats(10)
        # print(getvalue())
        return retval

    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    # raise NotImplementedError("Complete this decorator function")
    return inner


def read_movies(src):
    """Returns a list of movie titles."""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    # """Returns True if title is within movies list."""
    # for movie in movies:
    #     if title == movie:
    #         return True
    # return False
    return title in movies


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    # movies = [movie.lower() for movie in read_movies(src)]
    duplicates = []
    while movies:
        movie = movies.pop()
        # if movie in movies:
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    av = 7
    bh = 5
    value = timeit.Timer(stmt='find_duplicate_movies("movies.txt")', setup='from __main__ import find_duplicate_movies')
    here = value.repeat(repeat=av, number=bh)
    average = min(here) / float(bh)
    print('Best time across {} repeats of {} runs per repeat: {} sec'.format(av, bh, average))
    # @wraps(func)
    # def wrapper(*args, **kwargs):
    #     start = time.perf_counter()
    #     result = func(*args, **kwargs)
    #     end = time.perf_counter()
    #     print(f'{func.__module__}, {func.__name__}:{end-start} seconds')
    #     return result
    # return wrapper


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    timeit_helper()
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
