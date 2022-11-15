from pytube import YouTube

link = input("               Enter link of Youtube Video (or type -1 to exit): ")

while(link != -1):
    print("\n")
    yt = YouTube(link)

    print("<>Title: ", yt.title)
    print("<>Views: ", yt.views)
    print("<>Duration: ", yt.length)
    print("<>Description: ", yt.description)
    print("\n")

    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("<>DOWNLOAD COMPLETED!\n")
    link = input("              Enter link of Youtube Video (or type -1 to exit): ")


