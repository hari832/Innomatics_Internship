import textwrap

def wrap(string, max_width):
    result=textwrap.fill(string,max_width)
    
    return result

if __name__ == '__main__':