

# Loop over each file in the dataset matching the wildcard pattern
for file in /data/Twitter\ dataset/geoTwitter20*.zip; do
    # Run map.py command using nohup to ensure it continues running
    nohup ./src/map.py --input_path="$file" > "map_output..log" 2>/dev/null &
done

echo "Mapping process started for all files from 2020."

