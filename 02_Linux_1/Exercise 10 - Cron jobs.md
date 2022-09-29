# [Cron jobs]
[Using Crontab to add scripts as Cronjobs.]

## Key terminology
[Write a list of key terminology with a short description. To prevent duplication you can reference to previous excercises.]

## Exercise
Wrote two scripts and scheduled them as Cron Jobs. One of them writes every minute to a text file in my home directory, while the other writes weekly to a log file in /var/log.
### Sources
[1. https://www.cyberciti.biz/faq/linux-display-date-and-time/

2. https://linuxize.com/post/how-to-set-or-change-timezone-in-linux/

3. https://www.cyberciti.biz/faq/unix-linux-getting-current-date-in-bash-ksh-shell-script/#:~:text=Sample%20shell%20script%20to%20display,scripts%20goes%20here%20%23%20...

4. https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/

5. https://opensource.com/article/18/7/how-check-free-disk-space-linux

6. https://stackoverflow.com/questions/82256/how-do-i-use-sudo-to-redirect-output-to-a-location-i-dont-have-permission-to-wr/16514624#16514624
7. ]

### Overcome challenges
[It took me a while to figure out why my script couldn't write to /var/log, but in the end I figured it out in time]

### Results
![Setting_timezone](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/d20370be767602548b7b59b1ff180852452c1a91/00_includes/Linux/Setting_timezone.png)
![Date_time_logging](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/d20370be767602548b7b59b1ff180852452c1a91/00_includes/Linux/Date_time_logging.png)
![Cron_nano](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/d20370be767602548b7b59b1ff180852452c1a91/00_includes/Linux/Cron_nano.png)
![Date_time_log](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/d20370be767602548b7b59b1ff180852452c1a91/00_includes/Linux/Date_time_log.png)
![Disk_logging](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/1c91d0049f5e1b3dc5dfb2a7bc39a4afe785c20d/00_includes/Linux/Disk_logging.png)
![Cron_nano(2)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/1c91d0049f5e1b3dc5dfb2a7bc39a4afe785c20d/00_includes/Linux/Cron_nano(2).png)
![Disk_log](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/1c91d0049f5e1b3dc5dfb2a7bc39a4afe785c20d/00_includes/Linux/Disk_log.png)