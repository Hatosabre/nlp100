import os
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\01.preparation" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

from common import n_gram

STR1 = "paraparaparadise"
STR2 = "paragraph"

X = n_gram(STR1, 2)
Y = n_gram(STR2, 2)

add_XY = list(set(X) | set(Y))
and_XY = list(set(X) & set(Y))
diff_XY = list(set(X) - set(Y))
print("X+Y", add_XY)
print("X×Y", and_XY)
print("X-Y", diff_XY)
print("se in X", "se" in X)
print("se in Y", "se" in Y)
