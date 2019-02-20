########################################################################################################################
# Create a func that reveres a string
# "Hi my name is Henry" should be :
# "yenrH si eman ym iH"
#
#
########################################################################################################################


def reversing_str(a):
    if not a:
        return "Sorry wrong input"
    else:
        return a[::-1]


r_a = reversing_str("Hi my name is Henry")
e_a = reversing_str("hi")
c_a = reversing_str("")

print(r_a)
print(e_a)
print(c_a)