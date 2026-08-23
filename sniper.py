import requests as r
import time
import threading
import string
import random

headers = {
  "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36",
  "Accept": "*/*",
  "Accept-Encoding": "deflate, gzip",
}

api = "https://api.mojang.com/users/profiles/minecraft/"
webhook = "https://discord.com/api/webhooks/1540133941695094844/Z8QG38RXQ17ZI5IkgEd-HlD6Wy91AKNCFjzpgBMBP0UDjnKfkkXQUaz6GrQIHAdiaiYj"

locktime = 5184000
length = 4
checked = set()

def sendtowebhook(name):
    data = {
        "content" : "",
        "username" : "alexandru gay"
    }
    data["embeds"] = [
        {
            "description" : f"Minecraft username found!\nName: {name}",
            "title" : f"Minecraft username found! Length: {len(name)}"
        }
    ]
    r.post(webhook, json = data)

def isitvalid(name):
    if name in checked:
        print(f"[X] {name} has already been checked")
        return False
    else:
             try:
            results = r.get(
                api + name + f"?at={int(time.time() - locktime)}",
                headers=headers,
                timeout=10
            )

            if results.status_code == 404:
                checked.add(name)
                sendtowebhook(name)
                print(f"[V] {name} is available!")
                return True
            else:
                print(f"[X] {name} isn't available!")
                return False

        except Exception as e:
            print(f"[!] Error: {e}")
            time.sleep(2)
            return False
length = random.choice([4,5])

def generate():
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxz"

    randomstring = ""

    for i in range(length):
        if i % 2 == 0:
            randomstring += random.choice(consonants)
        else:
            randomstring += random.choice(vowels)

    print(f"[*] Checking {randomstring}")
    isitvalid(randomstring)

while True:
    threading.Thread(target=generate).start()
    time.sleep(0.5)

