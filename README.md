# Data Center Scale Computing

### CSCI-5253 - Fall 23 Dr. Alex Yarosh

---

### About 

This repository holds all the future and current homework assignment files as pull requests individualised as different branches.

---

### Lab03 Airflow -- Instructions to Run

##### Docker Compose Instantiation

* Instantiate Docker

Navigate inside the folder ( Make sure the `docker-compose.yml` is within the directory check with `ls` )

In the **terminal/wsl**, run the following

```bash
docker compose up
```

---

#### Cloud Instantiation References - Proof of Execution 

### Airflow Dag Represenation

![Example Image](assets/airflow-status.png)

## DAGs

<img width="1220" alt="Screenshot 2023-11-20 at 6 54 05 PM" src="https://github.com/r0han99/CSCI-5253-HW/assets/45916202/eb2c7ff7-70b8-4048-a718-e81eefea3384">

## Storing Data on to the Cloud - S3 Bucket

![Example Image](assets/s3-bucket.png)

## Cloud Relational Database - Amazon RDS

![Example Image](assets/data-warehouse.png)

## Connection Test to the Cloud RDS through DBeaver

<img width="1466" alt="Screen Shot 2023-11-20 at 6 59 46 PM" src="https://github.com/r0han99/CSCI-5253-HW/assets/45916202/968955e1-2ba2-42c6-8cfc-a3017f3062c7">

## Succesful Data Loading through the ETL process

<img width="1470" alt="Screen Shot 2023-11-20 at 6 58 57 PM" src="https://github.com/r0han99/CSCI-5253-HW/assets/45916202/9e01edaf-ae33-4bb3-ba6c-801f79367be7">


##### Note ~ Edit Credentials 

In order to execute the lab-3 code, nagivate to `/dags/secrets.env` replace the credentials items with your own before running the `docker-compose.yml`

----

