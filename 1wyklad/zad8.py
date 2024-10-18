import asyncio


async def wczytanie(nazwaPliku) -> None:
    await asyncio.sleep(2)
    print("Wczytano Plik " + nazwaPliku)


async def analiza(nazwaPliku) -> None:
    await asyncio.sleep(4)
    print("Skonczono Analize Pliku " + nazwaPliku)


async def zapis(nazwaPliku) -> None:
    await asyncio.sleep(1)
    print("Zapisano Plik " + nazwaPliku)


async def przetworzeniePliku(nazwaPliku) -> None:
    await wczytanie(nazwaPliku)
    await analiza(nazwaPliku)
    await zapis(nazwaPliku)
    print("Przetworzono plik " + nazwaPliku)

async def main() -> None:
    await asyncio.gather(przetworzeniePliku('1'), przetworzeniePliku('2'),
                         przetworzeniePliku('3'), przetworzeniePliku('4'),
                         przetworzeniePliku('5'))


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())