a_string='12'
b_int=13

print("Datatype of a_string before converting:",type(a_string))

a_string=int(a_string)

print("Datatype of a_string after converting:",type(a_string))

c=a_string+b_int

print(c)
print("Datatype of c:",type(c))