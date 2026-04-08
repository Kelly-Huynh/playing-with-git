def superify(name):
    return f"super{name}"

dog_result = superify("dog")
print(f"Look, it's {dog_result}!")

cat_result = superify(superify(superify("cat")))
print(f"Look, it's {cat_result}!")