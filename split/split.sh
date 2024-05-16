input_file="hebing.txt"
lines_per_file=100
counter=1
output_file="split_${counter}.txt"

while read -r line; do
  echo "$line" >> "$output_file"
  if [ $((counter % lines_per_file)) -eq 0 ]; then
    counter=$((counter + 1))
    output_file="split_${counter}.txt"
  else
    counter=$((counter + 1))
  fi
done < "$input_file"