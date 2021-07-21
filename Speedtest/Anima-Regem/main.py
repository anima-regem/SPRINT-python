import speedtest

spt = speedtest.Speedtest()
spt.download()
spt.upload()
spt.get_best_server()
print(f'''Download Speed : {int(spt.results.download/8000)} KB/s
Upload Speed : {int(spt.results.upload/8000)} KB/s
Ping : {spt.results.ping}''')