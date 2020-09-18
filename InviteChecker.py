import random
import string
import requests
import time
import multiprocessing

ids = []
letters = string.ascii_letters + string.digits
proxies = [line.rstrip('\n') for line in open("proxies.txt", 'r')]
headers = {
    'authority': 'discordapp.com',
    'accept-language': 'en-US',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.12 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://discordapp.com/channels/753876664286707742/753877454422278174',
    'accept-encoding': 'gzip, deflate, br'
}


def data(invite):
    return (
        ('inputValue', invite),
        ('with_counts', 'true'),
    )


def generateID(length):
    result_str = ''.join(random.choice(
        letters) for _ in range(length))
    return result_str


def checkIDExists(id, threadID):
    try:
        url = "https://discordapp.com/api/v8/invites/{id}".format(id=id)
        proxyNumber = random.randint(0,len(proxies))
        response = requests.get(url, proxies={"https": "http://" + proxies[proxyNumber].split(':')[0] + ":" + proxies[proxyNumber].split(':')[1]}, headers=headers, params=data(id))
        if response.status_code == 200:
            workingfile = open("working.txt", "a")
            workingfile.write(id + "\n")
            workingfile.close()
            print("Thread {threadID}: {id}: Valid(200)".format(threadID=threadID, id=id))
            return True
        elif response.status_code == 429:
            print("Thread {threadID}: {id}: Ratelimited(429) - {proxy}".format(threadID=threadID, id=id, proxy=proxies[proxyNumber]))
            return False
        else:
            print("Thread {threadID}: {id}: Invalid({status}) - {response}".format(
                threadID=threadID, id=id, status=response.status_code, response=response.text))
            return False
    except:
        return False


def threadLoop(threadID, codeLen):
    print("Started Thread " + str(threadID))
    while True:
        id = generateID(codeLen)
        checkIDExists(id, threadID)

def main():
    numThreads = int(input("Threads: "))
    codeLen = int(input("Invite code length (Random invites are 6 characters long): "))
    jobs = []
    for threadID in range(numThreads):
        p = multiprocessing.Process(target=threadLoop, args=(threadID, codeLen))
        jobs.append(p)
        p.start()

if __name__ == "__main__":
    main()
