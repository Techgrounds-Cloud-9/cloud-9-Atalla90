# [Public Key Infrastructure]
[Getting to know about Public Key Infrastructure and digital certification.]

## Key terminology
[Public Key Ifrastructure (PKI): A set of rules and other elements that controls digital certification and manages asymmetric encryption using public keys.

Digital certificate: A piece of cipher text in a certain digital form that belongs to a certain entity and used to prove their authenticity to other parties in digital communications. Digital certification is a main component of PKI.

Certificate Authority (CA): Another main component of PKI. CA is the authority responsible for judging in certificate requests and eventually issuing the certificates.

Registration Authority (RA): Another main component of PKI. RA is authorized by CA to accept certification requests from users and provide digital certificates based on each individual case.

TLS/SSL Certificate: A certificate granted to a server to insure the security of communication between that server and other client hosts. HTTPS protocol utilizes TLS/SSL certificates.

X.509: An international standard defines the form which a public key certificate should have.]

## Exercise
Created a self-signed digital certificate on my Linux VM, Analyzed the certificate path of a couple of websites and found the list of trusted certificates both on my Windows system and on my Linux VM.

### Sources
[1. https://documentation.observeit.com/installation_guide/finding_the_path_to_the_trusted_certificates.htm

2. https://en.wikipedia.org/wiki/Public_key_infrastructure

3. https://www.venafi.com/education-center/pki/how-does-pki-work#:~:text=There%20are%20three%20key%20components,certificate%20authority%2C%20and%20registration%20authority.

4. https://en.wikipedia.org/wiki/X.509]

### Overcome challenges
[]

### Results
![My_certificate](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a42886279f9462ea7fbab31da4ea53e769668623/00_includes/Security/My_certificate.png)
![Google_cer_gen](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a42886279f9462ea7fbab31da4ea53e769668623/00_includes/Security/Google_cer_gen.png)
![Google_cer_details](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a42886279f9462ea7fbab31da4ea53e769668623/00_includes/Security/Google_cer_details.png)
![ING_cer_gen](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a42886279f9462ea7fbab31da4ea53e769668623/00_includes/Security/ING_cer_gen.png)
![ING_cer_details](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a42886279f9462ea7fbab31da4ea53e769668623/00_includes/Security/ING_cer_details.png)
![TechGrounds_cer_gen](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a42886279f9462ea7fbab31da4ea53e769668623/00_includes/Security/TechGrounds_cer_gen.png)
![TechGrounds_cer_details](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a42886279f9462ea7fbab31da4ea53e769668623/00_includes/Security/TechGrounds_cer_details.png)
![Trusted_cer_root_Windows](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a42886279f9462ea7fbab31da4ea53e769668623/00_includes/Security/Trusted_cer_root_Windows.png)
![Cert_root_Linux](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a42886279f9462ea7fbab31da4ea53e769668623/00_includes/Security/Cert_root_Linux.png)