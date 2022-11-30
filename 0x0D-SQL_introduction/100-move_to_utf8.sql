-- converting hbtn_0c_0 database to UTF8 in mysql
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name CHARACTER SET utf8mb4 COLLATE utf8_unicode_ci;
