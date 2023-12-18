import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return '''Hey there!! I'm Dicey, the cutest little dice. 
        Guess what? I have a superpower too! I can bring luck and happiness to all your games. 
        Whenever you need that extra boost to win, just give me a the following commands, 
        and I'll be there to cheer you on. Together, we'll make every game more exciting and enjoyable!
                  
        commands:
            hello - for selfintro
            roll - to roll the dice
            help - if stuck anywhere'''

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'help':
        return "`check for typos`"

    return 'I didn\'t understand what you wrote. Try typing "help".'