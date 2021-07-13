# Split pdf to HKACMGM eBook format

## usage

- save the pdf need to be converted to `file_to_convert` folder.
- start `pipenv shell` first and then run the script `python split_pdf.py ./file_to_convert/*.pdf`
- upload the converted jpgs and the pdf to hkacmgm.org folder with the following script.

```sh
scp -r ./file_to_convert/* cyrusncy@hkacmgm.org:/home/vpdf/public/pages/
rm -rf ./file_to_convert
mkdir file_to_convert
```
