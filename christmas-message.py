christmas = lambda name=None: print(f"Merry Christmas {name.capitalize() if name != None else ''}!" + "\n","\n".join([" " * int(10 - i) + ("*" * int(i * 2 + 1)) for i in range(10)]),"\n".join([f"{' '*9}|||" for x in range(3)]),f"{' '*5}-----------", sep="\n")
christmas() #when calling the method, you can add a name to the person you wish him a merry christmas.
