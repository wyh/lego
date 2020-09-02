import datetime
import sys
import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcdn.request.v20180510.\
    BatchSetCdnDomainServerCertificateRequest  \
    import BatchSetCdnDomainServerCertificateRequest

from aliyunsdkcore.acs_exception.exceptions import ServerException


root = ".lego/certificates/"

accessKeyId = sys.argv[1]
accessSecret = sys.argv[2]
domains = sys.argv[3]

client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')

request = BatchSetCdnDomainServerCertificateRequest()
request.set_accept_format('json')
request.set_SSLProtocol("on")
request.set_CertType("upload")


def construct_content(files):
    lines = []
    for f in files:
        filename = root + f
        fi = open(filename, 'r')
        for line in fi.readlines():
            lines.append(line)
    return "".join(lines)


def get_certificate():
    files = os.listdir(root)
    cert_files = filter(lambda f: f.endswith("crt"), files)
    return construct_content(cert_files)


def get_key():
    files = os.listdir(root)
    key_files = filter(lambda f: f.endswith("key"), files)
    return construct_content(key_files)


def upload_domain_cert(domain, suffix):
    cert_name = f"{domain}_{suffix}"
    request.set_DomainName(domain)
    request.set_CertName(cert_name)
    response = client.do_action_with_exception(request)
    return response


if __name__ == "__main__":
    today = datetime.date.today()
    today_str = today.strftime("%Y%m%d")
    cert = get_certificate()
    key = get_key()
    request.set_SSLPub(cert)
    request.set_SSLPri(key)

    for domain in domains.split(","):
        print("domain", domain)
        try:
            response = upload_domain_cert(domain, suffix=today_str)
            print(response)
        except ServerException as e:
            print("ERROR", e)
