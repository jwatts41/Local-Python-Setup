def hello():
    print("Hello User")
def pack(pack1, pack2, pack3):
    return[pack1, pack2, pack3]
def eat_lunch(my_food):
    if len(my_food) == 0:
        print("I am hungry")
    else:
        for i in range(len(my_food)):
            if i == 0:
                print("First I Eat {my_food[0]}")
            else:
                print("Next I Eat {my_food[i]}")

hello()
print(pack("pack1", "pack2", "pack3"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["salmon"])
eat_lunch(["chicken", "sub", "tacos", "burrito"])
