import struct

a = struct.unpack("I","abcd")[0]
b = struct.unpack("I","efgh")[0]
c = struct.unpack("I","ijkl")[0]
d = struct.unpack("I","mnop")[0]
e = struct.unpack("I","qrst")[0]
abcd =  a+b+c+d
bina = bin(abcd & 0xffffffff)
print int(bina,2)
#in signed int abcd = -1448762980
tmp = -1448762980
bina = bin(tmp & 0xffffffff)
print int(bina,2)

print ''
print 'a+b+c+d+e = '
abcde = a+b+c+d+e
print abcde
print "in 32bits = "
bina = bin(abcde & 0xffffffff)
bin1 =  int(bina,2)
print bin1
resf = 568134124  #final hash required
resint = resf - bin1
print resint
#a+b+c+d+e = 504960013
print resint + e # 4 bytes to use 2016897104
print ''

#the final char should be 0x21DD09EC = 568134124
#
print struct.pack("i",2016897104)
print "the last 4 bytes has to be Ph7x"
print "abcdefghijklmnopPh7x"

#Getting the key
import paramiko
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect('pwnable.kr', port=2222, username='col', password='guest')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("./col abcdefghijklmnopPh7x")
ssh_stdin.close()
print "*********** Flag ****************"
for line in ssh_stdout.read().splitlines():
    print(line)
