import asyncio


async def main(n):

    a = 0
    b = 1

    for i in range(n):
        if i == 0:
            print(a)
        else:
            if i == 1:
                print(b)
            else:   
                print(a+b)
                temp = a
                a = b
                b = temp + b

        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main(10))