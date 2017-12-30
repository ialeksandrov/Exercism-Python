def hey(phrases):
    """Bob is a lackadaisical teenager. In conversation, his responses are very limited.

    Bob answers 'Sure.' if you ask him a question.

    He answers 'Whoa, chill out!' if you yell at him.

    He says 'Fine. Be that way!' if you address him without actually saying
    anything.

    He answers 'Whatever.' to anything else."""
    phrases = phrases.strip()
    if not phrases:
        return "Fine. Be that way!"
    if phrases.isupper():
        return 'Whoa, chill out!'
    if phrases.endswith('?'):
        return 'Sure.'

    return 'Whatever.'
