# [Elastic Block Store (EBS)]

[Studying EBS.]

## Key terminology

[Elastic Block Store (EBS): A part of Amazon EC2. It enables the user of creating virtual storage devices, called Volumes, that can be formatted, configured and mounted such as any storage device. AWS recommends using EBS for data that needs to be quickly accessible and requires long-term persistence. An EBS volume created in one AZ has to be attached to an EC2 instance in the same AZ.

SSD: Solid-State Drive, is a storage device that uses flash-based memory to store the data, making it faster in storing the data than the traditional HDD.

HDD: Hard Drive Disk, is an older generation of storage devices that are usually installed in computers.

Throughput: The amount of data a system can process in a given amount of time.

Root volume: An EBS volume the gets created when creating the EC2 instance. It acts like a built-in storage device of the instance. A root volume can't be detached when the instance is running.

Non-root volume: An EBS volume that gets created separatly from any instances and can be attached with and detached from any instance in the same AZ, like an external storage device.

IOPS: Input/output Operations Per Second, is the measurement of the performance of the reading and writing processes on a storage device.

Snapshot: An image of an EBS volume, created to save the state of the volume at a certain time for backup and duplication purposes. With a snapshot you can create copies of the same EBS volume in different AZs or regions.]

## Exercise

1. Created a new EC2 instance with the provided requirements.

2. Created a new non-root volume, attached it to the new EC2 instance, created a file system for the volume and mounted it, changed its owner to my user and wrote a text file to it.

3. Made a snapshot of the new volume, deleted the text file, created a new volume of the snapshot, detached the original volume and connected and mounted the new one. The text file was there along with the whole file system of the original volume.

### Sources

[1. <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html>

2. <https://www.avast.com/c-what-is-ssd>

3. <https://www.techtarget.com/searchstorage/definition/hard-disk-drive>

4. <https://www.webopedia.com/definitions/throughput/>

5. <https://en.wikipedia.org/wiki/IOPS>

6. <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html>]

### Overcome challenges

[]

### Results

![Volume_Attached](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/11231cfdf977031d304cf856a1b86855523d47ef/00_includes/Cloud(AWS)/Volume_Attached.png)  
![Volume_Mount](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/11231cfdf977031d304cf856a1b86855523d47ef/00_includes/Cloud(AWS)/Volume_Mount.png)  
![Snapshot_Created](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/11231cfdf977031d304cf856a1b86855523d47ef/00_includes/Cloud(AWS)/Snapshot_Created.png)  
![Snapshot_Volume](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/11231cfdf977031d304cf856a1b86855523d47ef/00_includes/Cloud(AWS)/Snapshot_Volume.png)  
![Snapshot_Volume_Data](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/11231cfdf977031d304cf856a1b86855523d47ef/00_includes/Cloud(AWS)/Snapshot_Volume_Data.png)
