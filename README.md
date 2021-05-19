# pymeta-bulk
Run [m8r0wn/pymeta](https://github.com/m8r0wn/pymeta) against multiple domains and combine results into single CSV file.

1. Install [m8r0wn/pymeta](https://github.com/m8r0wn/pymeta)
2. Put all domains in a file called "urls.txt".
3. Run the following to use pymeta against the domains in urls.txt. Use your favourite VPN CLI client to switch IPs in order to circumvent Captchas.
```bash
while IFS= read -r line
do
echo "Running pymeta against $line..."
nordvpn c # replace with your VPN
pymeta -d $line -f ./$line.csv
nordvpn d # replace with your VPN
done < urls.txt
```

4. Save merge_csv.py in the current directory and run it to get a single CSV file:
```bash
$ python3 merge_csv.py 
processing example1.com.csv
processing example2.com.csv
processing example3.com.csv
Merged CSV files into out.csv
```
