class A:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def print_init(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

# 创建一个空字典，用于存储狗狗的属性
dog_info = {}

# 获取用户输入的狗狗信息，可以根据需要输入不定数量的属性
while True:
    key = input("请输入属性名称 (或输入 'done' 完成输入): ")
    if key == 'done':
        break
    value = input(f"请输入狗狗的 {key}: ")
    dog_info[key] = value

# 使用提供的属性创建一个A类的实例
dog = A(**dog_info)

# 打印狗狗的属性
dog.print_init()
