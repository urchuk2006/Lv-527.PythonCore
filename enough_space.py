def enough(cap, on, wait):
    # Your code here
    if cap >= on + wait:
        return 0
    else:
        return on+wait-cap
    
