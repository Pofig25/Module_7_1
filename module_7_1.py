# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.

# Реализовать без "классовой зависимости" не получилось, и т.к. проверка идёт по наличию в магазине, то "Shop" будет
# надклассом, а "Product" подклассом.

class Shop:
    __file_name = 'products.txt'                            # Инкапсулированный атрибут __file_name = 'products.txt'.

    def get_products(self):                                 # Метод get_products(self), который
        file = open(self.__file_name, 'r')                  # считывает всю информацию из файла __file_name,
        product = file.read()                               # закрывает его и возвращает единую
        file.close()                                        # строку со всеми товарами из файла __file_name.
        return product

    def add(self, *products):                 # Метод add(self, *products), принимает неогр. кол-во объектов кл. Product.

        file = open(self.__file_name, 'a')                      # Добавляет в файл __file_name каждый продукт из products,
        for i in products:                                      # если его ещё нет в файле (по названию).
            if str(i) in self.get_products():                   # Если такой продукт уже есть, то не добавляет
                print(f"Продукт {str(i)} уже есть в магазине")  #и выводит строку 'Продукт <название> уже есть в магазине'.
            else:
                file.write(str(i) + '\n')
        file.close()

class Product(Shop):
    def __init__(self, name, weight, category):
        self.name = name                                # Атрибут name - название продукта (строка).
        self.weight = weight                            # Атрибут weight - общий вес товара (дробное число) (5.4 и т.п.).
        self.category = category                        # Атрибут category - категория товара (строка).

    def __str__(self):                                              # Метод __str__, который возвращает строку в формате
        return f'{self.name}, {self.weight}, {self.category}'       # '<название>, <вес>, <категория>'.

# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())