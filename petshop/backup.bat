@ECHO OFF

IF EXIST backup_petshop.sql DEL backup_petshop.sql
SET PGPASSWORD=victor

ECHO Realizam backup-ul datelor...

(FOR %%t IN (
    "magazin_locatie" 
    "magazin_animal" 
    "magazin_categorie" 
    "magazin_brand" 
    "magazin_furnizor" 
    "magazin_serviciu" 
    "magazin_pret_serviciu" 
    "magazin_produs" 
    "magazin_oferta"
) DO (
    ECHO Exportam tabelul %%t
    
    "C:\Program Files\PostgreSQL\18\bin\pg_dump.exe" --column-inserts --data-only --inserts -h localhost -U victor -p 5432 -d dj2025 -t %%t >> backup_petshop.sql
))

SET PGPASSWORD=
