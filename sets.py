def remove_duplicates(random_list):
   return list(set(random_list))



def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__ == "__main__":
    run()