def main():
    tensu_syukei()

def tensu_syukei():
    print("合計点と平均点を求めます。")
    number = int(input("学生の人数："))
    tensu = [None] * number

    for i in range(number):
        tensu[i] = int(input("{}番の点数：".format(i + 1)))

    total = 0
    for i in range(number):
        total += tensu[i]
    
    print("合計は{}点です。".format(total))
    print(f"平均は{int(total / number)}点です。")


if __name__ == "__main__":
    main()
