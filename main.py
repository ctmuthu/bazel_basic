import sys
import requests

print(sys.version)

request = requests.get("https://raw.githubusercontent.com/ctmuthu/bazel_basic/master/WORKSPACE", verify=False)
print(request.content)