import sys

def print_lol(the_list, indent=False, level=0, fn=sys.stdout):

    for each_line in the_list:
        if isinstance(each_line, list):
            print_lol(each_line, indent, level+1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print ('\t', end='', file=fn)
            print (each_line, file=fn)



