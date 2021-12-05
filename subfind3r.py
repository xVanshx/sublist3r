import requests
import optparse

parser = optparse.OptionParser()
parser.add_option("-d", "--domain", dest="domain", help="Enter   the Domain")
(options, arguements) = parser.parse_args()

domain = options.domain
file = open('wordlist.txt','r')
content = file.read()
subdomains = content.splitlines()

def banner():
  print("\u001b[33m╭━━━╮╱╱╭╮╱╭━━━╮╱╱╱╱╱╭┳━━━╮")
  print("\u001b[33m┃╭━╮┃╱╱┃┃╱┃╭━━╯╱╱╱╱╱┃┃╭━╮┃")
  print("\u001b[33m┃╰━━┳╮╭┫╰━┫╰━━┳┳━╮╭━╯┣╯╭╯┣━╮")
  print("\u001b[33m╰━━╮┃┃┃┃╭╮┃╭━━╋┫╭╮┫╭╮┣╮╰╮┃╭╯")
  print("\u001b[33m┃╰━╯┃╰╯┃╰╯┃┃╱╱┃┃┃┃┃╰╯┃╰━╯┃┃")
  print("\u001b[33m╰━━━┻━━┻━━┻╯╱╱╰┻╯╰┻━━┻━━━┻╯")
  print("\u001b[33m\nVersion 1.0")
  print("\u001b[33mCopyright: xVanshx")
  print("\u001b[33mhttps://github.com/xVanshx/sublist3r")

banner()

for subdomain in subdomains:
	url1 = f"http://{subdomain}.{domain}"
	url2 = f"https://{subdomain}.{domain}"
	try:
		requests.get(url1)
		print(f"\u001b[32m[+]Discovered URL: {url1}")
		requests.get(url2)
		print(f"\u001b[32m[+]Discovered URL: {url2}")
	except requests.ConnectionError:
		pass
