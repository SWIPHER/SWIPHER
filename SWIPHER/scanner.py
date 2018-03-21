def scanner(url,script_type):
    f=open("resualt.html","a")
    f.write("<title>Scanning Result</title>\n")
    f.close()
    dic=open(script_type.upper()+".txt").readlines()
    for line in dic:
        web=url+line
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
