CREATE TABLE Animal (
    Animal_ID VARCHAR(255) PRIMARY KEY,
    Breed VARCHAR(255),
    Color VARCHAR(255),
    Name VARCHAR(255),
    Date_of_Birth DATE,
    Animal_Type VARCHAR(255)
);

CREATE TABLE Outcome_Type (
    Outcome_Type_ID INT PRIMARY KEY,
    Outcome_Type VARCHAR(255) UNIQUE
);

CREATE TABLE Outcome_Event (
    Outcome_Event_ID INT PRIMARY KEY,
    DateTime TIMESTAMP,
    Sex_upon_Outcome VARCHAR(255),
    Outcome_Subtype VARCHAR(255),
    Animal_ID VARCHAR(255),
    Outcome_Type_ID INT,
    FOREIGN KEY (Animal_ID) REFERENCES Animal(Animal_ID),
    FOREIGN KEY (Outcome_Type_ID) REFERENCES Outcome_Type(Outcome_Type_ID)
); 