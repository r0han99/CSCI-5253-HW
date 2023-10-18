# Data Center Scale Computing

### CSCI-5253 - Fall 23 Dr. Alex Yarosh

---

### About 

This repository holds all the future and current homework assignment files as pull requests individualised as different branches.

---

### HW2 - Intructions to Run 

##### Docker Compose Instantiation

* Instantiate Docker

Navigate inside the folder ( Make sure the `docker-compose.yml` is within the directory check with `ls` )

In the **terminal/wsl**, run the following

```bash
docker compose up --build
```

---

#### Expected Output

```
csci-5253-hw-etl-1  | Etl Pipeline
csci-5253-hw-etl-1  | --------------------------------------------------
csci-5253-hw-etl-1  | Data Received!
csci-5253-hw-etl-1  | --------------------------------------------------
csci-5253-hw-etl-1  | Transforming Data.
csci-5253-hw-etl-1  | - Converting datetime and date_of_birth to datetime objects and transforming them to the pattern mm/dd/yyyy
csci-5253-hw-etl-1  | - Filling NA.
csci-5253-hw-etl-1  | - Creating ID for Outcome type and Outcome Event Type.
csci-5253-hw-etl-1  | - Dividing into Entities
csci-5253-hw-etl-1  | Data Transformed.
csci-5253-hw-etl-1  | --------------------------------------------------
csci-5253-hw-etl-1  | Received transformed data.
csci-5253-hw-etl-1  | --------------------------------------------------
csci-5253-hw-etl-1  | - Firing up Postgres
csci-5253-hw-etl-1  | - Connection Established.
csci-5253-hw-etl-1  | - Loading Data
csci-5253-hw-etl-1  | --------------------------------------------------
csci-5253-hw-etl-1  | Data Load Completed.
csci-5253-hw-etl-1  | 
csci-5253-hw-etl-1  | 
csci-5253-hw-etl-1  | 
csci-5253-hw-etl-1  |         ,/  \.
csci-5253-hw-etl-1  |        |(    )|
csci-5253-hw-etl-1  |   \`-._:,\  /.;_,-'/
csci-5253-hw-etl-1  |    `.\_`')(`/'_/,'
csci-5253-hw-etl-1  |        )/`.,'\(
csci-5253-hw-etl-1  |        |.    ,|
csci-5253-hw-etl-1  |        (@)  (@)
csci-5253-hw-etl-1  |         \`\ _('
csci-5253-hw-etl-1  |          \._'; `.___...---..________...------._
csci-5253-hw-etl-1  |           \   |   ,'   .  .     .       .     .`:.
csci-5253-hw-etl-1  |            \`.' .  .         .   .   .     .   . \
csci-5253-hw-etl-1  |             `.       .   .  \  .   .   ..::: .    ::
csci-5253-hw-etl-1  |               \ .    .  .   ..::::::::''  ':    . ||
csci-5253-hw-etl-1  |                \   `. :. .:'            \  '. .   ;;
csci-5253-hw-etl-1  |                 `._  \ ::: ;           _,\  :.  |/(
csci-5253-hw-etl-1  |                    `.`::: /--....--- \ `. :. :`\`   '
csci-5253-hw-etl-1  |                     | |:':               \  `. :.'  '
csci-5253-hw-etl-1  |                     | |' ;                \  (\  .'  (*)
csci-5253-hw-etl-1  |                     | |.:                  \  \`.  :
csci-5253-hw-etl-1  |                     |.| |                   ) /  :.|
csci-5253-hw-etl-1  |                     | |.|                  /./   | |
csci-5253-hw-etl-1  |                     |.| |                 / /    | |
csci-5253-hw-etl-1  |                     | | |                /./     |.|
csci-5253-hw-etl-1  |                     ;_;_;              ,'_/      ;_|
csci-5253-hw-etl-1  |                     -/_(              '--'      /,'   ETL-v2.
csci-5253-hw-etl-1  | 


```

---

##### Note ~ Docker Compose Functionality

Docker compose file maps the port 5432 from the container image to the local computer's port 5432. Connection to the database and Load functionality can be validated by manually connecting to the database by using the credentials specified under `credentials.txt`  through any database management tool like `DBeaver`. 

----

