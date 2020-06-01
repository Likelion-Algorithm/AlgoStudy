def pivot(n):
    if n<=1:
        return 1
    return(pivot(n-1)+(n-2))