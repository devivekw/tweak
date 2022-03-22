import streamlink
streams = streamlink.streams("https://twitch.tv/tarik")

stream = streams["best"]

print(stream)


fd = stream.open()

data = fd.read(1024)

fd.close()