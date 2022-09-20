banner = """
development  python file dont downloads
"""
print(banner)

vpn = input("vpn name #> ")

if vpn == "us1":
    print(vpn + " connecting")
elif vpn == "us2":
    print(vpn + " vpn connecting")
else:
    print("vpn connecting to vpn "+vpn)
