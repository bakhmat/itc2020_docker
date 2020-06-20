import sys
import urllib.request
# from time import sleep

if __name__ == "__main__":
    url_list = sys.argv
    for url in url_list:
        try:
            fp = urllib.request.urlopen(url)
            mybytes = fp.read()
            html_output = mybytes.decode("utf8")
            fp.close()
        except:
            html_output = ""

        print("### URL source ######################################################### \n\n")
        print(html_output)

# if __name__ == "__main__":
#     num = int(sys.argv[1])
#     for i in range(num):
#         print (str(i)+" "+str(i*i*i))
#         sleep(1)
