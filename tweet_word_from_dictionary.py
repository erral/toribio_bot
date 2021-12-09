# -*- coding: utf-8 -*-
import json
import datetime
import random
from TwitterAPI import TwitterAPI


def tweet_word_from_dictionary():
    word = get_random_untweeted_word()
    if word:
        tweet_word(word)


def get_random_untweeted_word():
    dictionary = json.load(open("dictionary.json"))
    word = random.choice(dictionary)
    while word and word.get("tweeted"):
        word = random.choice(dictionary)

    word["tweeted"] = True
    word["tweeted_at"] = datetime.datetime.utcnow().isoformat()
    dictionary.remove(word)
    dictionary.append(word)
    json.dump(dictionary, open("dictionary.json", "w"))

    return word


def tweet_word(word):
    text = "Egunian berba edo esamolde bat. Gaur {word}: {meaning} {url} #eibar #eibarkoeuskara"
    text = text.format(
        word=word["entry"], meaning=word["meaning"].strip(), url=word["url"]
    )

    with open("credentials.twitter.json") as fp:
        credentials = json.load(fp)

        api = TwitterAPI(
            credentials["API_KEY"],
            credentials["API_SECRET"],
            credentials["ACCESS_TOKEN_KEY"],
            credentials["ACCESS_TOKEN_SECRET"],
        )
        res = api.request("statuses/update", {"status": text})
        if res.response.ok:
            print('Tweeted: "{}"'.format(text))


if __name__ == "__main__":
    tweet_word_from_dictionary()
