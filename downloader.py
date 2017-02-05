import requests;
import re;
import sys;
import os;

PY3 = sys.version_info[0] == 3
if PY3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve
links = sys.argv[1:];
downloadlink = "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=47.0&x=id%3D{}%26installsource%3Dondemand%26uc"
extensionids = [];
regexx = re.compile("http[s]?.+\/(?P<lastpart>.+)");
for link in links:
    extensionids.append(regexx.search(link).group("lastpart"));

for extensionid in extensionids:
    link = downloadlink.format(extensionid);
    extensiondownload = requests.get(link,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"}).url;
    urlretrieve(extensiondownload,"/tmp/{}.crx".format(extensionid));
    if sys.platform == "darwin":
      os.system("open /Applications/Chromium.app /tmp/%s.crx" % extensionid);
    else:
      os.system("inox /tmp/%s.crx" % extensionid);
