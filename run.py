import dotenv

if __name__ == '__main__':
    dotenv.load_dotenv()
    from bot import start
    start()