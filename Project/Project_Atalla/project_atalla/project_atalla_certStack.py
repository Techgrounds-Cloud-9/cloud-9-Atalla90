# The purpose of this stack is creating the self-signed certificate for the alb and importing it to ACM.
# For this purpose we make use of some external libraries and modules, most importantly, crypto from OpenSSL and boto3.
# In the end we export the certificate construct in ACM as a class attribute to be consumed by the VPC stack.
import random
from aws_cdk import (
    aws_certificatemanager as acm,
    Stack,
    )
from OpenSSL import crypto
from constructs import Construct
import boto3
import time

class projectAtallaCertStack(Stack):

    atallaCert = acm.Certificate

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Importing boto3 ACM client.
        boto_acm = boto3.client('acm')
        # We attempt to list the certificates available in our ACM.
        cert_check = boto_acm.list_certificates()

        # We check if there are already any certificates in ACM. If so, we just use the first one that's there.
        # This aims to avoid creating multiple certificates for no reason. Since this code will get processed over
        # and over everytime we list, deploy or even destroy our stacks.
        if len(cert_check["CertificateSummaryList"]):
            cert = cert_check["CertificateSummaryList"][0]
            certArn = cert["CertificateArn"]
            atalla_cert = acm.Certificate.from_certificate_arn(self, "AtallaCert", certificate_arn = certArn)
            self.atallaCert = atalla_cert
        # If not, we create a certificate and we import it to ACM.
        else:
            ca_key = crypto.PKey()
            ca_key.generate_key(crypto.TYPE_RSA, 2048)
            ca_cert = crypto.X509()
            ca_cert.set_version(2)
            ca_cert.set_serial_number(random.randrange(100000))
            ca_subj = ca_cert.get_subject()
            ca_subj.C = "NL"
            ca_subj.ST = "Noord-Holland"
            ca_subj.L = "Amsterdam"
            ca_subj.O = "TechGrounds"
            ca_subj.OU = "AtallaProject"
            ca_subj.CN = "AtallaCA"
            ca_cert.add_extensions([
                crypto.X509Extension(b"subjectKeyIdentifier", False, b"hash", subject=ca_cert),
            ])
            ca_cert.add_extensions([
                crypto.X509Extension(b"authorityKeyIdentifier", False, b"keyid:always", issuer=ca_cert),
            ])
            ca_cert.add_extensions([
                crypto.X509Extension(b"basicConstraints", False, b"CA:TRUE"),
                crypto.X509Extension(b"keyUsage", False, b"keyCertSign, cRLSign"),
            ])
            ca_cert.set_issuer(ca_subj)
            ca_cert.set_pubkey(ca_key)
            ca_cert.sign(ca_key, 'sha256')
            ca_cert.gmtime_adj_notBefore(0)
            ca_cert.gmtime_adj_notAfter(10*365*24*60*60)
            ca_certifictate_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, ca_cert).decode('utf-8')

            client_key = crypto.PKey()
            client_key.generate_key(crypto.TYPE_RSA, 2048)
            client_cert = crypto.X509()
            client_cert.set_version(2)
            client_cert.set_serial_number(random.randrange(100000))
            client_subj = client_cert.get_subject()
            ca_subj.C = "NL"
            ca_subj.ST = "Noord-Holland"
            ca_subj.L = "Amsterdam"
            ca_subj.O = "TechGrounds"
            ca_subj.OU = "AtallaProject"
            client_subj.CN = "AtallaProject.com"
            client_cert.add_extensions([
                crypto.X509Extension(b"basicConstraints", False, b"CA:FALSE"),
                crypto.X509Extension(b"subjectKeyIdentifier", False, b"hash", subject=client_cert),
            ])
            client_cert.add_extensions([
                crypto.X509Extension(b"authorityKeyIdentifier", False, b"keyid:always", issuer=ca_cert),
                crypto.X509Extension(b"extendedKeyUsage", False, b"serverAuth"),
                crypto.X509Extension(b"keyUsage", False, b"digitalSignature"),
            ])
            client_cert.add_extensions([
                crypto.X509Extension(b'subjectAltName', False,
                    ','.join([
                        'DNS:*AtallaProject.com'
            ]).encode())])
            client_cert.set_issuer(ca_subj)
            client_cert.set_pubkey(client_key)
            client_cert.gmtime_adj_notBefore(0)
            client_cert.gmtime_adj_notAfter(9*365*24*60*60)
            client_cert.sign(ca_key, 'sha256')
            certifictate_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, client_cert).decode('utf-8')
            private_key_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, client_key).decode('utf-8')
            import_cert = {
                'certificate': certifictate_pem,
                'private_key': private_key_pem,
                'certificate_chain': ca_certifictate_pem
            }
            # We hold the code processing for 2 seconds to give the certificate time to be valid and therefore able to be imported.
            # Otherwise, the attempt to import the certificate may be processed within a fraction of a second after creating it.
            # Which means the certificate won't be valid yet causing failure of our code.
            time.sleep(2)
            import_cert = boto_acm.import_certificate(
                Certificate=certifictate_pem,
                PrivateKey=private_key_pem,
                CertificateChain=ca_certifictate_pem,
            )
            certArn = import_cert["CertificateArn"]
            # Finally, we create the ACM certificate construct using the arn we get as part of the dict value returned from the
            # boto3 import_certificate function.
            atalla_cert = acm.Certificate.from_certificate_arn(self, "AtallaCert", certificate_arn = certArn)
            self.atallaCert = atalla_cert