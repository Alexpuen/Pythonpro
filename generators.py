import time

def fibo_gen(max = None):
    n1, n2 = 0, 1
    counter = 0
    while not max or counter <= max: 
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux



def run():
    fibonacci = fibo_gen(20)
    i= 1
    for element in fibonacci:
        print(str(i)+ " Vueltas")
        print(element)
        time.sleep(0.7)
        i +=1

if __name__ == "__main__":
    run()