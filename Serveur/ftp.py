import ftplib
session = ftplib.FTP('test.test','test','azerty123')
file = open('kitten.jpg','rb')                  # file to send
session.storbinary('STOR kitten.jpg', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
