# ------------ check imports -------------#
try:
    pass
except ModuleNotFoundError:
    print(
        """
    Looks like you dont have required libraries installed to run this bot.

    Inatall by "pip install -r requirements.txt"
    """
    )
    exit(1)

try:
    from bot import BaseBot
except ModuleNotFoundError as e:
    print(f"essential files are missing/not found in current diectory: {e}")
    exit(1)

bot = BaseBot()

bot.run()
