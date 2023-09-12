# Data Center Scale Computing

### CSCI-5253 - Fall 23 Dr. Alex Yarosh

---

### About 

This repository holds all the future and current homework assignment files as pull requests individualised as different branches.

---

### HW1 - Intructions to Run 

##### Docker Instantiation

* Instantiate Docker

Navigate inside the folder ( Make sure the Dockerfile is within the directory check with `ls` )

In the **terminal/wsl**, run the following

```bash
docker build -t pandas-pipeline:0.1 .
```

##### Running Docker Image

```bash
docker run -it pandas-pipeline:0.1 --read --transform dob
```

The --read and --transform ( dob ) flag and options respectively are native to the data-pipeline script that is run at the entrypoint of the docker image, without these flags the script does nothing. 

*Expected Output from the docker run*

```shell
Transformation
- Dropping redundancies
- Converting to Datetime objects
- Individualising Month, Day and Year to different columns
- Transformation Done!
- Saving Transformed data. transformed data is saved as /app/transformed-data.csv.
-------------------------------------------------------
Job Completed.

```



---



