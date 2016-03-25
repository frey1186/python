import configparser




config = configparser.ConfigParser()
config["DEFAULT"] = {
    'HOST': '127.0.0.1',
    'PORT': '12345',
}
config["felo"] = {
    'password':'password',
    'quotation': 1000000, #1GB
}

config["alex"] = {
    'password':'password',
    'quotation': 1000000, #1GB
}

with open('ftpd.conf', 'w') as configfile:
   config.write(configfile)
# config_file = "ftpd.conf"
# config = configparser.ConfigParser()
# config.read(config_file)
#
# # HOST = config["default"]["host"]
# # PORT = config["default"]["port"]
# a = config.sections()
# print(a)