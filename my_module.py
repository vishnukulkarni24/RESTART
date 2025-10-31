print("Top-level print: __name__ =", __name__)

def say_hello():
    print("Hello!")

if __name__ == "__main__":
    print("Running directly!")
    say_hello()
