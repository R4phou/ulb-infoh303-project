                        +-------------+  
                        |   Patient   |  
                        +-------------+  
                        |  Firstname  |  
                        |   Lastname  |  
                        |    Gender   |  
                        | DateOfBirth|  
                        |     NISS    |  
                        |   Email     |  
                        |   Phone     |  
                        +-------------+  
                               |      
                               |      
                     +-----------------+ 
                     |  HealthRecord   |  
                     +-----------------+ 
                     |  PatientId (FK) | 
                     |  DoctorId (FK)  | 
                     |  PharmacistId (FK)| 
                     |  PathologyId (FK)| 
                     +-----------------+ 
                               |      
                 ------------------------  
                 |           |           |  
                 |           |           |  
      +---------------+ +---------------+ +---------------+ 
      |     Doctor    | |   Pharmacist  | |   Pathology   | 
      +---------------+ +---------------+ +---------------+ 
      |     Name      | |     Name      | |     Name      | 
      |   INAMI_Number| |  INAMI_Number | | SystemAnatomy | 
      |   Specialty   | |   Phone      | +---------------+ 
      |     Email     | +---------------+ 
      +---------------+ 

         +-------------------+ 
         |      Medicine     | 
         +-------------------+ 
         |      DCI          | 
         | Commercial_Name   | 
         |   Packaging_Size  | 
         +-------------------+ 
                 |      
                 |      
        +----------------------+ 
        |      Prescription     | 
        +----------------------+ 
        | PrescriptionId (PK)   | 
        | MedicineId (FK)       | 
        | DoctorId (FK)         | 
        | Duration              | 
        +----------------------+ 
                 |      
                 |      
         +-------------------+ 
         |     Treatment     | 
         +-------------------+ 
         | PatientId (FK)    | 
         | PrescriptionId (FK)| 
         | PharmacistId (FK)  | 
         | StartDate         | 
         | Duration          | 
         +-------------------+ 
