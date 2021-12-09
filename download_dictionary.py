# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import hashlib
import os
import requests
import json


BASE_URL = "http://www.eibarko-euskara.eus"


def download_dictionary():
    letters = [
        "a",
        "b",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "r",
        "s",
        "t",
        "u",
        "x",
        "z",
    ]
    words = []
    try:
        for letter in letters:
            dictionary_url = f"{BASE_URL}/hiztegia/letra/{letter}"
            words += download_page(dictionary_url)
    except KeyboardInterrupt:
        print("Process interrupted")

    with open("dictionary.json", "w") as f:
        json.dump(words, f)


def download_page(dictionary_url):
    if not dictionary_url.startswith("http"):
        dictionary_url = BASE_URL + dictionary_url
    words = []
    # Find next page
    res = requests.get(dictionary_url)
    if res.ok:
        soup = BeautifulSoup(res.text, "html.parser")
        pages = soup.find_all("a", {"class": "pager-next"})
        for page in pages:
            if page.attrs.get("title", "").startswith("Hurrengo orrira"):
                print("Hurrengoa")
                words += download_words_from_url(page.attrs.get("href"))
                words += download_page(page.attrs.get("href"))
                break

    return words


def download_words_from_url(url):
    if not url.startswith("http"):
        url = BASE_URL + url

    print(f"Processing {url}")
    file_contents = get_file_contents(url)
    words = extract_words_from_html(file_contents)
    return words


def get_file_contents(url):
    hashed_filename = hashlib.md5(url.encode("utf-8")).hexdigest()
    if hashed_filename in os.listdir("cache"):
        with open(f"cache/{hashed_filename}", "r") as f:
            return f.read()

    else:
        res = requests.get(url)
        if res.ok:
            with open(f"cache/{hashed_filename}", "w") as f:
                f.write(res.text)
            return res.text
        else:
            return []


def extract_words_from_html(html):
    words = []
    soup = BeautifulSoup(html, "html.parser")
    entries = soup.find_all("span", {"class": "sarrera"})
    for entry in entries:
        links = entry.find_all("a")
        for link in links:
            word = extract_word_info_from_url(link.attrs.get("href"))
            words.append(word)

    return words


def extract_word_info_from_url(url):
    word = {}
    if not url.startswith("http"):
        url = BASE_URL + url

    contents = get_file_contents(url)

    soup = BeautifulSoup(contents, "html.parser")
    word["url"] = url
    table = soup.find("table", {"class": "berba-taula"})
    for tr in table.find_all("tr"):
        if tr.find("th") and tr.find("th").text == "Sarrera":
            word["entry"] = tr.find("td").text
        if tr.find("th") and tr.find("th").text == "Esanahia":
            word["meaning"] = tr.find("td").text
        if tr.find("th") and tr.find("th").text == "Kategoria gramatikala":
            word["category"] = tr.find("td").text

    return word


if __name__ == "__main__":
    download_dictionary()
