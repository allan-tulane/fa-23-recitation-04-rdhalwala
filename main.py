import random
import time
import tabulate


def qsort(a, pivot_fn):
  if len(a) <= 1:
    return a
  else:
    pivot = pivot_fn(a)
    smaller = []
    larger = []
    equal = []
    for x in a:
      if x < pivot:
        smaller.append(x)
      elif x > pivot:
        larger.append(x)
      else:
        equal.append(x)
    return qsort(smaller, pivot_fn) + equal + qsort(larger, pivot_fn)


#make a random pivot function
def random_pivot(a):
  return random.choice(a)


#first element is pivot
def first_pivot(a):
  return a[0]


#selection sort from notes
def selection_sort(L):
  for i in range(len(L)):
    # print(L)
    m = L.index(min(L[i:]))
    L[i], L[m] = L[m], L[i]
  return L


def time_search(sort_fn, mylist):
  """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
  start = time.time()
  sort_fn(mylist)
  return (time.time() - start) * 1000
  ###


#replit told me to make functions, couldnt use lambda
def qsort_fixed_pivot(a):
  return qsort(a, first_pivot)


def qsort_random_pivot(a):
  return qsort(a, random_pivot)


def tim_sort(a):
  return sorted(a)


def ssort(a):
  return selection_sort(a)


def compare_sort(
    sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
  #WTF DO I DO WITH TIM
  #tim_sort =  lambda a: sorted(a)
  #first element pivot
  #qsort_fixed_pivot = lambda a: qsort(a, first_pivot)
  #random pivot
  #qsort_random_pivot = lambda a: qsort(a, random_pivot)
  #selection sort with array a
  #ssort = lambda a: selection_sort(a)

  #resutls
  result = []

  #iterat through the different sizes
  for size in sizes:
    # create list in ascending order
    random_list = list(range(size))
    # random_list = list(mylist)
    random.shuffle(random_list)

    result.append([
        size,
        time_search(qsort_fixed_pivot, random_list),
        time_search(qsort_random_pivot, random_list),
        # time_search(ssort, random_list),
        time_search(tim_sort, random_list)
    ])
    # if size == 50000: break

  return result
  ###
  """
    Compare the running time of different sorting algorithms.

    Returns:
    This makes no sense why does it say linear and binary search??
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
  ### TODO - sorting algorithms for comparison


def print_results(results):
  """ change as needed for comparisons """
  print(
      tabulate.tabulate(
          results,
          headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim_sort'],
          floatfmt=".3f",
          tablefmt="github"))


def test_print():
  print_results(compare_sort())


random.seed()
test_print()
