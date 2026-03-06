This development is a free asset tracker website for the Ontario Line

To use and update the database please do the following:

1. Replace the contents of "devices.csv" by the new devices to be added into the database and save (I recommend opening the file via Excel)
2. run append_devices.py and look for the printed output in the terminal - copy the output.
3. Paste the output to the end of init_db.py and make sure the indentationa and the format is the same. In there, do not replace the current values because that will be the entire database. Only delete if you want to eliminate devices from the website.
4. Go to instance and delete the database file: assets.db
5. Run init_db.py (that will create a new database file with the same name)
6. Paste the copied outputs from step 2 into the file generate_qr.py and run it to generate the respective qr codes, which will appear in the folder static\qrcodes. The script will generate a qr code for all of the devices in the file, so delete the ones you already generated or don't need.
7. Open Github with my account (carlos.rojas@tgp.build) and push + commmit the changes made to this folder.
8. Open Render with my account and deploy the latest commit: https://dashboard.render.com/web/srv-d1mmsbadbo4c73c4k26g
9. Share the corresponding qr codes.
