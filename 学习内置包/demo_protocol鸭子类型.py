from typing import Protocol


class Animal(Protocol):
    """申明协议类型"""

    def eat(self):
        pass

    def drink(self):
        pass


class Dog:
    """与ABC不同的是：不需要显示继承，甚至可以不知道协议是什么"""

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")


class Cat:
    def eat(self):
        print("eat")


def do_something(animal: Animal):
    animal.eat()
    animal.drink()


if __name__ == "__main__":
    dog = Dog()
    do_something(dog)
    cat = Cat()
    do_something(cat)  # 猫没有实现完整方法，运行时报错
