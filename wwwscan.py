import requests
def scanner(url,script_type):
    f=open("resualt.html","a")
    f.write("<title>Scanning Result</title>\n")
    f.close()
    dic=open(script_type.upper()+".txt","rb").readlines()
    for line in dic:
        web=url+line.decode()
        web_real=web.strip()
        #print(web_real)
        code=requests.get(web_real)
        if code.status_code==200:
            f=open("resualt.html","a")
            f.write('<a href="{}">{}</a>\n'.format(web_real,web_real+" 200 OK"))
            print("[*]"+web_real+" Found")
            f.close()
        elif code.status_code==404:
            print("[*]NOT found 404")

def get_code(url):
    code=requests.get(url).status_code
    return code
while 1:
    url=input("[*]Please put in the website:")
    if(url=="" or url.count("/")!=2):
        print("[*]fa♂q Please put in the website url!")
    else:
        break
script_type=input("[*]Please put in the script type:")
if(script_type==""):
    if(get_code(url+"/index.asp")==200):
        script_type="asp"
    if(get_code(url+"/index.php")==200):
        script_type="php"
    if(get_code(url+"/index.aspx")==200):
        script_type="aspx"
    if(get_code(url+"/index.jsp")==200):
        script_type="jsp"
    if(get_code(url+"/index.php")==200):
        script_type="php"
    if(get_code(url+"/index.aspx")==200):
        script_type="aspx"
print("[*]Now start scanning!")
scanner(url,script_type)
