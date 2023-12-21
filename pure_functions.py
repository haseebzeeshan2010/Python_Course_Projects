#NOTE: pure functions are functions that have no effect beyond their own scope.
#They must fulfill these criteria

#1. Must accept list as an argument
#2. Original list must stay intact
#3. Must return a new list

#Why are the used:

#They always do exactly what they are supposed to do
#They have the ability to cache because return will always be the same
#They work well with multi-threaded programs

#An exxample of a pure function
def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl


#Multi threaded programs are programs that have many threads of data
#Pure functions don't alter data on global scope ensuring data stays reliable