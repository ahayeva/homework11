if __name__ == "__main__":
    #exercise11
    try:
        name = input("vashe imya: ")
        age = int(input("vash vik: "))
        if age < 0 or age > 130:
            raise ValueError("nекоректний вік")
        print(f"pryvit, {name}! tviy vik — {age}")
    except ValueError as e:
        print(f"pomylka: {e}")
        #exercise 2
        def form_greeting(name, age):
            if age < 0 or age > 130:
                raise ValueError("ne korektnyi vik")
            return f"pryvit, {name}! vash vik — {age}"
        try:
            name = input("vashe imya: ")
            age = int(input("vash vik: "))
            greeting = form_greeting(name, age)
            print(greeting)
        except ValueError as e:
            print(f"pomylka: {e}")
            #exercise 3
            try:
                numbers = []
                while True:
                    num = int(input("введіть число (для завершення введіть 0): "))
                    if num < 0:
                        raise ValueError("введено від'ємне число")
                    if num == 0:
                        break
                    numbers.append(num)
                total_sum = sum(numbers)
                print(f"suma: {total_sum}")
            except ValueError as e:
                print(f"pomylka: {e}")

                #exercise4
                def calculate_sum(lst):
                    if any(num < 0 for num in lst):
                        raise ValueError("введено від'ємне число")
                    return sum(lst)
                try:
                    numbers = []
                    while True:
                        num = int(input("введіть число для завершення введіть 0: "))
                        if num == 0:
                            break
                        numbers.append(num)
                    total_sum = calculate_sum(numbers)
                    print(f"сума чисел: {total_sum}")
                except ValueError as e:
                    print(f"помилка: {e}")