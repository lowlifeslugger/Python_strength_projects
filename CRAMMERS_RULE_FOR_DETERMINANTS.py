import numpy as np
# accepting user input
print(" ax + by + cy = d\n ex + fy +gz = h\n ix + jy +kz = l\n")
a ,b , c , d = input("Enter variable values (a) : ") , input("Enter variable values (b) : ") ,input("Enter variable values (c) : ") ,input("Enter variable values (d) : ")
e ,f , g , h = input("Enter variable values (e) : ") ,input("Enter variable values (f) : ") , input("Enter variable values (g) : ") , input("Enter variable values (h) : ")
i ,j , k , l = input("Enter Variable Values (i) : ") ,input("Enter Variable Values (j) : ") ,input("Enter Variable Values (k) : ") ,input("Enter Variable Values (l) : ") 
a , b , c , d , e , f ,g ,h , i , j , k , l = float(a) , float(b) , float(c) , float(d) , float(e) , float(f) , float(g) , float(h) , float(i) , float(j) , float(k) , float(l)
# marking the Matrices with A being the original and B , C , D = is modified for values
A = np.array([[ a , b , c ] , [ e , f , g] , [i , j , k ]])
B = np.array([[d , b , c ], [ h , f , g] , [l , j , k ] ])
C = np.array([[a , d , c] , [ e , h , g] , [i , l , k ]])
D = np.array([[ a , b , d ] , [ e , f , h] , [ i , j , l]])
# making determinants of our matrices
E = np.linalg.det(A)
F = np.linalg.det(B)
G = np.linalg.det(C)
H = np.linalg.det(D)
# confirm values 
print(f" { A }\n { B }\n { C }\n { D }")

print(f"{ E } { F } { G } { H }")

print(f" final values\nx = {F/E} y = {G/E} z = {H/E}")
