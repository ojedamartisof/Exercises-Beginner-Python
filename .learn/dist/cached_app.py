def number_of_bottles():
    for x in range(99, 2, -1):
        print(str(x) + " bottles of milk on the wall, " +
              str(x) + " bottles of milk.")
        print("Take one down and pass it around, " +
              str(int(x)-1) + " bottles of milk on the wall.")
    print("1 bottle of milk on the wall, 1 bottle of milk.")
    print("Take one down and pass it around, no more bottles of milk on the wall.")
    print("No more bottles of milk on the wall, no more bottles of milk.")
    print("Go to the store and buy some more, 99 bottles of milk on the wall.")


number_of_bottles()
