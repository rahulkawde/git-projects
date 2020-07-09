import subprocess
data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8',errors='backslashreplace').split('\n')
profiles = [i.split(':')[1][1:-1]for i in data if 'all user profile' in i ]
for i in profiles:
    try:
        result =subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8',errors='backslashreplace').split('\n')
        result= [b.split(':')[1][1:-1] for b in result if 'key content' in b ]
        try:
            print('{:<30}| {:<})',format(i,result[0]))
        except IndexError:
            print('{:<30}| {:<})',format(i,''))
    except subprocess.CalledProcessError:
        print('{:<30}| {:<})',format(i,'Encoding error'))
input('')



