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
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat")


def do_something(animal: Animal):
    animal.eat()
    animal.drink()


class Student(Protocol):
    """
    声明一种类型有多个属性
    """

    name: str
    age: int


def use_attr(instance: Student):
    """与Student 有相同属性的才可以传入"""
    print(instance.name)
    print(instance.age)


if __name__ == "__main__":
    dog = Dog()
    do_something(dog)
    use_attr(dog)  # 猫的不具备所有属性
    cat = Cat("jm", 5)
    do_something(cat)  # 猫没有实现完整方法，运行时报错
    use_attr(cat)
