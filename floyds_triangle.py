def floyds_triangle(k):
    n  = 0
    for i in range(1,k+1):
        for j in range(i):
          n += 1
          print(n,end = " ")
        print()  


floyds_triangle(5)